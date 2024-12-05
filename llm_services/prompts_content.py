"""
This script contains all the prompts used for the content segmentation part, including filtering 
the information of a requirement, extracting the ISO knowledge, and grouping topics.

Functions:
- prompt_filter_requirement: Generates a prompt for filtering and abstracting the content of a 
  given requirement from a standard framework to aid developers in understanding compliance 
  requirements.
- get_requirement_titles: Retrieves the titles for the specified part, clause, and section of the 
  ISO 26262 standard.
"""

import os
import pandas as pd

from llm_services.models_content import ClauseModel

# ----------------- Prompts for content segmentation ----------------- #
def prompt_filter_requirement(requirement) -> str:
    """
    Generates a prompt for filtering and abstracting the content of a given requirement 
    from a standard framework to aid developers in understanding compliance requirements.
    
    Args:
        requirement (dict): A dictionary containing details of the requirement, including:
            ISO26262:
            - 'Standard Name' (str): The name of the standard framework.
            - 'Complete ID' (str): The full identifier of the requirement.
            - 'Part' (str): The part of the standard.
            - 'Clause' (str): The clause of the standard.
            - 'Section' (str): The section of the standard.
            - 'Subsection' (str): The subsection of the standard.
            - 'Subsubsection' (str, optional): The subsubsection of the standard.
            - 'Work Product' (str): The work product associated with the requirement.
            - 'Description' (str): The description of the requirement.
            - 'external_knowledge' (str, optional): Any external references found in the 
              description (if ISO26262).
            ASPICE:
            - 'Standard Name' (str): The name of the standard framework.
            - 'Complete ID' (str): The full identifier of the requirement.
            - 'Work Product' (str): The work product associated with the requirement.
            - 'Description' (str): The description of the requirement.
    Returns:
        str: A formatted prompt string for analyzing and abstracting the requirement content.
             If the 'Standard Name' is not recognized or required fields are missing, returns None.
    """

    prompt = (
        f"You are provided with a requirement from the **{requirement['Standard Name']}** "
        "standard framework. Your task is to analyze the description and external references "
        "(if given) to filter and abstract their content to include only essential information "
        f"for the work product {requirement['Work Product']}.\n\n"

        f"**Objective:**\n"
        "The goal is to return information that allows developers to understand what to do for "
        "compliance without having to read the guidelines. Therefore, mentioning any external "
        "references is not allowed (No table numbers, clauses, IDs).\n\n"

        "**Task Instructions:**\n"
        "1. **Analyze the provided requirement and any external references (if given).**\n"
        "2. **Filter the information** to extract only the key points relevant for compliance "
        "tracking.\n"
        "   - Focus on actionable items, obligations, and guidelines necessary for compliance.\n"
        "   - Disregard any irrelevant or redundant information.\n"
        "   - Remove all external references (IDs, clauses, tables).\n"
        "3. **Filter the content** that addresses the following questions:\n"
        "   - What are the essential criteria to evaluate the quality of the associated "
        "work product?\n"
        "   - What documentation or evidence is needed to demonstrate that the work product "
        "complies with the standard's requirements?\n"
        "   - Are there any specific attributes or characteristics of the work product that "
        "should be verified or validated?\n"
        "4. **Ensure the content is based exclusively on the information provided** in the "
        "requirement and external references.\n"
        "   - Do not introduce information that is not present in the provided requirement.\n\n"

        "**Important Note:**\n"
        "- If the provided information does not contain sufficient details to address the "
        "work product, simply state: 'No actionable items could be identified based on the "
        "provided information.'\n\n"
    )

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement.get('Part'),
            requirement.get('Clause'),
            requirement.get('Section')
        )
        prompt += (
            f"**Requirement to Analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"  - **Part {requirement['Part']}:** {titles['Part']}\n"
            f"    - **Clause {requirement['Clause']}:** {titles['Clause']}\n"
            f"      - **Section {requirement['Section']}:** {titles['Section']}\n"
            f"        - **Subsection:** {requirement['Subsection']}\n"
        )
        if pd.notna(requirement['Subsubsection']):
            prompt += (
                f"          - **Subsubsection:** {requirement['Subsubsection']}\n"
            )
        prompt += (
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )
        if 'external_knowledge' in requirement and requirement['external_knowledge']:
            prompt += (
                "**Note:**\n"
                "External references for this ISO 26262 requirement can be found in previous "
                "messages if available."
            )
        return prompt

    if requirement['Standard Name'] == 'ASPICE':
        prompt += (
            f"**Requirement to Analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )
        return prompt

    return None


# ----------------- Prompts for ISO knowledge retrieval ----------------- #
def prompt_identify_table(requirement: dict) -> str:
    """
    Generates a prompt for extracting references to tables from a given ISO 26262 requirement.

    Args:
        requirement (dict): A dictionary containing details of the requirement, including:
            - 'Standard Name' (str): The name of the standard (e.g., 'ISO 26262').
            - 'Part' (str): The part number of the standard.
            - 'Clause' (str): The clause number of the standard.
            - 'Section' (str): The section number of the standard.
            - 'Subsection' (str): The subsection number of the standard.
            - 'Subsubsection' (str, optional): The subsubsection number of the standard.
            - 'Complete ID' (str): The full identifier of the requirement.
            - 'Work Product' (str): The work product associated with the requirement.
            - 'Description' (str): The description of the requirement.

    Returns:
        str: A formatted prompt string to identify references to tables within the requirement 
             description.
             If the 'Standard Name' is not 'ISO 26262', returns None.
    """

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
        )

        prompt = (
            "You are given a requirement from the ISO 26262 standard framework. "
            "Your task is to analyze the requirement description and identify any references "
            "to tables.\n\n"
        )

        prompt += (
            "**Objective:**\n"
            "Identify references to tables within the description to aid developers in locating "
            "relevant tabular information.\n\n"
        )

        prompt += (
            "**Task Instructions:**\n"
            "1. **Identify references to tables:**\n"
            "   - Search the description for any references to tables.\n"
            "   - A table is referenced only if the keyword 'Table' is followed by a number "
            "(e.g., 'Table 3').\n"
            "   - **Note:** References to figures, sections, or clauses are **not** considered "
            "tables.\n"
            "2. **For each table referenced, extract:**\n"
            "   - **Standard Name:** 'ISO 26262' (default for this requirement).\n"
            "   - **Part Number:** If a part number is mentioned with the table, use it; "
            "otherwise, "
            "use the part number from the requirement details.\n"
            "   - **Table Number:** The integer number immediately following the word 'Table'.\n"
            "3. **List all identified tables:**\n"
            "   - Include all references to tables in the format above.\n"
            "4. **If no table is referenced, return an empty result.**\n\n"
        )

        # Expected Outcome
        prompt += (
            "**Expected Outcome:**\n"
            "Use the `IdentifyTablesModel` function tool to define and process the result:\n"
            "- The tool should include a `tables` attribute containing a list of table details.\n"
            "- Each table detail should include the `table_number` field, representing the "
            "table's number.\n"
        )

        # Extra Information
        prompt += (
            "**Requirement to Analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"  - **Part {requirement['Part']}:** {titles.get('Part', 'N/A')}\n"
            f"    - **Clause {requirement['Clause']}:** {titles.get('Clause', 'N/A')}\n"
            f"      - **Section {requirement['Section']}:** {titles.get('Section', 'N/A')}\n"
            f"        - **Subsection:** {requirement['Subsection']}\n"
        )
        if 'Subsubsection' in requirement and pd.notna(requirement['Subsubsection']):
            prompt += f"          - **Subsubsection:** {requirement['Subsubsection']}\n"
        prompt += (
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )

        return prompt

    return None


