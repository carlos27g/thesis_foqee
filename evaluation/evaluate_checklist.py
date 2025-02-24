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
            df_questions["Traceability"] = ""
            df_questions["Traceability Notes"] = ""
            df_questions["Correctness"] = ""
            df_questions["Correctness Notes"] = ""
            df_questions["Redundancy"] = ""
            df_questions["Redundancy Notes"] = ""
            df_questions["Applicability"] = ""
            df_questions["Applicability Notes"] = ""

            for index, row in df_questions.iterrows():
                print(f"- Evaluating topic: {row['Topic']}")
                ids_list = row["IDs"].split("\n")
                matching_requirements = requirements[requirements['ID'].isin(ids_list)]
                matching_requirements = matching_requirements[['ID', 'Description']]
                work_product = row["Work Product"]
                topic = row["Topic"]
                questions = row["Questions"]
                # Evaluate traceability
                prompt_traceability = prompt_evaluation_question_level(work_product, topic, questions,
                                                                        matching_requirements, "traceability")
                message = [{"role": "user", "content": prompt_traceability}]
                traceability_model = send_prompt(message, RubricQuestionModel)
                
                # Evaluate correctness
                prompt_correctness = prompt_evaluation_question_level(work_product, topic, questions,
                                                                        matching_requirements, "correctness")
                message = [{"role": "user", "content": prompt_correctness}]
                correcctness_model = send_prompt(message, RubricQuestionModel)
                
                # Evaluate redundancy
                prompt_redundancy = prompt_evaluation_question_level(work_product, topic, questions,
                                                                    matching_requirements, "redundancy")
                message = [{"role": "user", "content": prompt_redundancy}]
                redundancy_model = send_prompt(message, RubricQuestionModel)

                # Evaluate applicability
                prompt_applicability = prompt_evaluation_question_level(work_product, topic, questions,
                                                                        matching_requirements, "applicability")
                message = [{"role": "user", "content": prompt_applicability}]
                applicability_model = send_prompt(message, RubricQuestionModel)

                # Update DataFrame with evaluation results
                df_questions.at[index, "Traceability"] = traceability_model.score
                df_questions.at[index, "Traceability Notes"] = traceability_model.notes
                df_questions.at[index, "Correctness"] = correcctness_model.score
                df_questions.at[index, "Correctness Notes"] = correcctness_model.notes
                df_questions.at[index, "Redundancy"] = redundancy_model.score
                df_questions.at[index, "Redundancy Notes"] = redundancy_model.notes
                df_questions.at[index, "Applicability"] = applicability_model.score
                df_questions.at[index, "Applicability Notes"] = applicability_model.notes

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
            df_questions = pd.read_excel(file_path)
            df_questions["Applicability"] = ""
            df_questions["Applicability Notes"] = ""
            df_questions["Consistency"] = ""
            df_questions["Consistency Notes"] = ""

            print(colored(f"Evaluating {file_name} at question level", "green"))
            # Evaluate traceability
            prompt = prompt_evaluation_checklist_level(df_questions, "applicability")
            message = [{"role": "user", "content": prompt}]
            traceability_model = send_prompt(message, RubricChecklistModel)

            # Evaluate correctness
            prompt = prompt_evaluation_checklist_level(df_questions, "consistency")
            message = [{"role": "user", "content": prompt}]
            correctness_model = send_prompt(message, RubricChecklistModel)

            df_questions[1, "Applicability"] = traceability_model.score
            df_questions[1, "Applicability Notes"] = traceability_model.notes
            df_questions[1, "Consistency"] = correctness_model.score
            df_questions[1, "Consistency Notes"] = correctness_model.notes

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
            df_requirements = pd.read_excel(file_path)
            print(colored(f"Evaluating {file_name} at question level", "green"))

            df_requirements["Traceability"] = ""
            df_requirements["Traceability Notes"] = ""
            df_requirements["Completeness"] = ""
            df_requirements["Completeness Notes"] = ""

            grouped_requirements = df_requirements.groupby(["Work Product", "ID", "Description"])

            for name, group in grouped_requirements:
                work_product = name[0]
                requirement_id = name[1]
                description = name[2]
                print(f"- Evaluating requirement ID: {requirement_id}")
                checklist_items = group[["Title", "Questions", "List_Ids"]].values.tolist()
                # Evaluate traceability
                prompt_traceability = prompt_evaluation_requirements_level(work_product, requirement_id,
                                                                            description, checklist_items, "traceability")
                message = [{"role": "user", "content": prompt_traceability}]
                traceability_model = send_prompt(message, RubricRequirementModel)

                # Evaluate completeness
                prompt_completeness = prompt_evaluation_requirements_level(work_product, requirement_id,
                                                                         description, checklist_items, "completeness")
                message = [{"role": "user", "content": prompt_completeness}]
                completeness_model = send_prompt(message, RubricRequirementModel)
                
                df_requirements.loc[df_requirements["ID"] == name, "Traceability"] = \
                    traceability_model.score
                df_requirements.loc[df_requirements["ID"] == name, "Traceability Notes"] = \
                    traceability_model.notes
                df_requirements.loc[df_requirements["ID"] == name, "Completeness"] = \
                    completeness_model.score
                df_requirements.loc[df_requirements["ID"] == name, "Completeness Notes"] = \
                    completeness_model.notes

            output_folder = os.path.join("checklist_auto_evaluation", "requirements_level")
            os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
            output_file_path = os.path.join(output_folder, f"evaluated_{file_name}")
            df_requirements.to_excel(output_file_path, index=False)
            print(f"Evaluation results saved to {output_file_path}")

    if not evaluation:
        print("No files found for evaluation at question level, file is empty.")

if __name__ == "__main__":
    evaluate_checklist()
