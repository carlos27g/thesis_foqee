""" This script contains all the methods necessary for step 3 'Generating Checklists'."""
import os

from termcolor import colored 

from llm_services.base_models import ChecklistModel
from llm_services.prompts import prompt_generate_checklist
from llm_services.send_prompt import send_prompt

from utils.save_markdown import save_checklist_to_markdown
from utils.save_models import save_models, load_models


def generate_checklists(dataframe):
    """
    INFO: This function generates checklists for each work product based on the provided dataframe.

    The dataframe must contain the columns: ID, Description and Work Product.
    """
    # Loop through each work product
    for work_product in dataframe['Work Product'].unique():
        if os.getenv("NEW_CHECKLISTS") != "true":
            checklist = load_models(f"{work_product} checklist")
            if checklist:
                print(colored(f"Checklist for work product {work_product} already exists.", 'green'))
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
    print(f"- Generating checklist...")
    prompt = prompt_generate_checklist(workproduct, checklists_workproduct_content)
    message = {"role": "user", "content": prompt}
    response = send_prompt([message], ChecklistModel)
    return response


def retrieve_work_product_content(work_product_rows):
    """
    INFO: This function returns the requirements of a workproduct in the form of a dictionary. 
    If external knowledge for ISO is activated, it is added to the dictionary as well.

    The work_product_rows must contain the columns: ID, Description and Work Product.
    """
    # Check if the dataframe contains the required columns
    required_columns = ['ID', 'Description', 'Work Product', 'Standard Name']
    if not all(column in work_product_rows.columns for column in required_columns):
        raise ValueError("Dataframe is missing required columns: {}".format(', '.join(required_columns)))
    print(f"- Retrieving content")
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
            raise ValueError(f"Standard Name {row[1]['Standard Name']} is not recognized. Only 'ISO 26262' and 'ASPICE' are supported.")
    print(f"- Number of requirements: {len(checklist_workproduct)}")
    return checklist_workproduct  