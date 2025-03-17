"""
This script evaluates the results of checklists using different metrics. The evaluations are 
performed  by language models (LLMs) which also provide notes to support their understanding.

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
    RubricQuestionModel, RubricChecklistModel, RubricRequirementModel)
from evaluation.prompts_evaluation import (
    prompt_evaluation_question_level, prompt_evaluation_checklist_level,
    prompt_evaluation_requirements_level)

from llm_services.send_prompt import send_prompt


def evaluate_checklist():
    """
    Evaluates the checklists based on the EVALUATION_TYPE environment variable.

    This function checks the type of evaluation and calls the appropriate 
    evaluation function.
    """

    # Check if the required folders and files exist
    if not os.path.exists(os.path.join(os.getcwd(), "datasets", "combined_data.csv")):
        raise FileNotFoundError("The file 'combined_data.csv' was not "
                                "found in the 'dataset' folder.")

    if not os.path.exists(os.path.join(os.getcwd(), "checklist_excel", "question_level")):
        raise FileNotFoundError("The folder 'question_level' was not "
                                "found inside 'checklist_excel'.")

    if not os.path.exists(os.path.join(os.getcwd(), "checklist_excel", "requirement_level")):
        raise FileNotFoundError("The folder 'requirements_level' was not "
                                "found inside 'checklist_excel'.")

    # Load combined data into a DataFrame
    combined_data_path = os.path.join(os.getcwd(), "datasets", "combined_data.csv")
    requirements = pd.read_csv(combined_data_path)

    if os.getenv("EVALUATE_QUESTION_LEVEL") == "true":
        print(colored("Starting question level evaluation...", "blue"))
        evaluate_question_level(requirements)

    if os.getenv("EVALUATE_CHECKLIST_LEVEL") == "true":
        print(colored("Starting checklist level evaluation...", "blue"))
        evaluate_checklist_level()

    if os.getenv("EVALUATE_REQUIREMENTS_LEVEL") == "true":
        print(colored("Starting requirements level evaluation...", "blue"))
        evaluate_requirements_level()


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
                "Traceability", "Traceability Notes", "Correctness", "Correctness Notes",
                "Redundancy", "Redundancy Notes", "Applicability", "Applicability Notes"
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
                ans_dict = {}
                for rubric in rubrics:
                    prompt = prompt_evaluation_question_level(work_product, topic, questions,
                                                              matching_requirements, rubric)
                    message = [{"role": "user", "content": prompt}]
                    ans_dict[rubric] = send_prompt(message, RubricQuestionModel)

                # Update DataFrame with evaluation results
                df_questions.at[index, "Traceability"] = ans_dict["traceability"].score
                df_questions.at[index, "traceability Notes"] = ans_dict["traceability"].notes
                df_questions.at[index, "Correctness"] = ans_dict["correctness"].score
                df_questions.at[index, "Correctness Notes"] = ans_dict["correctness"].notes
                df_questions.at[index, "Redundancy"] = ans_dict["redundancy"].score
                df_questions.at[index, "Redundancy Notes"] = ans_dict["redundancy"].notes
                df_questions.at[index, "Applicability"] = ans_dict["applicability"].score
                df_questions.at[index, "Applicability Notes"] = ans_dict["applicability"].notes

            output_folder = os.path.join("checklist_auto_evaluation", "question_level")
            os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
            output_file_path = os.path.join(output_folder, f"evaluated_{file_name}")
            df_questions.to_excel(output_file_path, index=False)
            print(f"Evaluation results saved to {output_file_path}")

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
            df_questions = pd.read_excel(file_path, engine='openpyxl')
            print(colored(f"Evaluating {file_name} at question level", "green"))
            columns_to_add = [
                "Applicability", "Applicability Notes", "Consistency", "Consistency Notes"
            ]
            for column in columns_to_add:
                df_questions[column] = ""
            rubrics = ["applicability", "consistency"]
            ans_dict = {}
            for rubric in rubrics:
                prompt = prompt_evaluation_checklist_level(df_questions, rubric)
                message = [{"role": "user", "content": prompt}]
                ans_dict[rubric] = send_prompt(message, RubricChecklistModel)

            df_questions["Applicability"] = ans_dict["applicability"].score
            df_questions["Applicability Notes"] = ans_dict["applicability"].notes
            df_questions["Consistency"] = ans_dict["consistency"].score
            df_questions["Consistency Notes"] = ans_dict["consistency"].notes

            output_folder = os.path.join("checklist_auto_evaluation", "checklist_level")
            os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
            output_file_path = os.path.join(output_folder, f"evaluated_{file_name}")
            df_questions.to_excel(output_file_path, index=False)
            print(f"Evaluation results saved to {output_file_path}")

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
            df_requirements = pd.read_excel(file_path, engine='openpyxl')
            print(colored(f"Evaluating {file_name} at question level", "green"))

            columns_to_add = [
                "Traceability", "Traceability Notes", "Completeness", "Completeness Notes"
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
                ans_dict = {}
                for rubric in rubrics:
                    prompt = prompt_evaluation_requirements_level(work_product, requirement_id,
                                                                    description, checklist_items,
                                                                    rubric)
                    message = [{"role": "user", "content": prompt}]
                    ans_dict[rubric] = send_prompt(message, RubricRequirementModel)

                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Traceability"] = ans_dict["traceability"].score
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Traceability Notes"] = ans_dict["traceability"].notes
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Completeness"] = ans_dict["completeness"].score
                df_requirements.loc[df_requirements["ID"] == requirement_id,
                                    "Completeness Notes"] = ans_dict["completeness"].notes

            output_folder = os.path.join("checklist_auto_evaluation", "requirements_level")
            os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
            output_file_path = os.path.join(output_folder, f"evaluated_{file_name}")
            df_requirements.to_excel(output_file_path, index=False)
            print(f"Evaluation results saved to {output_file_path}")

    if not evaluation:
        print("No files found for evaluation at question level, file is empty.")

if __name__ == "__main__":
    evaluate_checklist()
