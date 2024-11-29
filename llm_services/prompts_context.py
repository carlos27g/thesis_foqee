from llm_services.models_context import WorkProductContextModel

# ----------------- For Contextualization of WP ----------------- #
def prompt_glossary_definition(term, definition) -> str:
    prompt = (
        f"You are tasked with defining the term '**{term}**' within the context of the ISO 26262 standard for functional safety in automotive systems.\n\n"
        f"**Task Instructions:**\n"
        f"1. **Provide a clear and precise definition** of '**{term}**' based on its use within ISO 26262.\n"
        f"2. **Focus on automotive safety** to ensure the definition is relevant to ISO 26262 applications.\n"
        f"3. **Extract any essential details** from the provided content to form a complete understanding of the term, using domain knowledge as needed.\n\n"
        f"**Provided Content:**\n"
        f"'{definition}'\n\n"
        f"**Note:** There is no need to include an introduction that repeats the term's name or the context of ISO 26262.\n"
    )
    return prompt

def prompt_terminology_iso_extraction(work_product, terminology_iso) -> str:
    prompt = (
        f"You are provided with a list of terminology from the ISO 26262 standard framework. Your task is to select terms directly relevant to the work product '**{work_product}**'.\n\n"
        f"**Task Instructions:**\n"
        f"**Focus on Direct Relevance:** Identify only those terms that explicitly relate to the creation, definition, or management of the work product '**{work_product}**'.\n"
        f"   - Examples of directly relevant terms include concepts that describe work product structure, content, management processes, or evaluation criteria.\n"
        f"   - Avoid including terms that are only tangentially related, such as general processes, unrelated testing methods, or implementation-specific details.\n\n"
        f"**Output Format:**\n"
        f"Please return the extracted terms in the following format:\n"
        f"- A list of objects, where each object includes:\n"
        f"  - 'id': The ID of the term in the glossary\n"
        f"  - 'term': The term in the glossary\n"
        f"  - 'definition': The description of the term in the glossary\n"
        f"If no relevant term is found, return nothing.\n\n"
        f"**Note:** Use the function 'TermListModel' to return the output. Ensure all structured data is passed into the function, and no other action is taken.\n"
        f"**Note:** Remove all references to external IDs or clauses from the definitions. Only mentions of ISO or ASPICE as frameworks are permitted.\n\n"
        f"**Terminology List:**\n"
    )
    for i, item in enumerate(terminology_iso):
        # Access each field within the dictionary
        term = item.get("term")
        definition = item.get("definition")
        # Append each entry to the prompt
        prompt += (
            f"  - **Term {i}:** {term}\n"
            f"  - **Definition:** {definition}\n\n"
        )
    return prompt
def prompt_disambiguation_extraction(work_product, disambiguations) -> str:
    prompt = (
        f"**Introduction**\n"
        f"You are an expert in ISO 26262 and ASPICE guidelines. I have a disambiguation table where each row represents a concept and its attributes, including its terminology in ISO 26262 and ASPICE. These concepts help distinguish terms, definitions, and purposes across the frameworks.\n"
        f"Some rows may not contain information for ISO 26262 or ASPICE terminology, which indicates either:\n"
        f"1. The concept is not explicitly mentioned or used in that framework, or\n"
        f"2. The same name is used across frameworks.\n\n"
        f"Your task is to filter the relevant concepts for the work product: {work_product}. Use the provided data to determine the relevance of each concept.\n\n"
        
        f"**Tasks**\n"
        f"1. Review the disambiguation table row by row.\n"
        f"2. Identify concepts that meet any of the following criteria:\n"
        f"   - Have explicit terminology linked to the requested work product: {work_product}, in the context of ISO 26262 and ASPICE.\n"
        f"   - Are fundamental or commonly used across frameworks, even if no explicit connection is visible.\n"
        f"   - Use the other attributes to assess if they are linked to the work product.\n"
        f"3. Exclude concepts that are irrelevant to the requested {work_product} unless they are widely applicable.\n"
        f"**Note:** Use the function 'DisambiaguationModel' to process the structured JSON output. Ensure all structured data is passed into the function, and no other action is taken.\n"
        f"**Note:** If any of the parameters of DisambiguationModel is not available, return 'NA'. \n"
        f"**Data**\n"
        f"Here is the disambiguation table:\n"
    )
    # Iterate through disambiguations and format them
    for row in disambiguations:
        prompt += (
            f"{'{' + '  '}\n"
            f'  "concept": "{row.get("concept")}",\n'
            f'  "definition": "{row.get("definition", "NA")}",\n'
            f'  "purpose": "{row.get("purpose", "NA")}",\n'
            f'  "examples": {row.get("examples", "NA")},\n'
            f'  "elements": {row.get("elements", "NA")},\n'
            f'  "example_elements": {row.get("example_elements", "NA")},\n'
            f'  "terminology_iso26262": "{row.get("terminology_iso26262", "NA")}",\n'
            f'  "terminology_aspice": "{row.get("terminology_aspice", "NA")}"\n'
            f"{'}'}\n\n"
        )
    
    return prompt
