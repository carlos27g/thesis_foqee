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
            description.
            ASPICE:
            - 'Standard Name' (str): The name of the standard framework.
            - 'Complete ID' (str): The full identifier of the requirement.
            - 'Work Product' (str): The work product associated with the requirement.
            - 'Description' (str): The description of the requirement.
    Returns:
        str: A formatted prompt string for analyzing and abstracting the requirement content.
             If the 'Standard Name' is not recognized, returns None.
    """

    prompt = (
        f"You are provided with a requirement from the **{requirement['Standard Name']}** "
        "standard framework. Your task is to analyze the description and external references "
        "(if given) to filter and abstract their content to include only essential information.\n"

        "The goal is to return information that allows developers to understand what to do for "
        "compliance without having to read the guidelines. Therefore, mentioning any external "
        "references is not allowed (No table numbers, clauses, ids).\n\n"
    )
    prompt += (
        "**Task Instructions:**\n"
        "1. **Analyze the provided requirement and any external references (if given).**\n"
        "2. **Filter the information** to extract only the key points relevant for compliance "
        "tracking.\n"
        "   - Focus on actionable items, obligations, and guidelines necessary for compliance.\n"
        "   - Disregard any irrelevant or redundant information.\n"
        "   - Remove all the external references (IDs, clauses, tables).\n"
        "3. **Filter the content** that addresses the following questions:\n"
        "   - What documentation or evidence is needed to demonstrate compliance with this "
        "standard?\n"
        "   - What processes or procedures should be implemented to ensure ongoing compliance?\n"
        "   - Is there any indication of how compliance should be monitored and maintained over " 
        "time?\n"
        "4. **Ensure the content is based exclusively on the information provided** in the "
        "requirement and external references.\n"
        "   - Do not introduce information that is not present in the provided requirement.\n\n"
        "**Important Note:**\n"
        "- If the provided information does not contain sufficient details to address the "
        "work product above, simply state: 'No actionable items could be identified based on the "
        "provided information.'\n\n"
    )
    if requirement['Standard Name'] == 'ISO 26262':
        # Extract titles to enrich the prompt
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
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
            - 'Standard Name': The name of the standard (e.g., 'ISO 26262').
            - 'Part': The part number of the standard.
            - 'Clause': The clause number of the standard.
            - 'Section': The section number of the standard.
            - 'Subsection': The subsection number of the standard.
            - 'Subsubsection': The subsubsection number of the standard (if applicable).
            - 'Complete ID': The full identifier of the requirement.
            - 'Work Product': The work product associated with the requirement.
            - 'Description': The description of the requirement.
    """

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
        )
        prompt = (
            "You are given a requirement from the ISO 26262 standard framework. Your task is to "
            "analyze the description and identify any references to tables.\n\n"
            "**Task Instructions:**\n"
            "1. **Identify references to tables:**\n"
            "   - Search the description for any references to tables.\n"
            "   - A table is referenced only if the keyword 'Table' is followed by a number "
            "(e.g., 'Table 3').\n"
            "   - **Note:** References to figures, sections, or clauses are **not** tables.\n\n"
            "2. **For each table referenced, extract:**\n"
            "   - **Standard Name:** 'ISO 26262' or 'ASPICE' (if mentioned; otherwise, use "
            "'ISO 26262').\n"
            "   - **Part Number:** If a part number is mentioned with the table, use that; "
            "otherwise, use the part number from the requirement details.\n"
            "   - **Table Number:** The integer number immediately following the word 'Table'.\n\n"
            "3. **If multiple tables are referenced, list all of them following the format above."
            "**\n\n"
            "4. **If no table is referenced, return an empty result.**\n\n"
        )
        prompt += (
            "**Requirement to analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"  - **Part {requirement['Part']}:** {titles.get('Part', 'N/A')}\n"
            f"    - **Clause {requirement['Clause']}:** {titles.get('Clause', 'N/A')}\n"
            f"      - **Section {requirement['Section']}:** {titles.get('Section', 'N/A')}\n"
            f"        - **Subsection ** {requirement['Subsection']}\n"
        )
        if pd.notna(requirement['Subsubsection']):
            prompt += (
                f"          - **Subsubsection :** {requirement['Subsubsection']}\n"
            )
        prompt += (
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )
        return prompt
    return None


