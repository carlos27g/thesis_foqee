"""
This script provides a collection of methods to generate prompts for generating the context of 
work products. 

Methods:
- prompt_terminology_iso_extraction(work_product: str, terminology_iso: list[dict]) -> str:
  Generates a prompt to extract ISO 26262 terminology relevant to the given work product.
- prompt_disambiguation_extraction(work_product: str, disambiguations: list[dict]) -> str:
  Creates a prompt for filtering disambiguation concepts tied to ISO 26262.
- prompt_abbreviations_extraction(work_product: str, abbreviations: list[dict]) -> str:
  Constructs a prompt to identify abbreviations relevant to the work product.
- prompt_gen_purpose(work_product: str) -> str:
  Generates a prompt explaining the purpose of a work product in ISO 26262 and ASPICE.
- prompt_gen_uses(work_product: str, standards: pd.DataFrame) -> str:
  Creates a prompt describing the use cases of a work product based on standards.
- prompt_gen_input(work_product: str, standards: pd.DataFrame) -> str:
  Develops a prompt to identify necessary inputs for the work product's compliance.
- prompt_gen_content(work_product: str, standards: pd.DataFrame) -> str:
  Produces a prompt defining required content for the work product under compliance standards.
- prompt_context(context: WorkProductContextModel, work_product: str) -> list[dict]:
  Consolidates context and generates a comprehensive prompt for the work product.

"""

import pandas as pd

from llm_services.models_context import WorkProductContextModel

# ----------------- For Contextualization of WP ----------------- #
def prompt_terminology_iso_extraction(work_product: str, terminology_iso: list[dict]) -> str:
    """
    Extracts ISO 26262 terms relevant to the given work product.

    Args:
        work_product (str): The target work product for extraction.
        terminology_iso (list): A list of dictionaries, where each dictionary contains:
            - 'term' (str): The name of the term.
            - 'definition' (str): The description of the term.

    Returns:
        str: A formatted prompt string.
    """

    prompt = (
        f"You are tasked with identifying terms from ISO 26262 terminology that are directly "
        f"relevant to the work product '**{work_product}**'.\n\n"
    )

    prompt += (
        "**Task Instructions:**\n"
        "1. Select terms explicitly tied to creating, defining, or managing "
        f"'**{work_product}**'.\n"
        "2. Include terms related to structure, content, or evaluation criteria.\n"
        "3. Exclude terms that are only tangentially related, such as general processes or "
        "unrelated methods.\n\n"
    )

    prompt += (
        "**Output Format:**\n"
        "- Return a list of objects, where each object includes:\n"
        "  - 'term': The name of the term.\n"
        "  - 'definition': The description of the term.\n\n"
    )

    prompt += (
        "**Expected Outcome:**\n"
        "Use the `TermListModel` function tool to define and process the result:\n"
        "- The tool should include a `terms` attribute containing a list of relevant terms.\n"
        "- Each term should follow the `TermModel` structure, including:\n"
        "  - `term`: The name of the term in the glossary.\n"
        "  - `definition`: The description of the term in the glossary.\n"
        f"- Ensure only directly relevant terms to the work product '**{work_product}**' are "
        "included.\n"
    )

    prompt += (
        "**Notes:**\n"
        "- Ensure the extracted terms are directly relevant to the work product.\n"
        "- Remove references to external IDs or clauses from definitions.\n"
        "- If no relevant terms are found, return an empty result.\n\n"
    )

    prompt += "**Terminology List:**\n"
    for i, item in enumerate(terminology_iso):
        term = item.get("term", "N/A")
        definition = item.get("definition", "N/A")
        prompt += (
            f"  - **Term {i + 1}:** {term}\n"
            f"  - **Definition:** {definition}\n\n"
        )

    return prompt


