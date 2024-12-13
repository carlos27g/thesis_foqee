"""
This module provides functionality to generate an Excel file from a ChecklistModel
and save it in a specified directory.

Functions:
    generate_excel_from_checklist_v3(checklist: ChecklistModel) -> Path:
"""

from pathlib import Path
import pandas as pd
from llm_services.base_models import ChecklistModel


def generate_excel_from_checklist(checklist: ChecklistModel):
    """
    Generates an Excel file from a ChecklistModel and saves it in the 'checklist_excel' folder
    in the current directory.

    Args:
        checklist (ChecklistModel): The checklist model to be converted into an Excel file.

    Returns:
        Path: The path to the saved Excel file.
    """
    # Create the folder for all checklist Excel files in the current directory
    output_folder = Path.cwd() / "checklist_excel"
    output_folder.mkdir(exist_ok=True)

    # Prepare data for the Excel file
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

    # Create a DataFrame and save it to an Excel file
    df = pd.DataFrame(data)
    excel_file_path = output_folder / f"{checklist.work_product}.xlsx"
    df.to_excel(excel_file_path, index=False)