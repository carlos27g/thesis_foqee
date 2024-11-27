import os
import openai
from openai import OpenAI
from llm_services.prompts import prompt_system_role
from utils.messages import add_message

def validate_response_with_model(response_content, base_model):
    """
    Validate the response content using the provided base_model.
    Returns the validated response if successful, otherwise returns None.
    """
    try:
        return base_model.model_validate_json(response_content)
    except Exception:
        print("The LLM did not return the expected structured outcome, retrying...")
        return None

def send_prompt(messages, base_model=None):
    """
    Send a query to ChatGPT using the OpenAI API and optionally validate responses with a Pydantic model.
    """
    try:
        client = OpenAI()
        tools = [openai.pydantic_function_tool(base_model)] if base_model else []
        max_tries = int(os.getenv("MAX_TRIES_STRUCTURED_OUTPUT", 3))
        gpt_model= os.getenv("CHATGPT_MODEL")
        temperature = float(os.getenv("MODEL_TEMPERATURE"))

        # Validate messages
        for message in messages:
            if not isinstance(message, dict) or 'role' not in message or 'content' not in message:
                raise ValueError("Each message must be a dictionary containing 'role' and 'content' attributes.")

        # Initial messages
        messages.insert(0, {"role": "system", "content": prompt_system_role()})

        # First attempt (outside the loop)
        chat = client.chat.completions.create(
            messages=messages,
            model=gpt_model,
            temperature=temperature,
            tools=tools if base_model else None
        )

        response = chat.choices[0].message
        tool_calls = getattr(response, 'tool_calls', None)

        if base_model:
            # Check for tool calls and validate the response
            if tool_calls and len(tool_calls) > 0:
                tool_response = tool_calls[0].function.arguments
                validated_response = validate_response_with_model(tool_response, base_model)
                if validated_response:
                    for message in messages:
                        add_message(message['role'], message['content'], base_model)
                    add_message("system", validated_response, base_model)
                    return validated_response

            # Add guidance message if first attempt fails
            guidance_message = (
                "Please ensure the response **follows the structured outcome format** defined earlier. "
                "Use the information already provided and correct any deviations in the format and content.\n"
                "The expected outcome structure is:\n"
                f"{base_model.schema()}"
            )
            messages.append({"role": "system", "content": guidance_message})

        # Retry loop (starts after guidance message is added)
        for _ in range(max_tries):
            chat = client.chat.completions.create(
                messages=messages,
                model=gpt_model,
                temperature=temperature,
                tools=tools if base_model else None
            )

            response = chat.choices[0].message
            tool_calls = getattr(response, 'tool_calls', None)

            if base_model and tool_calls and len(tool_calls) > 0:
                tool_response = tool_calls[0].function.arguments
                validated_response = validate_response_with_model(tool_response, base_model)
                if validated_response:
                    for message in messages:
                        add_message(message['role'], message['content'], base_model)
                    add_message("system", validated_response, base_model)
                    return validated_response

        # If no valid structured response after retries, raise an error
        if base_model:
            raise Exception("No structured response provided after multiple attempts.")

        # If base_model is not provided, return the raw content
        if not base_model:
            if response.content:
                for message in messages:
                    add_message(message['role'], message['content'], base_model)
                add_message("system", validated_response, base_model)
                return response.content

    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return str(e)