def prompt_disambiguation_extraction(work_product: str, disambiguations: list[dict]) -> str:
    """
    Generates a prompt for extracting disambiguations relevant to the given work product.

    Args:
        work_product (str): The target work product for extraction.
        disambiguations (list): A list of dictionaries, where each dictionary contains:
            - 'concept' (str): The concept being disambiguated.
            - 'definition' (str): The definition of the concept.
            - 'purpose' (str): The purpose of the concept.
            - 'examples' (list[str]): Examples demonstrating the concept.
            - 'elements' (list[str]): Related elements of the concept.
            - 'example_elements' (list[str]): Example elements of the concept.
            - 'terminology_iso26262' (str): ISO 26262-related terminology for the concept.
            - 'terminology_aspice' (str): ASPICE-related terminology for the concept.

    Returns:
        str: A formatted prompt string.
    """

    prompt = (
        f"You are tasked with filtering relevant disambiguations for '**{work_product}**' "
        "from the provided table.\n\n"
    )

    prompt += (
        "**Task Instructions:**\n"
        "1. Identify concepts explicitly tied to ISO 26262 and ASPICE for the work product.\n"
        "2. Include commonly used or fundamental terms where relevance is evident.\n"
        "3. Exclude unrelated concepts unless they have wide applicability across the domain.\n\n"
    )

    prompt += (
        "**Output Format:**\n"
        "Use the `DisambiguationModel` function tool to return structured JSON:\n"
        "- The output should include an `entries` attribute containing a list of disambiguation "
        "entries.\n"
        "- Each entry should follow the `DisambiguationEntryModel` structure, including:\n"
        "  - `concept`: The concept being disambiguated.\n"
        "  - `definition`: The definition of the concept.\n"
        "  - `purpose`: The purpose of the concept.\n"
        "  - `examples`: Examples demonstrating the concept.\n"
        "  - `elements`: Related elements of the concept.\n"
        "  - `example_elements`: Example elements of the concept.\n"
        "  - `terminology_iso26262`: ISO 26262-related terminology for the concept.\n"
        "  - `terminology_aspice`: ASPICE-related terminology for the concept.\n"
    )

    prompt += "**Disambiguation Table:**\n"
    for row in disambiguations:
        prompt += (
            "{\n"
            f'  "concept": "{row.get("concept", "NA")}",\n'
            f'  "definition": "{row.get("definition", "NA")}",\n'
            f'  "purpose": "{row.get("purpose", "NA")}",\n'
            f'  "examples": {row.get("examples", "[]")},\n'
            f'  "elements": {row.get("elements", "[]")},\n'
            f'  "example_elements": {row.get("example_elements", "[]")},\n'
            f'  "terminology_iso26262": "{row.get("terminology_iso26262", "NA")}",\n'
            f'  "terminology_aspice": "{row.get("terminology_aspice", "NA")}"\n'
            "}\n\n"
        )

    return prompt


def prompt_abbreviations_extraction(work_product: str, abbreviations: list[dict]) -> str:
    """
    Generates a prompt for extracting relevant abbreviations for a given work product.

    Args:
        work_product (str): The target work product for abbreviation extraction.
        abbreviations (list): A list of dictionaries, where each dictionary contains:
            - 'abbreviation' (str): The abbreviation to extract.
            - 'definition' (str): The explanation or meaning of the abbreviation.

    Returns:
        str: A formatted prompt string.
    """

    prompt = (
        f"You are tasked with identifying abbreviations relevant to the work product "
        f"'**{work_product}**'.\n\n"
    )

    prompt += (
        "**Task Instructions:**\n"
        f"1. Identify abbreviations directly tied to the creation, management, or evaluation of "
        f"'**{work_product}**'.\n"
        "2. Provide explanations or definitions for each relevant abbreviation.\n"
        "3. Exclude abbreviations that are only tangentially related or irrelevant to the work "
        "product.\n\n"
    )

    prompt += (
        "**Output Format:**\n"
        "Use the `AbbreviationListModel` function tool to define and process the result:\n"
        "- The output should include an `abbreviations` attribute containing a list of abbreviation "
        "entries.\n"
        "- Each entry should follow the `AbbreviationModel` structure, including:\n"
        "  - `abbreviation`: The abbreviation.\n"
        "  - `definition`: The explanation or meaning of the abbreviation.\n"
    )

    prompt += "**Abbreviation List:**\n"
    for item in abbreviations:
        abbreviation = item.get("abbreviation", "N/A")
        definition = item.get("definition", "N/A")
        prompt += (
            f"- **Abbreviation:** {abbreviation}\n"
            f"- **Definition:** {definition}\n\n"
        )

    return prompt


def prompt_gen_purpose(work_product: str) -> str:
    """
    Generates a prompt for explaining the purpose of a work product.

    Args:
        work_product (str): The target work product.

    Returns:
        str: A formatted prompt string.
    """

    # Introduction
    prompt = (
        f"You are tasked with explaining the purpose of the work product '**{work_product}**' "
        f"within the context of ISO 26262 and ASPICE.\n\n"
    )

    # Task Instructions
    prompt += (
        "**Task Instructions:**\n"
        f"1. Provide a clear explanation of the purpose of '**{work_product}**' in both ISO 26262 "
        "and ASPICE standards.\n"
        "2. Focus on its role in ensuring compliance, functional safety, and quality.\n"
        "3. For ISO 26262:\n"
        "   - Highlight the work product's importance in achieving functional safety objectives.\n"
        "   - Describe its relevance to processes or guidelines outlined in ISO 26262.\n"
        "4. For ASPICE:\n"
        "   - Explain how the work product supports process improvement and quality assurance.\n"
        "   - Relate it to ASPICE's engineering or management processes.\n\n"
    )

    # Output Format
    prompt += (
        "**Output Format:**\n"
        "Use the `PurposeModel` function tool to define and process the result:\n"
        "- The tool should include:\n"
        "  - `purpose_iso`: A clear and concise description of the work product's purpose "
        "according to ISO 26262.\n"
        "  - `purpose_aspice`: A clear and concise description of the work product's purpose "
        "according to ASPICE.\n"
        "- Use structured, professional language suitable for technical reports or documentation.\n"
        "- Ensure the explanations are specific, relevant, and concise.\n\n"
    )

    return prompt


