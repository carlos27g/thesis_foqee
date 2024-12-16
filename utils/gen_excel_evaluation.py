"""
This module provides functionality to generate Excel sheets for evaluating checklists.
Each checklist will be saved in the 'checklist_excel' folder in the current directory.
"""

import os

from pathlib import Path
import pandas as pd
from llm_services.models_checklist import ChecklistModel


def create_excel_evaluation_sheet(checklist: ChecklistModel, requirements: pd.DataFrame):
    """
    Args:
        checklist (ChecklistModel): The checklist model to be converted into an Excel file.
        requirements (pd.DataFrame): DataFrame containing the requirements.
            Must have columns: 'Work Product', 'ID', 'Description'.
    Returns:
        None
    """
    gen_evaluation_requirements_level(requirements, checklist)
    generate_checklist_excel(checklist)


def generate_checklist_excel(checklist: ChecklistModel):
    """
    Generates an Excel file from a ChecklistModel and saves it in the 'checklist_excel' folder
    in the current directory.

    Args:
        checklist (ChecklistModel): The checklist model to be converted into an Excel file.

    Returns:
        Path: The path to the saved Excel file.
    """
    output_folder = Path(os.path.join(os.getcwd(), "checklist_excel", "question_level"))
    output_folder.mkdir(exist_ok=True)

    data = {
        "Work Product": [],
        "Topic": [],
        "Checklist Item": [],
    }

    for item in checklist.checklist_items:
        data["Work Product"].append(checklist.work_product)
        data["Topic"].append(item.title)
        questions = "\n".join([f"{i + 1}. {q}" for i, q in enumerate(item.description)])
        ids = "\n".join(item.ids)
        checklist_item_content = f"**Questions:**\n{questions}\n\n**IDs:**\n{ids}"
        data["Checklist Item"].append(checklist_item_content)

    df = pd.DataFrame(data)
    excel_file_path = output_folder / f"{checklist.work_product}_checklist.xlsx"
    df.to_excel(excel_file_path, index=False)
    print(f"Excel file for checklist questions saved to: {excel_file_path}")


def gen_evaluation_requirements_level(requirements: pd.DataFrame,
                                      checklist: ChecklistModel):
    """
    Generates an Excel file with a left merge of the requirements and checklist items.

    Args:
        requirements (pd.DataFrame): DataFrame containing the requirements.
            Must have columns: 'Work Product', 'Id', 'Description'.
        checklist (ChecklistModel): ChecklistModel containing checklist items.
        output_path (str): Path where the Excel file will be saved.

    Returns:
        None
    """
    output_folder = Path(os.path.join(os.getcwd(), "checklist_excel", "requirements_level"))
    output_folder.mkdir(exist_ok=True)

    checklist_data = []
    for item in checklist.checklist_items:
        for checklist_id in item.ids:
            checklist_data.append({
                "Checklist ID": checklist_id,
                "Title": item.title,
                "Questions": "; ".join(item.description),
                "List_Ids": item.ids
            })

    print(len(checklist_data))

    checklist_df = pd.DataFrame(checklist_data)

    merged_df = pd.merge(
        requirements,
        checklist_df,
        how="left",
        left_on="ID",
        right_on="Checklist ID"
    )

    merged_df = merged_df.drop(
        columns=["Checklist ID", "Version", "Part", "Clause", "Standard Name",
                 "Section", "Subsection", "Subsubsection"])

    excel_file_path = output_folder / f"{checklist.work_product}_requirements.xlsx"
    merged_df.to_excel(excel_file_path, index=False)
    print(f"Excel file with requirements level saved to: {excel_file_path}")