def prompt_identify_clause(requirement: dict) -> str:
    """
    Generates a prompt for identifying references to external clauses in a given requirement 
    from the ISO 26262 standard framework.

    Args:
        requirement (dict): A dictionary containing details of the requirement. Expected keys are:
            - 'Standard Name' (str): The name of the standard (e.g., 'ISO 26262').
            - 'Part' (str): The part number of the standard.
            - 'Clause' (str): The clause number of the standard.
            - 'Section' (str): The section number of the standard.
            - 'Subsection' (str): The subsection number of the standard.
            - 'Subsubsection' (str, optional): The subsubsection number of the standard.
            - 'Complete ID' (str): The complete identifier of the requirement.
            - 'Work Product' (str): The work product associated with the requirement.
            - 'Description' (str): The description of the requirement.

    Returns:
        str: A formatted prompt string to identify references to clauses within the requirement 
             description.
             If the 'Standard Name' is not 'ISO 26262', returns None.
    """

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
        )

        # Introduction
        prompt = (
            "You are given a requirement from the ISO 26262 standard framework. "
            "Your task is to analyze the requirement description and identify any references "
            "to external clauses.\n\n"
        )

        # Objective
        prompt += (
            "**Objective:**\n"
            "Identify references to clauses within the description to ensure accurate "
            "tracking of related information.\n\n"
        )

        # Task Instructions
        prompt += (
            "**Task Instructions:**\n"
            "1. **Identify references to clauses:**\n"
            "   - Search the description for any references to clauses.\n"
            "   - A clause is referenced only if the keyword 'Clause' is followed by a number.\n"
            "   - **Note:** IDs in the format 'Integer.Integer' (e.g., '2.3') or "
            "'Integer.Integer.Integer' (e.g., '1.2.3') are **not** clauses but IDs and should "
            "be ignored.\n"
            "   - **Note:** References to tables, figures, or sections are **not** clauses.\n\n"
            "2. **For each clause referenced, extract:**\n"
            "   - **Standard Name:** 'ISO 26262' (default for this requirement).\n"
            "   - **Part Number:** If a part number is mentioned with the clause, use it; "
            "otherwise, use the part number from the requirement details.\n"
            "   - **Clause Number:** The integer number immediately following the word "
            "'Clause'.\n\n"
            "3. **List all identified clauses:**\n"
            "   - Include all references to clauses in the format above.\n\n"
            "4. **If no clause is referenced, return an empty result.**\n\n"
        )

        # Expected Outcome
        prompt += (
            "**Expected Outcome:**\n"
            "Use the `IdentifyClausesModel` function tool to define and process the result:\n"
            "- The tool should include a `clauses` attribute containing a list of clause details.\n"
            "- Each clause detail should follow the `ClauseModel` structure, including:\n"
            "  - `clause_number`: The number of the clause as specified in the requirement "
            "description.\n"
        )

        # Extra Information
        prompt += (
            "**Requirement to Analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"  - **Part {requirement['Part']}:** {titles.get('Part', 'N/A')}\n"
            f"    - **Clause {requirement['Clause']}:** {titles.get('Clause', 'N/A')}\n"
            f"      - **Section {requirement['Section']}:** {titles.get('Section', 'N/A')}\n"
            f"        - **Subsection:** {requirement['Subsection']}\n"
        )
        if 'Subsubsection' in requirement and pd.notna(requirement['Subsubsection']):
            prompt += f"          - **Subsubsection:** {requirement['Subsubsection']}\n"
        prompt += (
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )

        return prompt

    return None