def prompt_gen_uses(work_product: str, standards: pd.DataFrame) -> str:
    """
    Generates a prompt for explaining the use cases of a work product based on given ISO 26262 
    and ASPICE standards.

    Args:
        work_product (str): The target work product.
        standards (pd.DataFrame): A DataFrame containing ISO 26262 and ASPICE requirements.

    Returns:
        str: A formatted prompt string.
    """

    standards_str = standards.to_string(index=False)

    prompt = (
        f"You are tasked with explaining the use cases of the work product '**{work_product}**' "
        f"within the context of ISO 26262 and ASPICE standards.\n\n"
    )

    prompt += (
        "**Task Instructions:**\n"
        "1. Review the provided ISO 26262 and ASPICE requirements.\n"
        f"2. Explain the primary use cases of the work product '**{work_product}**'.\n"
        "3. Describe how the work product supports documentation and compliance efforts.\n"
        "4. Focus on key points that demonstrate the work product's role in achieving compliance "
        "with ISO 26262 and ASPICE.\n"
        "5. Avoid referencing external IDs or specific clauses; only general mentions of ISO or "
        "ASPICE frameworks are permitted.\n\n"
    )

    prompt += (
        "**Output Format:**\n"
        f"- Provide a clear and concise explanation of the use cases for '**{work_product}**'.\n"
        "- Highlight its significance in ensuring compliance and facilitating documentation.\n"
        "- Use structured, professional language suitable for technical reports or "
        "documentation.\n\n"
    )

    prompt += (
        "The following ISO 26262 and ASPICE requirements are provided for context:"
        f"\n\n{standards_str}\n\n"
    )

    return prompt



def prompt_gen_input(work_product: str, standards: pd.DataFrame) -> str:
    """
    Generates a prompt for identifying the necessary inputs for a work product based 
    on ISO 26262 and ASPICE standards.

    Args:
        work_product (str): The target work product.
        standards (pd.DataFrame): A DataFrame containing ISO 26262 and ASPICE requirements.

    Returns:
        str: A formatted prompt string.
    """

    standards_str = standards.to_string(index=False)

    prompt = (
        f"You are tasked with identifying the necessary inputs for the work product "
        f"'**{work_product}**' "
        f"to ensure compliance with ISO 26262 and ASPICE standards.\n\n"
    )

    prompt += (
        "**Task Instructions:**\n"
        "1. Review the provided ISO 26262 and ASPICE requirements.\n"
        "2. Focus on the key requirements that guarantee compliance of the work product "
        f"'**{work_product}**'.\n"
        "3. Explain the necessary inputs the work product should have to achieve compliance.\n"
        "4. Be concise and specific, focusing only on relevant inputs.\n"
        "5. Avoid referencing external IDs or specific clauses; only general mentions of ISO or "
        "ASPICE frameworks are permitted.\n\n"
    )

    prompt += (
        "**Output Format:**\n"
        "- Provide a clear and concise explanation of the necessary inputs for "
        f"'**{work_product}**'.\n"
        "- Highlight how these inputs contribute to compliance with ISO 26262 and ASPICE "
        "standards.\n"
        "- Use structured, professional language suitable for technical documentation.\n\n"
    )

    prompt += (
        "The following ISO 26262 and ASPICE requirements are provided for context:"
        f"\n\n{standards_str}\n\n"
    )

    return prompt


