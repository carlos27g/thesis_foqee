"""
This script evaluates the results of checklists using different metrics. The evaluations are 
performed by language models (LLMs) which also provide notes to support their understanding.

Methods:
- evaluate_checklists: Controls which evaluation to perform.
- evaluate_question_level: Analyzes the checklist at the question level.
- evaluate_checklist_level: Analyzes the checklist at the checklist level.
- evaluate_requirements_level: Analyzes the checklist at the requirements level.
"""

import os
import pandas as pd
from termcolor import colored

from evaluation.evaluation_models import (
    RubricChecklistModel, RubricQuestionModel, RubricRequirementModel
)
from evaluation.prompts_evaluation import (
    prompt_evaluation_question_level, prompt_evaluation_checklist_level,
    prompt_evaluation_requirements_level)

from llm_services.send_prompt import send_prompt


def save_evaluation_to_excel(df: pd.DataFrame, output_folder: str, file_name: str):
    """
    Saves the evaluation results DataFrame to an Excel file.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing evaluation results.
    - output_folder (str): The folder where the Excel file will be saved.
    - file_name (str): The name of the Excel file.
    """
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    output_file_path = os.path.join(output_folder, f"evaluated_{file_name}")
    df.to_excel(output_file_path, index=False)
    print(f"Evaluation results saved to {output_file_path}")


def evaluate_checklist():
    """
    Evaluates the checklists based on the EVALUATION_TYPE environment variable.

    This function checks the type of evaluation and calls the appropriate 
    evaluation function.
    """
    # Code omitted for brevity...

def evaluate_question_level(requirements: pd.DataFrame):
    """
    Analyzes the checklist at the question level.
    """
    evaluation = False
    question_level_folder = os.path.join("checklist_excel", "question_level")

    for file_name in os.listdir(question_level_folder):
        if file_name.endswith(".xlsx"):
            evaluation = True
            file_path = os.path.join(question_level_folder, file_name)
            df_questions = pd.read_excel(file_path)
            print(colored(f"Evaluating {file_name} at question level", "green"))

            # Adding new columns to the DataFrame
            columns_to_add = [
                "Traceability", "Traceability Notes",
                "Correctness", "Correctness Notes",
                "Redundancy", "Redundancy Notes",
                "Applicability", "Applicability Notes"
            ]
            for column in columns_to_add:
                df_questions[column] = ""

            for index, row in df_questions.iterrows():
                print(f"- Evaluating topic: {row['Topic']}")
                ids_list = row["IDs"].split("\n")
                matching_requirements = requirements[requirements['ID'].isin(ids_list)]
                matching_requirements = matching_requirements[['ID', 'Description']]
                work_product = row["Work Product"]
                topic = row["Topic"]
                questions = row["Questions"]
                rubrics = ["traceability", "correctness", "redundancy", "applicability"]
                evaluation_answ = {}
                for rubric in rubrics:
                    prompt = prompt_evaluation_question_level(
                        work_product, topic, questions, matching_requirements, rubric
                    )
                    message = [{"role": "user", "content": prompt}]
                    evaluation_answ[rubric] = send_prompt(message, RubricQuestionModel)

                # Update DataFrame with evaluation results using the dictionary
                df_questions.at[index, "Traceability"] = \
                    evaluation_answ["traceability"].score
                df_questions.at[index, "Traceability Notes"] = \
                    evaluation_answ["traceability"].notes
                df_questions.at[index, "Correctness"] = \
                    evaluation_answ["correctness"].score
                df_questions.at[index, "Correctness Notes"] = \
                    evaluation_answ["correctness"].notes
                df_questions.at[index, "Redundancy"] = \
                    evaluation_answ["redundancy"].score
                df_questions.at[index, "Redundancy Notes"] = \
                    evaluation_answ["redundancy"].notes
                df_questions.at[index, "Applicability"] = \
                    evaluation_answ["applicability"].score
                df_questions.at[index, "Applicability Notes"] = \
                    evaluation_answ["applicability"].notes

            save_evaluation_to_excel(df_questions, "checklist_auto_evaluation/question_level",
                                     file_name)

    if not evaluation:
        print("No files found for evaluation at question level, file is empty.")


def evaluate_checklist_level():
    """
    Analyzes the checklist at the checklist level.
    """
    evaluation = False
    question_level_folder = os.path.join("checklist_excel", "question_level")

    for file_name in os.listdir(question_level_folder):
        if file_name.endswith(".xlsx"):
            evaluation = True
            file_path = os.path.join(question_level_folder, file_name)
            df_questions = pd.read_excel(file_path)
            columns_to_add = [
                "Applicability", "Applicability Notes",
                "Consistency", "Consistency Notes"
            ]
            for column in columns_to_add:
                df_questions[column] = ""
            print(colored(f"Evaluating {file_name} at question level", "green"))

            rubrics = ["applicability", "consistency"]
            evaluation_answ = {}
            for rubric in rubrics:
                prompt = prompt_evaluation_checklist_level(df_questions, rubric)
                message = [{"role": "user", "content": prompt}]
                evaluation_answ[rubric] = send_prompt(message, RubricChecklistModel)

            # Update DataFrame with evaluation results using the dictionary
            df_questions.at[1, "Applicability"] = evaluation_answ["applicability"].score
            df_questions.at[1, "Applicability Notes"] = evaluation_answ["applicability"].notes
            df_questions.at[1, "Consistency"] = evaluation_answ["consistency"].score
            df_questions.at[1, "Consistency Notes"] = evaluation_answ["consistency"].notes

            save_evaluation_to_excel(df_questions, "checklist_auto_evaluation/checklist_level",
                                     file_name)

    if not evaluation:
        print("No files found for evaluation at question level, file is empty.")


def evaluate_requirements_level():
    """
    Analyzes the checklist at the requirements level.
    """
    evaluation = False
    question_level_folder = os.path.join("checklist_excel", "requirement_level")

    for file_name in os.listdir(question_level_folder):
        if file_name.endswith(".xlsx"):
            evaluation = True
            file_path = os.path.join(question_level_folder, file_name)
            df_requirements = pd.read_excel(file_path)
            print(colored(f"Evaluating {file_name} at question level", "green"))

            columns_to_add = [
                "Traceability", "Traceability Notes",
                "Completeness", "Completeness Notes"
            ]
            for column in columns_to_add:
                df_requirements[column] = ""

            grouped_requirements = df_requirements.groupby(["Work Product", "ID", "Description"])

            for name, group in grouped_requirements:
                work_product = name[0]
                requirement_id = name[1]
                description = name[2]
                print(f"- Evaluating requirement ID: {requirement_id}")
                checklist_items = group[["Title", "Questions", "List_Ids"]].values.tolist()

                rubrics = ["traceability", "completeness"]
                evaluation_answ = {}
                for rubric in rubrics:
                    prompt = prompt_evaluation_requirements_level(work_product, requirement_id,
                                                                  description, checklist_items,
                                                                  rubric)
                    message = [{"role": "user", "content": prompt}]
                    evaluation_answ[rubric] = send_prompt(message, RubricRequirementModel)

                # Update DataFrame with evaluation results using the dictionary
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Traceability"] = evaluation_answ["traceability"].score
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Traceability Notes"] = evaluation_answ["traceability"].notes
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Completeness"] = evaluation_answ["completeness"].score
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Completeness Notes"] = evaluation_answ["completeness"].notes

            save_evaluation_to_excel(df_requirements,
                                     "checklist_auto_evaluation/requirements_level",
                                     file_name)

    if not evaluation:
        print("No files found for evaluation at question level, file is empty.")


if __name__ == "__main__":
    evaluate_checklist()