def prompt_identify_external_id(requirement: dict) -> str:
    """
    Generates a detailed prompt for identifying external references within a requirement 
    from the ISO 26262 standard framework.

    Args:
        requirement (dict): A dictionary containing details of the requirement, including:
            - 'Standard Name' (str): The name of the standard (e.g., 'ISO 26262').
            - 'Part' (str): The part number of the standard.
            - 'Clause' (str): The clause number of the standard.
            - 'Section' (str): The section number of the standard.
            - 'Subsection' (str): The subsection number of the standard.
            - 'Subsubsection' (str, optional): The subsubsection number of the standard.
            - 'Complete ID' (str): The complete ID of the requirement.
            - 'Work Product' (str): The work product associated with the requirement.
            - 'Description' (str): The description of the requirement.

    Returns:
        str: A formatted prompt string to identify references to external IDs within the 
             requirement description. If the 'Standard Name' is not 'ISO 26262', returns None.
    """

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
        )

        prompt = (
            "You are given a requirement from the ISO 26262 standard framework. "
            "Your task is to analyze the description and identify any references to external "
            "IDs.\n\n"
        )

        prompt += (
            "**Objective:**\n"
            "Extract references to external IDs within the description to ensure accurate "
            "tracking of related information.\n\n"
        )

        prompt += (
            "**Task Instructions:**\n"
            "1. **Identify external references to other sections and subsections:**\n"
            "   - External IDs are in the format Integer.Integer (Clause.Section) or Integer."
            "Integer.Integer (Clause.Section.Subsection).\n"
            "   - A fourth number (Clause.Section.Subsection.Integer) may appear; include this as "
            "the 'Subsection_number'.\n"
            "   - Ignore references like 'Clause 9' or 'Clause 7' that refer to a clause in "
            "general.\n"
            "   - Ignore IDs where the section number is zero (e.g., '2.0').\n\n"
            "2. **For each external ID found, extract:**\n"
            "   - **Standard Framework:** Always 'ISO 26262'.\n"
            "   - **Part Number:** If specified; otherwise, use the part number from the "
            "requirement.\n"
            "   - **Clause Number:** If specified; otherwise, use the clause number from the "
            "requirement.\n"
            "   - **Section Number:** The section number of the external ID (must not be zero).\n"
            "   - **Subsection Number:** If applicable; otherwise, return zero.\n\n"
            "3. **List all identified external IDs.**\n"
            "4. **If no external IDs are found, return an empty list.**\n\n"
        )

        prompt += (
            "**Expected Outcome:**\n"
            "Use the `IdentifyExternalIdsModel` function tool to define and process the result:\n"
            "- The tool should include an `external_ids` attribute containing a list of external "
            "ID details.\n"
            "- Each external ID detail should follow the `RequirementIdModel` structure, "
            "including:\n"
            "  - `part_number`: The part number of the external ID.\n"
            "  - `clause_number`: The clause number of the external ID.\n"
            "  - `section_number`: The section number of the external ID.\n"
            "  - `subsection_number`: The subsection number of the external ID.\n"
            "  - `subsubsection_number`: The subsubsection number of the external ID "
            "(if applicable).\n"
            "- If no external IDs are referenced, the `external_ids` attribute should be an empty "
            "list.\n\n"
        )

        prompt += (
            "**Requirement to Analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"  - **Part {requirement['Part']}:** {titles.get('Part', 'N/A')}\n"
            f"    - **Clause {requirement['Clause']}:** {titles.get('Clause', 'N/A')}\n"
            f"      - **Section {requirement['Section']}:** {titles.get('Section', 'N/A')}\n"
            f"        - **Subsection:** {requirement['Subsection']}\n"
        )
        if 'Subsubsection' in requirement and pd.notna(requirement['Subsubsection']):
            prompt += f"          - **Subsubsection:** {requirement['Subsubsection']}\n"
        prompt += (
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )

        return prompt

    return None


