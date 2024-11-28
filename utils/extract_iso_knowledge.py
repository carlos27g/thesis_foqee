"""
This module provides functions to help in the extraction of ISO external knowledge during the 
content segmentation phase.
Functions:
    identify_table(requirement): Identifies table information for a given requirement.
    identify_clause(requirement): Identifies clause information for a given requirement.
    identify_external_id(requirement): Identifies external ID information for a given requirement.
    retrieve_table_knowledge(table_model: TableModel) -> str: 
        Retrieves the table from the ISO26262 standards.
    retrieve_clause_knowledge(clause_model: ClauseModel) -> str: 
        Retrieves the clause from the ISO26262 standards.
    retrieve_external_id_knowledge(external_id_model: RequirementIdModel) -> str: 
        Retrieves IDs from the ISO26262 standards.
"""

import os
import pandas as pd

from llm_services.models_content import (
    IdentifyTablesModel, IdentifyClausesModel, TableModel, ClauseModel,
    IdentifyExternalIdsModel, RequirementIdModel
)
from llm_services.prompts_content import (
    prompt_identify_external_id, prompt_identify_clause, prompt_identify_table,
    create_clause_summary_prompt
)
from llm_services.send_prompt import send_prompt

def identify_table(requirement):
    """
    Identifies the table based on the given ISO26262 requirement.
    Args:
        requirement (dict): The requirement from ISO for which the table needs to be identified.
    Returns:
        response (IdentifyTablesModel): The identified table information as a response.
        None: If no clause is identified.
    """
    prompt = prompt_identify_table(requirement)
    message = {"role": "user", "content": prompt}
    response = send_prompt([message], IdentifyTablesModel)
    return response


def identify_clause(requirement):
    """
    Identifies the clause from a given ISO26262 requirement.
    Args:
        requirement (dict): The requirement text from which the clause needs to be identified.
    Returns:
        response (IdentifyClausesModel): The identified clause from the requirement.
        None: If no clause is identified.
    """
    prompt = prompt_identify_clause(requirement)
    message = {"role": "user", "content": prompt}
    response = send_prompt([message], IdentifyClausesModel)
    return response


def identify_external_id(requirement):
    """
    Identifies the external ID for a given ISO26262 requirement.
    Args:
        requirement (str): The requirement for which the external ID needs to be identified.
    Returns:
        str: The identified external ID for the given requirement.
    """
    prompt = prompt_identify_external_id(requirement)
    message = {"role": "user", "content": prompt}
    response = send_prompt([message], IdentifyExternalIdsModel)
    return response


def retrieve_table_knowledge(table_model: TableModel) -> str:
    """
    Given a specific requirement ID, the function searches for extra knowledge in the table file.
    This knowledge is returned as a string to extend the prompt and context for the generation of
    checklists.
    """
    if table_model.standard_name == "ISO 26262":
        current_path = os.getcwd()
        table_file = os.path.join(current_path, "datasets", "26262-Tables.xlsx")
        table_df = pd.read_excel(table_file)
        table_df = table_df[
            (table_df['Part'] == table_model.part_number) &
            (table_df['Table'] == table_model.table_number)
        ]
        if table_df.empty:
            return None
        row_columns = ['Row', 'Method', 'ASIL A', 'ASIL B', 'ASIL C', 'ASIL D']
        table_information = ''
        grouped = table_df.groupby('Title')
        for title, group in grouped:
            table_information += f"Title: {title}\n"
            group = group.reset_index(drop=True)
            group_str = group[row_columns].to_string(index=False)
            table_information += group_str + '\n\n'
        return table_information
    return None


def retrieve_clause_knowledge(clause_model: ClauseModel) -> str:
    """
    Given a specific requirement ID, the function searches for extra knowledge in the clause file.
    This knowledge is returned as a string to extend the prompt and context for the generation of
    checklists.    
    """
    current_path = os.getcwd()
    clause_file = os.path.join(current_path, "datasets", "combined_data.csv")
    dataframe = pd.read_csv(clause_file)
    data_filtered = None
    if clause_model.standard_name == "ISO 26262":
        data_filtered = dataframe[
            (dataframe['Part'] == clause_model.part_number) &
            (dataframe['Clause'] == clause_model.clause_number)
        ]
    if not data_filtered.empty:
        message = {"role": "user", "content": f"Clause {clause_model.clause_number} found."}
        clause_summary = send_prompt([message])
        return clause_summary
    return None


def retrieve_external_id_knowledge(external_id_model: RequirementIdModel) -> str:
    """
    Given a specific requirement ID, the function searches for extra knowledge in the clause file.
    This knowledge is returned as a string to extend the prompt and context for the generation of
    checklists.    
    """
    filtered_df = None
    # Check if the clause model exists and contains data
    if external_id_model:
        current_path = os.getcwd()
        clause_file = os.path.join(current_path, "datasets", "combined_data.csv")
        dataframe = pd.read_csv(clause_file)
        if external_id_model.standard_name == "ISO 26262":
            filtered_df = dataframe[
                (dataframe['Part'] == external_id_model.part_number) &
                (dataframe['Clause'] == external_id_model.clause_number) &
                (dataframe['Section'] == external_id_model.subsection_number)
            ]
            if external_id_model.subsection_number != 0:
                filtered_df = dataframe[
                    (dataframe['Subsection'] == external_id_model.subsection_number)
                ]
            if external_id_model.subsubsection_number != 0:
                filtered_df = dataframe[
                    (dataframe['Subsubsection'] == external_id_model.subsubsection_number)
                ]

    if not filtered_df.empty:
        result = ""
        for _, row in filtered_df.iterrows():
            result += f"ID: {row['ID']}\nDescription: {row['Description']}\n\n"
        return result
    return None
