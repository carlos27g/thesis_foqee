"""
This module is responsible for generating context for the creation of checklists.

The context contains the following components:
- Definitions: Contains the definitions of terms and concepts used in the checklists.
- Descriptions: Provides detailed descriptions of the items to be included in the checklists.
- Context Generation: Combines the definitions and descriptions to generate a coherent context
    for the checklists, making them easy to understand and use.
"""
import os

import pandas as pd

from termcolor import colored

from llm_services.prompts_context import (
    prompt_gen_purpose, prompt_gen_content, prompt_gen_input, prompt_gen_uses,
    prompt_terminology_iso_extraction, prompt_disambiguation_extraction,
    prompt_abbreviations_extraction)
from llm_services.send_prompt import send_prompt
from llm_services.models_context import (
    TermListModel, DisambiguationModel, AbbreviationListModel, DescriptionModel,
    WorkProductContextModel, ConceptsModel, PurposeModel)
from utils.save_markdown import save_context_to_markdown
from utils.context_to_dict import (
    create_dict_iso_terminology, create_dict_disambiguation, create_dict_abbreviations)
from utils.save_models import save_models, load_models

def gen_context(df_standards) -> dict:
    """
    Generates context for the creation of checklists.

    Args:
    - standards (dict): Dataframe containing the standards from ISO26262 and ASPICE.

    Returns:
    - context (dict): Dictionary containing the context for each work product.
    """
    # dataset from the ASPICE and ISO26262 standards 
    work_products = df_standards['Work Product'].unique()
    df_standards_filtered = df_standards[['Work Product', 'ID', 'Description']]
    context = {}

    # Load existing context if available
    if os.getenv('CREATE_NEW_CONTEXT') == 'false':
        print(colored("Loading existing contexts...", "green"))
        for work_product in work_products:
            context_model = load_models(f"{work_product} context", WorkProductContextModel)
            if not context_model:
                print(colored("No context found for work product:", "red"), work_product)
                raise Exception(f"No context found for work product: {work_product}")
            context[work_product] = context_model
        return context

    # Create new context for the work products
    print(colored("Creating new contexts...", "green"))
    disambiguation_path = os.path.join(os.getcwd(), "datasets", "Disambiguation.xlsx")
    # datasets for contextualisation
    disambiguation_df_iso = pd.read_excel(disambiguation_path, sheet_name='Terminology in ISO 26262')
    disambiguation_df_disambiguation = pd.read_excel(disambiguation_path, sheet_name='Disambiguation')
    disambiguation_df_abbreviations = pd.read_excel(disambiguation_path, sheet_name='Abbreviations')

    # datasets for contextualisation converted to a list of dictionaries
    terminology_iso_list = create_dict_iso_terminology(disambiguation_df_iso)
    concepts_list = create_dict_disambiguation(disambiguation_df_disambiguation)
    abbreviations_list = create_dict_abbreviations(disambiguation_df_abbreviations)

    for work_product in work_products:
        print(colored(f"Processing work product: {work_product}", "green"))
        df_standards_filtered = df_standards[df_standards['Work Product'] == work_product]
        print(f"Number of standards available: {len(df_standards_filtered)}")
        concepts = filter_concepts(work_product, terminology_iso_list, concepts_list, abbreviations_list)
        description = gen_description(work_product, df_standards_filtered)
        context_model = WorkProductContextModel(
            description=description,
            concepts=concepts
        )
        context[work_product] = context_model
        if context_model:
            context_model = WorkProductContextModel.model_validate(context_model)
            save_context_to_markdown(context_model, work_product)
            save_models(f"{work_product} context", context_model)
        else:
            print(colored("No context generated for work product:", "red"), work_product)
    return context