def create_clause_summary_prompt(clause_model: ClauseModel,
                                 clause_requirements: pd.DataFrame) -> str:
    """
    Generates a prompt for summarizing a specific clause from a standard document.

    Args:
        clause_model: An object containing details about the clause, including:
            - standard_name (str): The name of the standard.
            - part_number (int): The part number of the standard.
            - clause_number (int): The clause number within the standard.
        clause_requirements: A DataFrame containing the requirements of the clause, with each 
                             row representing a requirement and columns:
            - 'ID' (str): The identifier of the requirement.
            - 'Description' (str): The description of the requirement.

    Returns:
        str: A formatted prompt string to summarize the clause.
    """

    titles = get_requirement_titles(
        standard=clause_model.standard_name,
        part=clause_model.part_number,
        clause=clause_model.clause_number,
    )

    clause_info = ""
    for _, row in clause_requirements.iterrows():
        clause_info += (
            f"- **Requirement ID:** {row['ID']}\n"
            f"  - **Description:** {row['Description']}\n\n"
        )

    prompt = (
        f"You are provided with information regarding **Clause {clause_model.clause_number}** "
        f"of the **{clause_model.standard_name}** standard.\n\n"

        f"**Objective:**\n"
        f"- Summarize the key concepts, instructions, and guidelines presented in Clause "
        f"{clause_model.clause_number}.\n\n"

        f"**Clause Details:**\n"
        f"- **Standard:** {clause_model.standard_name}\n"
        f"  - **Part {clause_model.part_number}:** {titles['Part']}\n"
        f"    - **Clause {clause_model.clause_number}:** {titles['Clause']}\n\n"

        f"**Requirements Within the Clause:**\n"
        f"{clause_info}"

        f"**Task Instructions:**\n"
        f"1. Identify and summarize the key concepts and guidelines within Clause "
        f"{clause_model.clause_number}.\n"
        f"2. Highlight instructions or recommendations necessary for compliance.\n\n"
        f"**Guidelines for the Summary:**\n"
        f"- Use clear and concise language.\n"
        f"- Present the information in bullet points or numbered lists for readability.\n"
        f"- Focus on critical aspects essential for understanding and compliance.\n\n"
    )

    return prompt



