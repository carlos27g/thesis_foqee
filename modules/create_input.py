"""
Creates a CSV with the ISO 26262 and Automotive SPICE standards.

Functions:
    create_input():
    result to a CSV file for further analysis. Returns a pandas DataFrame with the 
    processed data.

    extract_required_columns(excel_data, required_columns):
    Extracts required columns from each sheet in the Excel data. Skips sheets that do not contain 
    the required columns and logs warnings for missing columns. Returns a dictionary of filtered 
    data from each sheet.

    process_combined_data(df):
    Filters work products based on environment variable settings and adds metadata columns 
    for standard-specific information. Returns the processed DataFrame.

    parse_iso_id(df, idx, long_id):
    Parses ISO 26262 ID and updates the DataFrame with extracted metadata. Extracts and assigns 
    values for standard name, version, part, clause, section, subsection, and subsubsection. 
    Returns the updated DataFrame.

    standardize_columns(columns):
    Returns a list of standardized column names.
"""

import os
import pandas as pd
from termcolor import colored

def create_input():
    """
    Reads an Excel file containing combined standards data from ASPICE and ISO 26262 across 
    multiple sheets. Extracts the required columns, processes the data, and saves the combined 
    result to a CSV file for further analysis.

    Args:
    None

    Returns:
    pd.DataFrame: 
        A combined and processed pandas DataFrame containing the extracted and cleaned data 
        from all sheets in the Excel file, specifically related to the ASPICE and ISO 26262 
        standards.
    """

    try:
        current_path = os.getcwd()
        file_path = os.path.join(current_path, "datasets", "ThesisInput v2.xlsx")
        print(f"Extracting files from {file_path}")

        # Required columns to extract
        required_columns = ['Work Product', 'ID', 'Description']

        # Read the Excel file and extract sheets
        excel_data = pd.read_excel(file_path, sheet_name=None)
        filtered_data = extract_required_columns(excel_data, required_columns)

        # Combine data from all sheets
        combined_df = pd.concat(filtered_data.values(), ignore_index=True)
        combined_df = process_combined_data(combined_df)

        # Save the combined DataFrame to a CSV file
        output_file_path = os.path.join(current_path, "datasets", "combined_data.csv")
        combined_df.to_csv(output_file_path, index=False)
        print(colored(f"Dataframe saved to {output_file_path}", "green"))

        return combined_df

    except FileNotFoundError as e:
        raise FileNotFoundError("Error: File not found. Please check the file path.") from e
    except ValueError as e:
        raise ValueError(
            "Error: Failed to read Excel file. The file may be corrupted or unsupported.") from e


def extract_required_columns(excel_data, required_columns):
    """
    Extracts required columns from each sheet in the Excel data.

    Args:
        excel_data (dict): All sheets from the Excel file.
        required_columns (list): List of required column names.

    Returns:
        dict: Filtered data from each sheet containing the required columns.
    """
    filtered_data = {}
    for sheet, data in excel_data.items():
        if sheet == "evi - process requirements":
            continue
        print(f"Processing sheet: {sheet}")

        if "Thesis" in data.columns:
            data = data[data["Thesis"] == "y"]

        standardized_columns = standardize_columns(data.columns)
        standardized_required_columns = standardize_columns(required_columns)

        if all(col in standardized_columns for col in standardized_required_columns):
            filtered_data[sheet] = data[required_columns]
        else:
            missing_cols = [
                required_columns[i] for i, col in enumerate(standardized_required_columns)
                if col not in standardized_columns
            ]
            print(colored(f"Warning: Missing columns {missing_cols} in sheet: {sheet}", "red"))
    return filtered_data


def process_combined_data(df):
    """
    Processes the combined DataFrame by splitting, filtering, and adding metadata columns.

    Args:
        df (pd.DataFrame): Combined DataFrame.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    if os.getenv("RESTRICT_WORK_PRODUCTS") == "true":
        df = df[
            (df['Work Product'] == 'Software Requirements Specification') |
            (df['Work Product'] == 'Software Architecture Specification')
        ]

    df = df.assign(**{'Work Product': df['Work Product'].str.split('\n')}).explode('Work Product')
    df.dropna(subset=['Work Product'], inplace=True)

    # Add metadata columns
    metadata_columns = ['Standard Name', 'Version', 'Part', 'Clause', 'Section', 'Subsection',
                        'Subsubsection']
    for col in metadata_columns:
        df[col] = None

    for idx, row in df.iterrows():
        long_id = row['ID']
        if str(long_id).startswith("26262"):
            df = parse_iso_id(df, idx, long_id)
        else:
            df.at[idx, 'Standard Name'] = 'ASPICE'

    print(colored("First 5 entries of the processed DataFrame:", "green"))
    print(df.head())
    return df


def parse_iso_id(df, idx, long_id):
    """
    Parses ISO 26262 ID and updates the DataFrame with extracted metadata.

    Args:
        df (pd.DataFrame): DataFrame to update.
        idx (int): Index of the current row.
        long_id (str): Long ID string.

    Returns:
        pd.DataFrame: Updated DataFrame with metadata.
    """
    long_id_parts = long_id.split(':')
    long_id_beginning = long_id_parts[0].split('-')
    version_and_rest = long_id_parts[1].split('.')

    df.at[idx, 'Standard Name'] = 'ISO 26262'
    df.at[idx, 'Part'] = long_id_beginning[1]
    df.at[idx, 'Version'] = version_and_rest[0]
    df.at[idx, 'Clause'] = version_and_rest[1]
    df.at[idx, 'Section'] = version_and_rest[2]
    df.at[idx, 'Subsection'] = version_and_rest[3] if len(version_and_rest) > 3 else None
    df.at[idx, 'Subsubsection'] = version_and_rest[4] if len(version_and_rest) > 4 else None

    return df


def standardize_columns(columns):
    """
    Standardizes column names by converting to lowercase and stripping whitespace.

    Args:
        columns (list): Original column names.

    Returns:
        list: Standardized column names.
    """
    return [col.strip().lower() for col in columns]