def gen_description(work_product, standards) -> dict:
    """
    Generates the description for a given work product.

    Args:
    - work_product (str): The name of the work product.
    - standards (DataFrame): The standards that apply to the work product.

    Returns:
    - description (dict): The description of the work product.
    """
    print(colored("Generating Description for Work Product:", "green"), work_product)
    print("Number of standards available: ", len(standards))
    
    purpose_prompt = prompt_gen_purpose(work_product)
    message_purpose = {"role": "user", "content": purpose_prompt}
    purpose = send_prompt([message_purpose], PurposeModel)
    print("- Purpose done.")

    content_prompt = prompt_gen_content(work_product, standards)
    message_content = {"role": "user", "content": content_prompt}
    content = send_prompt([message_content])
    print("- Content done.")

    input_prompt = prompt_gen_input(work_product, standards)
    message_input = {"role": "user", "content": input_prompt}
    input_data = send_prompt([message_input])
    print("- Input done.")

    uses_prompt = prompt_gen_uses(work_product, standards)
    message_uses = {"role": "user", "content": uses_prompt}
    uses = send_prompt([message_uses])
    print("- Uses done.")
    
    description_model = DescriptionModel(
        purpose=purpose,
        content=content,
        input=input_data,
        uses=uses
    )

    return description_model


def filter_concepts(work_product, terminology_iso, disambiguation, abbreviations) -> dict:
    """
    Filters the concepts relevant to a given work product.
    This function first filters the terminologies, then sends them to the list of previous messages 
    to the disambiguations, and finally to the list of abbreviations, building a system on itself.

    Args:
    - work_product (str): The name of the work product.
    - terminology_iso (list): List of terminology from ISO 26262.
    - disambiguation (list): List of disambiguation concepts.
    - abbreviations (list): List of abbreviations.

    Returns:
    - concepts (dict): Dictionary containing the relevant concepts for the work product.
    """
    print("Filtering Concepts...")

    terminology_model = None
    disambiguation_model = None
    abbreviations_model = None

    consolidated_abbreviation_model = AbbreviationListModel(abbreviations=[])
    consolidated_terminology_model = TermListModel(terms=[])
    consolidated_disambiguation_model = DisambiguationModel(entries=[])

    for i in range(0, len(terminology_iso), 5):
        batch = terminology_iso[i:min(i + 5, len(terminology_iso))]
        prompt_terminology = prompt_terminology_iso_extraction(work_product, batch)
        message_terminology = {"role": "user", "content": prompt_terminology}
        response_terminology = send_prompt([message_terminology], TermListModel)
        if response_terminology:
            terminology_model = TermListModel.model_validate(response_terminology)
            if terminology_model:
                consolidated_terminology_model.terms.extend(terminology_model.terms) # pylint: disable=no-member
    print("- Terminology done.")

    for i in range(0, len(disambiguation), 5):
        batch = disambiguation[i:min(i + 5, len(disambiguation))]
        prompt_disambiguation = prompt_disambiguation_extraction(work_product, batch)
        message_disambiguation = {"role": "user", "content": prompt_disambiguation}
        response_disambiguation = send_prompt([message_disambiguation], DisambiguationModel)
        if response_disambiguation:
            disambiguation_model = DisambiguationModel.model_validate(response_disambiguation)
            if disambiguation_model:
                consolidated_disambiguation_model.entries.extend(disambiguation_model.entries) # pylint: disable=no-member
    print("- Disambiguation done.")

    for i in range(0, len(abbreviations), 10):
        batch = abbreviations[i:min(i + 10, len(abbreviations))]
        prompt_abbreviations = prompt_abbreviations_extraction(work_product, batch)
        message_abbreviations = {"role": "user", "content": prompt_abbreviations}
        response_abbreviations = send_prompt([message_abbreviations], AbbreviationListModel)
        if response_abbreviations:
            abbreviations_model = AbbreviationListModel.model_validate(response_abbreviations)
            if abbreviations_model:
                consolidated_abbreviation_model.abbreviations.extend(abbreviations_model.abbreviations) # pylint: disable=no-member
    print("- Abbreviations done.")
    
    consolidated_disambiguation_model = DisambiguationModel.model_validate(consolidated_disambiguation_model)
    consolidated_terminology_model = TermListModel.model_validate(consolidated_terminology_model)
    consolidated_abbreviation_model = AbbreviationListModel.model_validate(consolidated_abbreviation_model)

    concepts_model = ConceptsModel(
        terminology_iso=consolidated_terminology_model,
        disambiguation=consolidated_disambiguation_model,
        abbreviations=consolidated_abbreviation_model
    )
    concepts_model = ConceptsModel.model_validate(concepts_model)
    return concepts_model

