"""
This script provides functionality for connecting to a language model (LLM) with structured 
outcomes and validating the responses using Pydantic models. It includes functions to send 
prompts to the OpenAI API, process the responses, and validate them against a provided schema.

The script also includes a retry mechanism to ensure that the responses follow the expected 
structured format.

Functions:
- validate_response_with_model(response_content, base_model): 
    Validates the response content using the provided Pydantic model.
- process_response(chat_response, messages, base_model=None): 
    Processes the ChatGPT response and optionally validates it with a base model.
- send_prompt(messages, base_model=None): 
    Sends a query to ChatGPT using the OpenAI API and optionally validates responses with a 
    Pydantic model.
"""

import os
import openai
from openai import OpenAI, OpenAIError
from llm_services.prompts_checklist import prompt_system_role
from llm_services.models_content import (
    NoInfoModel, TableModel, ClauseModel, ClauseSummaryModel, IdentifyExternalIdsModel,
    IdentifyTablesModel, IdentifyClausesModel, IdentifyInformationModel)
from utils.messages import add_message

def validate_response_with_model(response_content, base_model):
    """
    Validate the response content using the provided base_model.
    
    Parameters:
    - response_content (str): The JSON content to validate.
    - base_model (Pydantic model): The model to use for validation.
    
    Returns:
    - dict: Validated response if successful.
    - None: If validation fails.
    """
    try:
        return base_model.model_validate_json(response_content)
    except (ValueError, TypeError) as e:
        print(f"Validation error: {e}")
        print("The LLM did not return the expected structured outcome, retrying...")
        return None


def process_response(chat_response, messages, base_model=None, bool_iso_model=False):
    """
    Process the ChatGPT response, optionally validating it with a base model.
    
    Parameters:
    - chat_response (object): The response from the OpenAI chat completion API.
    - messages (list of dict): The conversation history.
    - base_model (Pydantic model, optional): Model for validating structured responses.
    
    Returns:
    - dict or None: Validated response or None if validation fails.
    """
    response = chat_response.choices[0].message
    tool_calls = getattr(response, 'tool_calls', None)

    if base_model and bool_iso_model:
        if tool_calls and len(tool_calls) > 0:
            tool_response = next(
                (call.function.arguments for call in tool_calls
                 if call.function.name == "NoInfoModel"),
                None
            )
            if tool_response:
            # Validate response using a specialized ISO-compliant method
                validated_response = validate_response_with_model(tool_response, NoInfoModel)
                if validated_response:
                    # Store conversation history
                    for msg in messages:
                        add_message(msg['role'], msg['content'], base_model)
                    add_message("system", "Nothing found", base_model)
                    return validated_response
    if base_model:
        if tool_calls and len(tool_calls) > 0:
            tool_response = tool_calls[0].function.arguments
            validated_response = validate_response_with_model(tool_response, base_model)
            if validated_response:
                # Store conversation history
                for msg in messages:
                    add_message(msg['role'], msg['content'], base_model)
                add_message("system", validated_response, base_model)
                return validated_response
        return None
    # Store conversation history
    if response.content:
        for msg in messages:
            add_message(msg['role'], msg['content'], base_model)
        add_message("system", response.content, base_model)
        return response.content
    return None


def send_prompt(messages, base_model=None):
    """
    Send a query to ChatGPT using the OpenAI API and optionally validate responses with a 
    Pydantic model.

    Parameters:
    - messages (list of dict): Messages to send, each containing 'role' and 'content'.
    - base_model (Pydantic model, optional): Model for validating structured responses.

    Returns:
    - dict or str: Validated response or raw response content.
    """
    try:
        client = OpenAI()
        max_tries = int(os.getenv("MAX_TRIES_STRUCTURED_OUTPUT"))
        gpt_model = os.getenv("CHATGPT_MODEL", "gpt-4")
        temperature = float(os.getenv("MODEL_TEMPERATURE"))
        tools = [openai.pydantic_function_tool(base_model)] if base_model else []
        bool_iso_model = bool(base_model and issubclass(base_model, (
            NoInfoModel, TableModel, ClauseModel, ClauseSummaryModel,
            IdentifyExternalIdsModel, IdentifyTablesModel, IdentifyClausesModel,
            IdentifyInformationModel)))

        if bool_iso_model:
            tools.append(openai.pydantic_function_tool(NoInfoModel))

        # Validate messages format
        for message in messages:
            if not all(k in message for k in ('role', 'content')):
                raise ValueError("Each message must have 'role' and 'content'.")

        # Add initial system message
        messages.insert(0, {"role": "system", "content": prompt_system_role()})

        # First attempt (outside retry loop)
        chat = client.chat.completions.create(
            messages=messages,
            model=gpt_model,
            temperature=temperature,
            tools=tools if base_model else None
        )
        result = process_response(chat, messages, base_model, bool_iso_model)
        if result:
            return result

        # Retry mechanism for structured responses
        if base_model:
            # Add guidance for structured format after first failure
            guidance_message = (
                "Please ensure the response **follows the structured outcome format** defined "
                "earlier. Use the provided schema and correct any deviations in format or "
                "content.\n"
                f"The expected outcome structure is:\n{base_model.model_json_schema()}\n"
            )
            if bool_iso_model:
                guidance_message += (
                    "\nHowever if no information is found, return the function: "
                    "NoInfoModel with 'no_information' set to true."
                )
            if chat.choices[0].message.content:
                guidance_message += (
                    f"\nYou generated this before:\n{chat.choices[0].message.content}"
                )
            messages.append({"role": "system", "content": guidance_message})

            for attempt in range(max_tries):
                print(f"Retry attempt {attempt + 1}...")
                chat = client.chat.completions.create(
                    messages=messages,
                    model=gpt_model,
                    temperature=temperature,
                    tools=tools if base_model else None
                )
                result = process_response(chat, messages, base_model, bool_iso_model)
                if result:
                    return result

            # Raise exception if no valid response after retries
            raise ValueError("No structured response provided after multiple attempts.")

        # If base_model is not provided, return raw content
        return chat.choices[0].message.content if chat.choices else None

    except (OpenAIError, ValueError, TypeError) as e:
        print("Error during send_prompt execution:")
        print(f"Exception: {e}")
        raise
