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
            "**Correctness**: Does each checklist question accurately reflect the content or intent "
            "of the corresponding requirement, even if it captures only part of it? Provide a qualification "
            "(1 to 3, where 3 is the best) and include a note explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    elif rubric == "redundancy":
        prompt += (
            "**Redundancy**: Provide a qualification (1 to 3, where 3 is the best) indicating if "
            "each checklist question is free of any additional criteria not directly derived from its associated "
            "requirement(s), avoiding unnecessary or extraneous information. Include a note explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    elif rubric == "applicability":
        prompt += (
            "**Applicability**: Are the checklist questions formulated so that they can be answered solely by analyzing "
            "the work product—with terminology that is both accurate to the domain standards and simplified for "
            "accessibility to non-experts? Provide a qualification (1 to 3, where 3 is the best) and include a note "
            "explaining the reasoning.\n\n"
            "Return your evaluation using the format from the `RubricEvaluationModel` to structure "
        )
    elif rubric == "traceability":
        prompt += (
            "**Traceability**: Does every checklist question clearly reference at least one underlying "
            "requirement, ensuring a transparent link between the evaluation item and its source? Provide a qualification "
            "(1 to 3, where 3 is the best) and include a note explaining the reasoning.\n\n"
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
            "**Applicability**: Is the granularity of the checklist such that it is usable in practice? "
            "If all the questions are answered 'yes,' does that indicate that the requirement is fulfilled? "
            "Rate this aspect (1 to 3, where 3 is the best). Provide a note explaining the reasoning.\n\n"
            "Use the format from the `EvaluationChecklistModel` to structure your response, including "
            "ratings and detailed notes for each criterion.\n"
        )
    elif rubric == "consistency":
        prompt += (
            "**Consistency**: Across the entire checklist, do the questions maintain a coherent framework, "
            "ensuring that no contradictions exist between topics? Rate this aspect (1 to 3, where 3 is the best). "
            "Provide a note explaining the reasoning.\n\n"
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
            "**Traceability**: Is each requirement explicitly linked to at least one checklist question? "
            "Rate this aspect (1 to 3, where 3 is the best). Provide a note explaining the reasoning.\n"
        )
    elif rubric == "completeness":
        prompt += (
            "**Completeness**: Do the checklist questions fully capture the essential information of each requirement? "
            "Rate this aspect (1 to 3, where 3 is the best). Provide a note explaining the reasoning.\n"
        )
    else:
        raise ValueError("Invalid rubric provided.")

    prompt += (
        "Use the format from the `EvaluationRequirementModel` to structure your response, including "
        "ratings and detailed notes for each criterion.\n"
    )
    return prompt