def prompt_gen_content(work_product: str, standards: pd.DataFrame) -> str:
    """
    Generates a prompt for explaining the content requirements for a work product.

    Args:
        work_product (str): The target work product.
        standards (pd.DataFrame): A DataFrame containing ISO 26262 and ASPICE requirements.

    Returns:
        str: A formatted prompt string.
    """

    # Convert standards DataFrame to a formatted string
    standards_str = standards.to_string(index=False)

    # Construct the prompt
    prompt = (
        f"You are provided with the following ISO 26262 and ASPICE requirements:\n\n"
        f"{standards_str}\n\n"
        "**Task Instructions:**\n"
        f"1. Explain the required content for the work product '**{work_product}**' to ensure "
        "compliance with ISO 26262 and ASPICE standards.\n"
        "2. Highlight specific elements, sections, or artifacts that must be included in the "
        "work product.\n"
        "3. Focus on the content necessary to meet compliance and quality expectations.\n"
        "4. Avoid referencing external IDs or clauses; only general mentions of ISO or ASPICE "
        "frameworks are permitted.\n\n"
    )

    # Output Format
    prompt += (
        "**Output Format:**\n"
        f"- Provide a detailed explanation of the required content for '**{work_product}**'.\n"
        "- Focus on relevance to ISO 26262 and ASPICE compliance requirements.\n"
        "- Use structured, professional language suitable for documentation purposes.\n\n"
    )

    return prompt


def prompt_context(context: WorkProductContextModel, work_product) -> list[dict]:
    """
    Generates a list of messages that describe various aspects of a work product in the context 
    of ISO 26262 and Automotive SPICE.
    Args:
        context (WorkProductContextModel): The context model containing descriptions, concepts, 
        and terminology related to the work product.
        work_product (str): The name of the work product.
    Returns:
        list: A list of dictionaries, each representing a message with a role and content, 
        detailing the purpose, content, input, uses, terminology, disambiguation entries, and 
        abbreviations related to the work product.
    """

    messages = []
    message_purpose = {
        "role": "user",
        "content": (
            "**Purpose in ISO 26262:**\n"
            "The purpose of this work product in the context of ISO 26262 is as follows:\n"
            f"{context.description.purpose.purpose_iso}\n"
            "**Purpose in Automotive SPICE:**\n"
            "The purpose of this work product in the context of Automotive SPICE is as follows:"
            f"\n{context.description.purpose.purpose_aspice}\n"
        )
    }
    messages.append(message_purpose)

    message_content = {
        "role": "user",
        "content": (
            "**Content:**\n"
            "This section outlines the necessary content for the work product:\n"
            f"{context.description.content}\n"
        )
    }
    messages.append(message_content)

    message_input = {
        "role": "user",
        "content": (
            "**Input:**\n"
            "This section describes the required inputs for the work product:\n"
            f"{context.description.input}\n"
        )
    }
    messages.append(message_input)

    message_uses = {
        "role": "user",
        "content": (
            "**Uses:**\n"
            "This section explains the uses and applications of the work product:\n"
            f"{context.description.uses}\n"
        )
    }
    messages.append(message_uses)

    # Consolidate Terminology Terms
    terminology_terms = context.concepts.terminology_iso.terms
    if terminology_terms:
        terminology_content = (
            f"In the context of the work product '{work_product}', the following glossary terms "
            "are defined:\n"
        )
        terminology_content += "\n".join(
            [f"- '{term.term}': {term.definition}" for term in terminology_terms]
        )
        messages.append({
            "role": "user",
            "content": terminology_content
        })

    # Consolidate Disambiguation Entries
    disambiguation_entries = context.concepts.disambiguation.entries
    if disambiguation_entries:
        disambiguation_content = (
            f"In the work product '{work_product}', the following disambiguation concepts are "
            "defined:\n"
            "Use these concepts to understand how a single idea can be referred to by different "
            "names in ISO 26262 and ASPICE. "
            "This section also provides examples of their usage, helping to clarify their "
            "application.\n"
            "The concept names serve to unify the different terminologies, ensuring consistency "
            "for the tasks in this work product.\n")

        for entry in disambiguation_entries:
            disambiguation_content += (
                f"\n- Concept: '{entry.concept}'\n"
                f"  - Definition: {entry.definition}\n"
                f"  - Purpose: {entry.purpose}\n"
                f"  - Examples: {', '.join(entry.examples)}\n"
                f"  - Elements: {', '.join(entry.elements)}\n"
                f"  - Example elements: {', '.join(entry.example_elements)}\n"
                f"  - ISO Terminology: {entry.terminology_iso26262}\n"
                f"  - ASPICE Terminology: {entry.terminology_aspice}\n"
            )
        messages.append({
            "role": "user",
            "content": disambiguation_content
        })

    # Consolidate Abbreviations
    abbreviations = context.concepts.abbreviations.abbreviations
    if abbreviations:
        abbreviations_content = (
            f"In the work product '{work_product}', the following abbreviations are defined:\n"
        )
        abbreviations_content += "\n".join(
            [
            f"- '{abbreviation.abbreviation}': {abbreviation.definition}"
            for abbreviation in abbreviations
            ]
        )
        messages.append({
            "role": "user",
            "content": abbreviations_content
        })

    return messages