def prompt_identify_clause(requirement) -> str:
    """
    Generates a prompt for identifying references to external clauses in a given requirement 
    from the ISO 26262 standard framework.
    Args:
        requirement (dict): A dictionary containing details of the requirement. Expected keys are:
            - 'Standard Name': The name of the standard (e.g., 'ISO 26262').
            - 'Part': The part number of the standard.
            - 'Clause': The clause number of the standard.
            - 'Section': The section number of the standard.
            - 'Subsection': The subsection number of the standard.
            - 'Subsubsection': The subsubsection number of the standard (optional).
            - 'Complete ID': The complete identifier of the requirement.
            - 'Work Product': The work product associated with the requirement.
            - 'Description': The description of the requirement.
   """

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
        )
        prompt = (
            "You are given a requirement from the ISO 26262 standard framework. Your task is to "
            "analyze the description and identify any references to external clauses.\n\n"
            "**Task Instructions:**\n"
            "1. **Identify references to clauses:**\n"
            "   - Search the description for any references to clauses.\n"
            "   - A clause is referenced only if the keyword 'Clause' is followed by a number.\n"
            "   - **Note:** IDs in the format 'Integer.Integer' (e.g., '2.3') or 'Integer.Integer."
            "Integer' (e.g., 1.2.3.) are **not** clauses but IDs and they will be re.\n"
            "   - **Note:** References to tables, figures, or sections are **not** clauses "
            "either.\n"
            "2. **For each clause referenced, extract:**\n"
            "   - **Standard Name:** 'ISO 26262' or 'ASPICE' (if mentioned; otherwise, use "
            "'ISO 26262').\n"
            "   - **Part Number:** If a part number is mentioned with the clause, use that; "
            "otherwise, use the part number from the requirement details.\n"
            "   - **Clause Number:** The integer number immediately following the word 'clause'.\n"
            "3. **If multiple clauses are referenced, list all of them.**\n\n"
            "4. **If no clause is referenced, return an empty result.**\n\n"
            "**Requirement Details:**\n"
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
        return prompt
    return None


def prompt_identify_external_id(requirement) -> str:
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
    """

    if requirement['Standard Name'] == 'ISO 26262':
        titles = get_requirement_titles(
            requirement['Standard Name'],
            requirement['Part'],
            requirement['Clause'],
            requirement['Section']
        )
        prompt = (
            "You will be provided with a requirement from the **ISO 26262** standard "
            "framework at the end.\n"
            "**Task Instructions:**\n"
            "1. **Identify external references to other sections and subsections** within the "
            "description of the requirement.\n"
            "   - An external ID from **ISO 26262** always comes in the form of Integer.Integer "
            "(Clause.Section) or Integer.Integer.Integer (Clause.Section.Subsection).\n"
            "   - Sometimes a fourth number is added (Clause.Section.Subsection.Integer). Add this "
            "last number to the 'Subsection_number'.\n"
            "   - **'2018' or numbers greater than '999' are the version of the Guidelines and not "
            "part of the ID format above.\n"
            "   - **Do not extract references that only mention 'Clause' followed by a number "
            "(e.g., 'Clause 9' or 'Clause 7'), as these refer to the clause in general and not a "
            "specific section or subsection.**\n"
            "   - **Important:** **Do not include external IDs where the section number is zero; "
            "these are considered references to clauses and should be ignored.**\n"
            "   - **Note:** **External IDs may appear on their own, without any preceding words or "
            "identifiers or they may follow phrases like 'in accordance with', 'according "
            "to', etc.**\n"
            "2. For each external ID found, extract the following information:\n"
            "   **Standard Framework:** 'ISO 26262'.\n"
            "   **Part Number:** The part number where the external ID is located. If none is "
            "mentioned, use the one from the requirement details.\n"
            "   **Clause Number:** The clause number where the external ID is located. If none is "
            "mentioned, use the one from the requirement details.\n"
            "   **Section Number:** The full section number where the external ID is located.\n"
            "   - **Important:** **'Section Number' is never zero '0'. Ignore any references that "
            "result in a section number of zero.**\n"
            "   **Subsection Number:** The subsection number where the external ID is located, if "
            "applicable; otherwise, return zero.\n"
            "3. **If multiple external IDs are referenced, list all of them.**\n\n"
            "4. **If no external IDs are referenced, return an empty list or do not return "
            "anything.**\n\n"
            "5. **Ensure the accuracy of the extracted information from the description of the "
            "requirement; only valid external IDs matching the specified formats above are "
            "extracted.**\n"
        )
        prompt += (
            "**Example:**\n"
            "**Input:**\n"
            "- **Full ID:** 26262-6:2018-6.4.2\n"
            "- **Description:** '... in accordance with Clause 9 and 2.4.4 ...'\n"
            "**Expected Output:**\n"
            "- **External IDs found:**\n"
            "  1. **Standard Framework:** ISO 26262\n"
            "     - **Part Number:** 6\n"
            "     - **Clause Number:** 2\n"
            "     - **Section Number:** 4\n"
            "     - **Subsection Number:** 4\n"
            "- **Note:** The reference to 'Clause 9' is not included because it refers "
            "to a clause in general and not a specific section or subsection. Any reference "
            "resulting in a section number of zero is ignored.\n\n"
        )
        prompt += (
            f"**Requirement to analyze:**\n"
            f"- **Full ID:** {requirement['Complete ID']}\n"
            f"- **Standard:** {requirement['Standard Name']}\n"
            f"  - **Part {requirement['Part']}:** {titles.get('Part', 'N/A')}\n"
            f"    - **Clause {requirement['Clause']}:** {titles.get('Clause', 'N/A')}\n"
            f"      - **Section {requirement['Section']}:** {titles.get('Section', 'N/A')}\n"
            f"        - **Subsection :** {requirement['Subsection']}\n"
        )
        if pd.notna(requirement['Subsubsection']):
            prompt += (
                f"          - **Subsubsection :** {requirement['Subsubsection']}\n"
            )
        prompt += (
            f"- **Work Product:** {requirement['Work Product']}\n"
            f"- **Description:**\n"
            f"'{requirement['Description']}'\n\n"
        )
        return prompt
    return None


def create_clause_summary_prompt(clause_model: dict, clause_requirements: pd) -> str:
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
        f"**Clause Details:**\n"
        f"- **Standard:** {clause_model.standard_name}\n"
        f"  - **Part {clause_model.part_number}:** {titles['Part']}\n"
        f"    - **Clause {clause_model.clause_number}:** {titles['Clause']}\n"
        f"**Requirements Within the Clause:**\n"
        f"{clause_info}"
        f"**Task Instructions:**\n"
        f"Please provide a summary of Clause {clause_model.clause_number} that includes:\n"
        f"- The key concepts presented in the clause.\n"
        f"- Instructions or guidelines for compliance.\n\n"
        f"**Guidelines for the Summary:**\n"
        f"- Use clear and concise language.\n"
        f"- Present the information in bullet points or numbered lists for readability.\n"
        f"- Focus on the most critical aspects that are essential for understanding and "
        f"compliance.\n\n"
    )
    return prompt


# ----------------- Prompt topics ----------------- #
def prompt_generate_topics(requirements_work_product: list[dict]) -> str:
    """
    Generates a prompt for grouping content by specified topics or categories.
    Args:
        requirements_work_product (list): The data to be grouped.
    Returns:
        str: A formatted prompt string for grouping content by topics or categories.
    """

    prompt = (
        "You are tasked with grouping the provided requirements by specified topics or categories "
        "to facilitate the organization and understanding of the content.\n\n"
        "**Task Instructions:**\n"
        "1. **Review the provided requirements** to identify common themes or categories.\n"
        "2. **Group the requirements** based on shared characteristics or topics.\n"
        "3. **Create a list of topics** that represent the grouped requirements.\n"
        "4. **Assign each requirement** to the corresponding topic or category.\n"
        "5. **Ensure each topic is distinct** and covers a specific aspect of the requirements.\n"
        "6. **Provide a brief description** for each topic to summarize the grouped "
        "requirements.\n\n"
        "**Content to Group:**\n"
    )
    for _ , req in requirements_work_product.items():
        prompt += (
            f"- **Requirement ID:** {req['Complete ID']}\n"
            f"  - **Description:** {req['Description']}\n"
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
