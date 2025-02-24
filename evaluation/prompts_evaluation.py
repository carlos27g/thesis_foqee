"""
This script contains the methods to build the prompts used in testing the 
evaluation frameworks.

Function:
    prompt_evaluation_question_level:
        Evaluates the checklist at the question level.
    prompt_evaluation_checklist_level:
        Evaluates the checklist at the checklist level.
    prompt_evaluation_requirements_level:
        Evaluates the checklist at the requirements level.
"""

import pandas as pd

def prompt_evaluation_question_level(work_product: str, topic: str, questions: str,
                                     requirements: pd.DataFrame, rubric: str) -> str:
    """
    Generates a prompt to evaluate a question based on predefined metrics.

    Parameters:
        work_product (str): The name or description of the work product.
        topic (str): The topic related to the generated question.
        questions (str): The question being evaluated.
        requirements (pd.DataFrame): A DataFrame with columns 'ID' and 'Description' containing 
        requirement IDs and their descriptions.

    Returns:
        str: The generated prompt.
    """
    requirements_list = "\n".join(
        [f"- {row['ID']}: {row['Description']}" for _, row in requirements.iterrows()]
    )

    prompt = (
        f"In the context of the work product '{work_product}' in ISO26262 and Automotive Spice "
        f"Frameworks, we are evaluating the following question(s):\n"
        f"\n    '{questions}'\n"
        f"\nThis question was generated in relation to the topic '{topic}' using the following "
        f"requirements:\n"
        f"{requirements_list}\n\n"
        "Please evaluate the question(s) based on the following criteria:\n\n"
    )
    if rubric == "correctness":
        prompt += (
            "**Correctness**: Provide a qualification (1 to 3, where 3 is the best) indicating if "
            "the question captures at least part of the information from the requirements it traces to. "
            "Include a note explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    elif rubric == "redundancy":
        prompt += (
            "**Redundancy**: Provide a qualification (1 to 3, where 3 is the best) indicating if "
            "the question is free of unnecessary or unrelated criteria. Include a note explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    elif rubric == "applicability":
        prompt += (
            "**Applicability**: Provide a qualification (1 to 3, where 3 is the best) indicating if "
            "the question can be answered by referencing only the work product. Include a note explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    elif rubric == "traceability":
        prompt += (
            "**Traceability**: Provide a qualification (1 to 3, where 3 is the best) indicating if "
            "the question is traced to at least one requirement. Include a note explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    else:
        raise ValueError("Invalid rubric provided.")
    return prompt


def prompt_evaluation_checklist_level(checklist: pd.DataFrame, rubric: str) -> str:
    """
    Generates a prompt to evaluate a checklist at the checklist level.

    Parameters:
        checklist (pd.DataFrame): The checklist items to be evaluated.
        rubric (str): The rubric to be used for evaluation.

    Returns:
        str: The generated prompt.
    """
    prompt = (
        "In the context of the ISO26262 and Automotive Spice Frameworks, we are evaluating the "
        "checklist at the checklist level.\n\n"
        "The checklist to be evaluated is as follows:\n"
        f"{checklist.to_string()}\n\n"
        "Please evaluate the checklist based on the following criteria:\n\n"
    )

    if rubric == "applicability":
        prompt += (
            "**Applicability**: Rate the checklist's granularity and practical usability (1 to 3, "
            "where 3 is the best). Provide a note explaining the reasoning.\n\n"
            "Use the format from the `EvaluationChecklistModel` to structure your response, including "
            "ratings and detailed notes for each criterion.\n"
        )
    elif rubric == "consistency":
        prompt += (
            "**Consistency**: Rate whether the checklist items are free from contradictions (1 to 3, "
            "where 3 is the best). Provide a note explaining the reasoning.\n\n"
            "Use the format from the `EvaluationChecklistModel` to structure your response, including "
            "ratings and detailed notes for each criterion.\n"
        )
    else:
        raise ValueError("Invalid rubric provided.")
    
    return prompt


def prompt_evaluation_requirements_level(work_product: str, requirement_id: str, description: str,
                                         checklist_items: list[tuple[str, str, str]], rubric: str) -> str:
    """
    Generates a prompt to evaluate a requirement at the requirements level.

    Parameters:
        work_product (str): The name or description of the work product.
        requirement_id (str): The ID of the requirement.
        description (str): A brief description of the requirement.
        checklist_items (list[tuple[str, str, str]]): A list of tuples containing title, questions, 
                                                      and requirement IDs for the checklist items.
        rubric (str): The rubric to be used for evaluation.

    Returns:
        str: The generated prompt.
    """
    prompt = (
        "In the context of the ISO26262 and Automotive Spice Frameworks, we are evaluating the "
        "checklist at the requirements level.\n\n"
        "The requirement to be evaluated is as follows:\n"
        f"Work Product: {work_product}\n"
        f"Requirement ID: {requirement_id}\n"
        f"Description: {description}\n\n"
        "Checklist Items:\n"
    )

    for title, questions, req_ids in checklist_items:
        prompt += (
            f"Title: {title}\n"
            f"Questions: {questions}\n"
            f"Requirement IDs: {req_ids}\n\n"
        )

    prompt += "Please evaluate the checklist based on the following criteria:\n\n"

    if rubric == "traceability":
        prompt += (
            "**Traceability**: Rate whether the requirement is traced to at least one checklist "
            "question (1 to 3, where 3 is the best). Provide a note explaining the reasoning.\n"
        )
    elif rubric == "completeness":
        prompt += (
            "**Completeness**: Assess whether the information in the checklist items adequately "
            "captures the relevant details of the requirement (1 to 3, where 3 is the best). Provide a "
            "note explaining the reasoning.\n"
        )
    else:
        raise ValueError("Invalid rubric provided.")

    prompt += (
        "Use the format from the `EvaluationRequirementModel` to structure your response, including "
        "ratings and detailed notes for each criterion.\n"
    )
    return prompt
