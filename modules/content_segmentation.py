"""
Info:
    This script segments content by filtering information, extracting relevant data from ISO 
    standards, and grouping it by topics.
Functions:
- prepare_filter_information(requirement: dict) -> dict: 
    Prepares the message that filters relevant information and removes references.
- get_iso_knowledge(requirement: dict) -> dict: 
    Extracts specific information from ISO standards.
- process_tables(requirement: dict) -> str: 
    Retrieve information from identified tables.
- process_clauses(requirement: dict) -> str: 
    Retrieve information from identified clauses.
- process_external_ids(requirement: dict) -> str: 
    Retrieve information from identified external IDs.
- format_external_id_info(id_model) -> str: 
    Format the external ID information.
- group_by_topics(requriements_work_product: list[dict]) -> dict: 
    Message with the groups content by specified topics.
"""

import os

from llm_services.prompts_content import prompt_filter_requirement, prompt_generate_topics
from llm_services.models_content import (
    IdentifyTablesModel, IdentifyClausesModel, IdentifyExternalIdsModel, TopicslistModel,
    NoInfoModel)
from llm_services.send_prompt import send_prompt

from utils.extract_iso_knowledge import (
    identify_table, identify_clause, identify_external_id, retrieve_table_knowledge,
    retrieve_clause_knowledge, retrieve_external_id_knowledge)


def prepare_filter_information(requirement: dict) -> dict:
    """
    Prepares the message that filters relevant information and removes references.

    Args:
    requirement (dict): The requirement to be filtered.

    Returns:
    dict: The filtered requirement based on the predefined criteria.
    """
    prompt_filter = prompt_filter_requirement(requirement)
    message = {"role": "user", "content": prompt_filter}
    return message


def get_iso_knowledge(requirement: dict) -> str:
    """
    Extracts specific information from ISO standards.

    Args:
        requirement (dict): The requirement dictionary containing standard information.

    Returns:
        str: The extracted information from the ISO standard.
    """
    if requirement["Standard Name"] != 'ISO 26262' or os.getenv("EXTRACT_ISO_KNOWLEDGE") != 'true':
        return None

    print("- Extracting external references...")
    retrieved_information = ""

    # Process tables
    retrieved_information += process_tables(requirement)

    # Process clauses
    retrieved_information += process_clauses(requirement)

    # Process external IDs
    retrieved_information += process_external_ids(requirement)

    if retrieved_information:
        retrieved_information = ("From the requirement, the following information was found:\n"
        + retrieved_information)

    message = {"role": "user", "content": retrieved_information}
    return message


def process_tables(requirement: dict) -> str:
    """Retrieve information from identified tables."""
    table_models = identify_table(requirement)
    if not table_models or isinstance(table_models, NoInfoModel):
        print("- No table information found")
        return ""

    retrieved_info = ""
    table_models_json = IdentifyTablesModel.model_validate(table_models)
    for table in table_models_json.tables:
        retrieved_table_info = retrieve_table_knowledge(table)
        if retrieved_table_info:
            table_info = (
                f"Table {table.table_number} from the standards {table.standard_name} "
                f"in part {table.part_number} was found."
            )
            print(table_info)
            retrieved_info += f"{table_info}\n{retrieved_table_info}\n"
    return retrieved_info


def process_clauses(requirement: dict) -> str:
    """Retrieve information from identified clauses."""
    clauses_models = identify_clause(requirement)
    if not clauses_models or isinstance(clauses_models, NoInfoModel):
        print("- No clause information found")
        return ""

    retrieved_info = ""
    clause_models_json = IdentifyClausesModel.model_validate(clauses_models)
    for clause in clause_models_json.clauses:
        retrieved_clause_info = retrieve_clause_knowledge(clause)
        if retrieved_clause_info:
            clause_intro = (
                f"Clause {clause.clause_number} from the standards {clause.standard_name} "
                f"in part {clause.part_number} was found."
            )
            print(clause_intro)
            clause_summary = f"Clause {clause.clause_number} summary and key points:\n"
            retrieved_info += f"{clause_intro}\n{clause_summary}{retrieved_clause_info}\n"
    return retrieved_info


def process_external_ids(requirement: dict) -> str:
    """Retrieve information from identified external IDs."""
    external_id_models = identify_external_id(requirement)
    if not external_id_models or isinstance(external_id_models, NoInfoModel):
        print("- No external ID information found")
        return ""

    retrieved_info = ""
    external_id_models = IdentifyExternalIdsModel.model_validate(external_id_models)
    for id_model in external_id_models.external_ids:
        retrieve_id_model = retrieve_external_id_knowledge(id_model)
        if retrieve_id_model:
            external_id_info = format_external_id_info(id_model)
            print(external_id_info)
            retrieved_info += f"{external_id_info}\n{retrieve_id_model}\n"
    return retrieved_info


def format_external_id_info(id_model) -> str:
    """Format the external ID information."""
    if id_model.subsection_number == 0:
        return f"External ID {id_model.clause_number}.{id_model.section_number} found."
    if id_model.subsubsection_number == 0:
        return (
            f"External ID {id_model.clause_number}."
            f"{id_model.section_number}.{id_model.subsection_number} found.")
    return (
        f"External ID {id_model.clause_number}."
        f"{id_model.section_number}."
        f"{id_model.subsection_number}."
        f"{id_model.subsubsection_number} found.")


def group_by_topics(requriements_work_product: list[dict]) -> dict:
    """
    Groups content by specified topics or categories.

    Args:
    data (list): The data to be grouped.
    criteria (str): The criteria for grouping the data.

    Returns:
    dict: The grouped data based on the specified criteria.
    """
    prompt = prompt_generate_topics(requriements_work_product)
    message = {"role": "user", "content": prompt}
    response_topics = send_prompt([message], TopicslistModel)
    group_message_content = (
        "This work product can be grouped by these topics: \n"
        f"{response_topics.model_dump_json()}"
    )
    group_message = {"role": "system", "content": group_message_content}
    return group_message
