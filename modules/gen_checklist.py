""" This script contains all the methods necessary for the step 'Generating Checklists'."""

import os
from termcolor import colored

from llm_services.models_checklist import ChecklistModel
from llm_services.models_content import RequirementDescriptionModel
from llm_services.prompts_checklist import prompt_generate_checklist
from llm_services.prompts_context import prompt_context
from llm_services.send_prompt import send_prompt

from utils.save_markdown import save_checklist_to_markdown
from utils.save_models import save_models, load_models
from utils.gen_excel_evaluation import create_excel_evaluation_sheet

from modules.content_segmentation import (
    get_iso_knowledge, prompt_filter_requirement, group_by_topics)

def generate_checklists(dataframe, context=None):
    """
    Generates checklists for each unique work product based on the provided dataframe. 
    If a checklist for a work product already exists and the environment variable 
    "NEW_CHECKLISTS" is not set to "true," the generation is skipped.

    Args:
    dataframe (pd.DataFrame): 
        A pandas DataFrame containing the following mandatory columns:
        - 'ID': Identifier for the checklist item.
        - 'Description': Description of the checklist item.
        - 'Work Product': Name of the work product associated with the checklist item.

    Returns:
    None: 
        This function performs actions such as loading, validating, and saving checklists 
        but does not return any value.
    """
    # Loop through each work product
    for work_product in dataframe['Work Product'].unique():
        if os.getenv("NEW_CHECKLISTS") != "true":
            checklist = load_models(f"{work_product} checklist", ChecklistModel)
            if checklist:
                print(colored(
                    f"Checklist for work product {work_product} already exists.", 'green'))
                continue

        print(colored(f"Generating checklist for work product: {work_product}", 'green'))

        # Retrieve the information of the work product
        work_product_rows = dataframe[dataframe['Work Product'] == work_product]
        work_product_content = retrieve_work_product_content(work_product_rows)

        # Generate the checklist for the work product
        if context:
            checklist = generate_wp_checklist(work_product, work_product_content,
                                              context[work_product])
        else:
            checklist = generate_wp_checklist(work_product, work_product_content, None)
        checklist_model = ChecklistModel.model_validate(checklist)

        # Generate the Excel evaluation sheets
        create_excel_evaluation_sheet(checklist_model, work_product_rows)

        # Save the checklist
        save_checklist_to_markdown(checklist_model, work_product)
        save_models(f"{work_product} checklist", checklist_model)


def generate_wp_checklist(work_product: str,
                          checklists_work_product_content: list[dict],
                          context: None) -> ChecklistModel:
    """
    Generates a checklist for a given work product by creating a prompt, sending it to the LLM, 
    and returning the generated response.

    Args:
    work product (str): 
        The name of the work product for which the checklist is being generated.
    checklists_work product_content (dict): 
        A dictionary containing the relevant content for the checklist, typically structured 
        information related to the work product.

    Returns:
    ChecklistModel: 
        The response from the LLM, validated as a ChecklistModel instance, containing the 
        generated checklist for the work product.
    """
    for _ , requirement_info in checklists_work_product_content.items():
        print(colored(f"Processing requirement {requirement_info['Complete ID']}", 'green'))
        # Filter requirements content
        if os.getenv("FILTER_REQUIREMENTS") == "true":
            filter_prompt = prompt_filter_requirement(requirement_info)
            filter_message = {"role": "user", "content": filter_prompt}
            print("- Filtering requirements content")
            # Retrieve external knowledge for ISO 26262
            messages_checklists = [filter_message]
            if os.getenv("EXTRACT_ISO_KNOWLEDGE") == "true":
                external_knowledge_message = get_iso_knowledge(requirement_info)
                if external_knowledge_message:
                    messages_checklists.insert(0, external_knowledge_message)
            response = send_prompt(messages_checklists, RequirementDescriptionModel)
            # Update the description with the filtered content
            requirement_info["Description"] = response.description
    messages_checklists = []
    messages_context = []

    if os.getenv("ADD_WP_CONTEXT") == "true" and context:
        messages_context = prompt_context(context, work_product)
        for message in messages_context:
            messages_checklists.append(message)

    if os.getenv("TOPIC_GROUPING") == "true":
        # Generate groups
        print(colored("Grouping requirements by topics", 'green'))
        if context:
            groups_message = group_by_topics(checklists_work_product_content, context)
        else:
            groups_message = group_by_topics(checklists_work_product_content, None)
        if groups_message:
            messages_checklists.append(groups_message)

    prompt = prompt_generate_checklist(work_product, checklists_work_product_content)
    message_checklist = {"role": "user", "content": prompt}
    messages_checklists.append(message_checklist)
    print("Generating checklist...")
    response = send_prompt(messages_checklists, ChecklistModel)
    return response


def retrieve_work_product_content(work_product_rows):
    """
    Retrieves the requirements of a work product and organizes them into a dictionary format. 
    Supports requirements from ISO 26262 and ASPICE standards. If external knowledge for ISO 
    is activated, it adds specific details to the dictionary. Raises an error if required 
    columns are missing or if an unsupported standard is encountered.

    Args:
    work_product_rows (pd.DataFrame): 
        A pandas DataFrame containing the rows corresponding to a specific work product.
        The DataFrame must include the following columns:
        - 'ID': Identifier of the requirement.
        - 'Description': Description of the requirement.
        - 'Work Product': Name of the work product.
        - 'Standard Name': The standard associated with the requirement ('ISO 26262' or 'ASPICE').
        - Additional columns for ISO 26262:
          - 'Part', 'Clause', 'Section', 'Subsection', 'Subsubsection'.

    Returns:
    dict: 
        A dictionary where the keys are the 'Complete ID' of each requirement, and the values 
        are the corresponding requirement details.
        The structure varies depending on the standard:
        - For ISO 26262: Includes 'Part', 'Clause', 'Section', 'Subsection', 'Subsubsection'.
        - For ASPICE: Includes only standard-specific details.
    """
    print("- Retrieving content")
    content_work_product = {}
    for row in work_product_rows.iterrows():
        requirement = None
        if row[1]['Standard Name'] == 'ISO 26262':
            requirement = {
                "Complete ID": row[1]['ID'],
                "Standard Name": row[1]['Standard Name'],
                "Part": row[1]['Part'],
                "Clause": row[1]['Clause'],
                "Section": row[1]['Section'],
                "Subsection": row[1]['Subsection'],
                "Subsubsection": row[1]['Subsubsection'],
                "Work Product": row[1]['Work Product'],
                "Description": row[1]['Description']
            }
        elif row[1]['Standard Name'] == 'ASPICE':
            requirement = {
                "Complete ID": row[1]['ID'],
                "Standard Name": row[1]['Standard Name'],
                "Work Product": row[1]['Work Product'],
                "Description": row[1]['Description']
            }
        if requirement:
            content_work_product[requirement['Complete ID']] = requirement
        else:
            raise ValueError(
                f"Standard Name {row[1]['Standard Name']} is not recognized. "
                "Only 'ISO 26262' and 'ASPICE' are supported."
            )
    print(f"- Number of requirements: {len(content_work_product)}")
    return content_work_product