# ----------------- Prompt topics ----------------- #
def prompt_generate_topics(requirements_work_product: list[dict]) -> str:
    """
    Generates a prompt for grouping content by specified topics or categories.

    Args:
        requirements_work_product (list): A list of dictionaries, where each dictionary contains:
            - 'Complete ID' (str): The unique identifier of the requirement.
            - 'Description' (str): The detailed description of the requirement.

    Returns:
        str: A formatted prompt string for grouping content by topics or categories.
    """

    # Introduction
    prompt = (
        "You are tasked with grouping the provided requirements by specified topics or categories "
        "to facilitate the organization and understanding of the content.\n\n"
    )

    # Objective
    prompt += (
        "**Objective:**\n"
        "- Group requirements into distinct topics or categories based on shared themes or "
        "characteristics.\n"
        "- If there is context in the messages from before, consider any disambiguating terms "
        "or information "
        "provided to ensure the topics are as precise as possible.\n\n"
    )

    # Task Instructions
    prompt += (
        "**Task Instructions:**\n"
        "1. **Review the provided requirements** to identify common themes or categories.\n"
        "2. **Group the requirements** based on shared characteristics or topics.\n"
        "3. **Create a list of topics** that represent the grouped requirements.\n"
        "4. **Assign each requirement** to the corresponding topic or category.\n"
        "5. **Ensure each topic is distinct** and covers a specific aspect of the requirements.\n"
        "6. **Provide a brief description** for each topic to summarize the grouped requirements.\n"
        "7. **Incorporate previous context** (if available) to resolve ambiguities and refine "
        "the topics.\n\n"
    )

    # Content to Group
    prompt += "**Content to Group:**\n"
    for _, req in requirements_work_product.items():
        prompt += (
            f"- **Requirement ID:** {req['Complete ID']}\n"
            f"  - **Description:** {req['Description']}\n"
        )

    # Expected Outcome
    prompt += (
        "\n**Expected Outcome:**\n"
        "Use the `TopicslistModel` function tool to define and process the result:\n"
        "- The tool should include a `topics` attribute containing a list of grouped topics.\n"
        "- Each topic should follow the `TopicModel` structure, including:\n"
        "  - `topic`: A brief title for the topic that represents a shared characteristic "
        "or theme.\n"
        "  - `ids`: A list of requirement IDs that belong to this topic.\n"
        "- Requirements can belong to multiple topics if relevant.\n"
        "- Ensure each topic is distinct and provides a clear representation of its grouped "
        "requirements.\n"
        "- Consider disambiguating terms from previous messages or context when identifying "
        "topics.\n\n"
    )

    # Additional Notes
    prompt += (
        "**Additional Notes:**\n"
        "- Requirements can be repeated across multiple topics if applicable.\n"
        "- Focus on improving clarity and usability for end-users by grouping logically and "
        "concisely.\n"
    )

    return prompt


# ----------------- Helper method ----------------- #
def get_requirement_titles(standard, part, clause, section=None) -> dict:
    """
    Retrieves the titles of the specified part, clause, and optionally section, 
    from the ISO 26262 standard structure.
    Args:
        standard (str): The standard to retrieve titles from. Currently only supports 'ISO 26262'.
        part (int or str): The part number of the standard.
        clause (int or str): The clause number within the specified part.
        section (int or str, optional): The section number within the specified clause. 
                                        Defaults to None.
    Returns:
        dict: A dictionary containing the titles of the specified part, clause, and optionally 
              section.      
        None: If no matching titles are found or if the standard is not supported.
    """

    current_path = os.getcwd()
    file_path = os.path.join(current_path, "datasets", "ISO26262_part6&8_structure.xlsx")
    iso26262_titles_df = pd.read_excel(file_path, sheet_name='Sheet1')

    if standard == 'ISO 26262':
        df = iso26262_titles_df
        filtered_df = df[
            (df['Part'].astype(str) == str(part)) &
            (df['Clause'].astype(str) == str(clause))
        ]
        if section is not None:
            filtered_df = filtered_df[filtered_df['Section'].astype(str) == str(section)]
        if filtered_df.empty:
            return None
        part_title = filtered_df.iloc[0]['Part Title']
        clause_title = filtered_df.iloc[0]['Clause Title']
        if section is None:
            return {'Part': part_title, 'Clause': clause_title}
        section_title = filtered_df.iloc[0]['Section Title']
        return {'Part': part_title, 'Clause': clause_title, 'Section': section_title}

    return None
