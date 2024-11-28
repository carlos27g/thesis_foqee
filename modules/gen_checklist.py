""" This script contains all the methods necessary for the step 'Generating Checklists'."""

import os
from termcolor import colored

from llm_services.base_models import ChecklistModel
from llm_services.prompts import prompt_generate_checklist
from llm_services.send_prompt import send_prompt

from utils.save_markdown import save_checklist_to_markdown
from utils.save_models import save_models, load_models


def generate_checklists(dataframe):
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
        checklists_workproduct_content = retrieve_work_product_content(work_product_rows)

        # Generate the checklist for the work product
        checklist = generate_wp_checklist(work_product, checklists_workproduct_content)
        checklist_model = ChecklistModel.model_validate(checklist)
        # Save the checklist
        save_checklist_to_markdown(checklist_model)
        save_models(f"{work_product} checklist", checklist_model)


def generate_wp_checklist(workproduct, checklists_workproduct_content):
    """
    Generates a checklist for a given work product by creating a prompt, sending it to the LLM, 
    and returning the generated response.

    Args:
    workproduct (str): 
        The name of the work product for which the checklist is being generated.
    checklists_workproduct_content (dict): 
        A dictionary containing the relevant content for the checklist, typically structured 
        information related to the work product.

    Returns:
    ChecklistModel: 
        The response from the LLM, validated as a ChecklistModel instance, containing the 
        generated checklist for the work product.
    """
    print("- Generating checklist...")
    prompt = prompt_generate_checklist(workproduct, checklists_workproduct_content)
    message = {"role": "user", "content": prompt}
    response = send_prompt([message], ChecklistModel)
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
    checklist_workproduct = {}
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
            checklist_workproduct[requirement['Complete ID']] = requirement
        else:
            raise ValueError(
                f"Standard Name {row[1]['Standard Name']} is not recognized. "
                "Only 'ISO 26262' and 'ASPICE' are supported."
            )
    print(f"- Number of requirements: {len(checklist_workproduct)}")
    return checklist_workproduct