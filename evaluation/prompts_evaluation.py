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
                                     requirements: pd.DataFrame) -> str:
    """
    Generates a prompt to evaluate a question based on predefined metrics.
    Parameters:
        work_product (str): The name or description of the work product.
        topic (str): The topic related to the generated question.
        question (str): The question being evaluated.
        requirements (pd.DataFrame): A DataFrame with columns 'ID' and 'Description' containing 
        requirement IDs and their descriptions.
    """
    requirements_list = "\n".join([f"- {row['ID']}: {row['Description']}" for _, row in requirements.iterrows()])

    prompt = (
        f"In the context of the work product '{work_product}' in ISO26262 and Automotive Spice "
        f"Frameworks, we are evaluating the questions:\n"
        f"\n    '{questions}'\n"
        f"\nThis question was generated in relation to the topic '{topic}' using the following "
        f"requirements:\n"
        f"{requirements_list}\n\n"
        "Please evaluate the question based on the following metrics:\n\n"
        "1. Traceability: Provide a qualification between 1 and 3 (3 being the best) indicating "
        "if each question is traced to at least one requirement. Provide a note explaining the "
        "qualification.\n"
        "2. Correctness: Provide a qualification between 1 and 3 (3 being the best) indicating if "
        "the question captures at least part of the information from the requirements it traces "
        "to. Provide a note explaining the qualification.\n"
        "3. Redundancy: Provide a qualification between 1 and 3 (3 being the best) indicating if "
        "the question is free of criteria that are not derived from any traced requirement. "
        "Provide a note explaining the qualification.\n"
        "4. Applicability: Provide a qualification between 1 and 3 (3 being the best) indicating "
        "if the question can be answered by looking just at the work product. Provide a note "
        "explaining the qualification.\n\n"
        "Your response should include integer values for the metrics and detailed notes for each "
        "qualification.\n"
    )

    prompt += "\nUse the format from the EvaluationQuestionModel to provide your response.\n"
    return prompt


def prompt_evaluation_checklist_level(checklist: pd.DataFrame) -> str:
    """
    Write a function that evaluates the checklist at the checklist level.
    """
    prompt = (
        "In the context of the ISO26262 and Automotive Spice Frameworks, we are evaluating the "
        "checklist at the checklist level.\n"
        "Please evaluate the checklist based on the following metrics:\n\n"
        "1. Applicability: is the granularity of the checklist such that it is usable in practice? (Rate from 1 to 3, where 3 is the best)\n"        
        "2. Consistency: are the checklist items free from contradictions? (Rate from 1 to 3, where 3 is the best)\n"
    )

    prompt += (
        "The checklist to be evaluated is as follows:\n"
        f"{checklist.to_string()}\n\n"
    )

    prompt += "\nUse the format from the EvaluationQuestionModel to provide your response.\n"
    return prompt


def prompt_evaluation_requirements_level(work_product: str, requirement_id: str, description: str,
                                         checklist_items: list[str, str, str]) -> str:
    """
    Write a function that evaluates the checklist at the requirements level.
    """
    prompt = (
        "In the context of the ISO26262 and Automotive Spice Frameworks, we are evaluating the "
        "checklist at the requirements level.\n"
        "Please evaluate the checklist based on the following metrics:\n\n"
        "1. Traceability: is each requirement traced to at least one question? (Rate from 1 to "
        "3, where 3 is the best)\n"
        "2. Completeness: assess if the information in the different checklist items is enough to "
        "capture the relevant information of the requirement. The checklist items may contain "
        "information from other requirements, but focus only on whether the requirement's "
        "information is adequately captured. (Rate from 1 to 3, where 3 is the best)\n"
    )

    prompt += (
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

    prompt += "\nUse the format from the EvaluationRequirementModel to provide your response.\n"
    return prompt