def prompt_abbreviations_extraction(work_product, abbreviations) -> str:
    prompt = (
        f"You are tasked with filtering the abbreviations relevant to the work product '**{work_product}**' from the provided list.\n\n"
        f"**Task Instructions:**\n"
        f"1. **Review the list of abbreviations** to identify those that are directly related to the work product '**{work_product}**'.\n"
        f"2. **Extract the relevant abbreviations** and provide a brief explanation of each abbreviation's meaning.\n"
        f"**Note:** Use the function 'AbbreviationListModel' to process the structured JSON output. Ensure all structured data is passed into the function, and no other action is taken.\n"
        f"**Note:** Remove all references to external IDs or clauses from the definitions. Only mentions of ISO or ASPICE as frameworks are permitted.\n\n"
        f"**Abbreviations List:**\n"
    )
    for item in abbreviations:
        prompt += (
        f"- **Abbreviation:** {item['abbreviation']}\n"
        f"- **Definition:** {item['definition']}\n\n"
        )
    return prompt
def prompt_gen_purpose(work_product):
    prompt = (
        f"As an auditor specializing in ISO 26262 and ASPICE compliance, "
        f"provide a clear and concise explanation of the purpose of the work product '{work_product}' "
        f"in the context of these standards, focusing on its role in ensuring compliance and quality."
    )
    return prompt

def prompt_gen_content(work_product, standards):
    standards_str = standards.to_string(index=False)
    prompt = (
        f"Based on the following ISO 26262 and ASPICE requirements:\n\n{standards_str}\n\n"
        f"Explain what necessary content the '{work_product}' should include to comply with these standards. "
        f"Be concise and focus on the key requirements.\n"
        f"**Note:** Remove all references to external IDs or clauses from the definitions. Only mentions of ISO or ASPICE as frameworks are permitted.\n\n"
    )
    return prompt

def prompt_gen_input(work_product, standards):
    standards_str = standards.to_string(index=False)
    prompt = (
        f"Based on the following ISO 26262 and ASPICE requirements:\n\n{standards_str}\n\n"
        f"Focus on the key requirements that guarantee compliance of the '{work_product}' with these standards. "
        f"Explain the necessary inputs that the '{work_product}' should have. "
        f"Be concise and specific.\n"
        f"**Note:** Remove all references to external IDs or clauses from the definitions. Only mentions of ISO or ASPICE as frameworks are permitted.\n\n"
    )
    return prompt

def prompt_gen_uses(work_product, standards):
    standards_str = standards.to_string(index=False)
    prompt = (
        f"Based on the following ISO 26262 and ASPICE requirements:\n\n{standards_str}\n\n"
        f"Explain the use cases for the '{work_product}' and how this work product aids in documentation. "
        f"Focus on key points and be concise."
        f"**Note:** Remove all references to external IDs or clauses from the definitions. Only mentions of ISO or ASPICE as frameworks are permitted.\n\n"
    )
    return prompt

def prompt_context(context, work_product):
    messages = []
    message_purpose = {
        "role": "user",
        "content": (
            f"**Purpose in ISO 26262:**\n"
            f"The purpose of this work product in the context of ISO 26262 is as follows:\n{context.description.purpose.purpose_iso}\n"
            f"**Purpose in Automotive SPICE:**\n"
            f"The purpose of this work product in the context of Automotive SPICE is as follows:\n{context.description.purpose.purpose_aspice}\n"
        )
    }
    messages.append(message_purpose)

    message_content = {
        "role": "user",
        "content": (
            f"**Content:**\n"
            f"This section outlines the necessary content for the work product:\n{context.description.content}\n"
        )
    }
    messages.append(message_content)

    message_input = {
        "role": "user",
        "content": (
            f"**Input:**\n"
            f"This section describes the required inputs for the work product:\n{context.description.input}\n"
        )
    }
    messages.append(message_input)

    message_uses = {
        "role": "user",
        "content": (
            f"**Uses:**\n"
            f"This section explains the uses and applications of the work product:\n{context.description.uses}\n"
        )
    }
    messages.append(message_uses)

    # Consolidate Terminology Terms
    terminology_terms = context.concepts.terminology_iso.terms
    if terminology_terms:
        terminology_content = f"In the context of the work product '{work_product}', the following glossary terms are defined:\n"
        terminology_content += "\n".join([f"- '{term.term}': {term.definition}" for term in terminology_terms])
        messages.append({
            "role": "user",
            "content": terminology_content
        })

    # Consolidate Disambiguation Entries
    disambiguation_entries = context.concepts.disambiguation.entries
    if disambiguation_entries:
        disambiguation_content = (
            f"In the work product '{work_product}', the following disambiguation concepts are defined:\n"
            f"Use these concepts to understand how a single idea can be referred to by different names in ISO 26262 and ASPICE. "
            f"This section also provides examples of their usage, helping to clarify their application.\n"
            f"The concept names serve to unify the different terminologies, ensuring consistency for the tasks in this work product.\n")

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
        abbreviations_content = f"In the work product '{work_product}', the following abbreviations are defined:\n"
        abbreviations_content += "\n".join([f"- '{abbreviation.abbreviation}': {abbreviation.definition}" for abbreviation in abbreviations])
        messages.append({
            "role": "user",
            "content": abbreviations_content
        })

    return messages

