def create_dict_iso_terminology(iso_terminology_df):
    """
    Iterate through the rows of a DataFrame and create a dictionary for each row.

    Args:
    - dataframe (pd.DataFrame): DataFrame containing the table data from the ISO terminology table.

    Returns:
    - terminology_list (list): List of dictionaries representing each row.
    """
    terminology_list = []
    for _, row in iso_terminology_df.iterrows():
        # Construct the dictionary for each row
        terminology_dict = {
            "id": row.get("ID"),
            "term": row.get("Term"),
            "definition": row.get("Definition"),
            "notes": row.get("Notes")
        }
        # Append the dictionary to the list
        terminology_list.append(terminology_dict)
    return terminology_list


def create_dict_disambiguation(disambiguation_df):
    """
    Iterate through the rows of a DataFrame and create a dictionary for each row.

    Args:
    - dataframe (pd.DataFrame): DataFrame containing the table data from the disambiguation table.

    Returns:
    - concepts_list (list): List of dictionaries representing each row.
    """
    concepts_list = []
    for _, row in disambiguation_df.iterrows():
        # Construct the dictionary for each row
        concept_dict = {
            "concept": row.get("Concept"),
            "definition": row.get("is a", ""),
            "purpose": row.get("aiming at", ""),
            "examples": [example.strip() for example in str(row.get("Examples", "")).split(";") if example.strip()],
            "elements": [element.strip() for element in str(row.get("Its elements are", "")).split(";") if element.strip()],
            "example_elements": [example.strip() for example in str(row.get("Example elements", "")).split(";") if example.strip()],
            "terminology_iso26262": row.get("Terminology ISO26262", ""),
            "terminology_aspice": row.get("Terminology in Automotive SPICE", "")
        }
        # Append the dictionary to the list
        concepts_list.append(concept_dict)
    return concepts_list


def create_dict_abbreviations(abbreviations_df):
    """
    Iterate through the rows of a DataFrame and create a dictionary for each row.

    Args:
    - dataframe (pd.DataFrame): DataFrame containing the table data from the abbreviations table.

    Returns:
    - abbreviations_list (list): List of dictionaries representing each row.
    """
    abbreviations_list = []
    for _, row in abbreviations_df.iterrows():
        # Construct the dictionary for each row
        abbreviation_dict = {
            "abbreviation": row.get("Abbreviation"),
            "definition": row.get("Definition"),
        }
        # Append the dictionary to the list
        abbreviations_list.append(abbreviation_dict)
    return abbreviations_list