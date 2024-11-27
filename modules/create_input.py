import os

import pandas as pd

from termcolor import colored 

def create_input():
    ''' 
    This function reads the Excel file and extracts the required columns from each sheet.
    It combines the extracted data into one DataFrame, splits the 'Work Product' column by '\n',
    and creates new rows for each work product. The function saves the combined DataFrame to an Excel file.
    '''
    # Get the current working directory
    try:
        current_path = os.getcwd()
        file_path = os.path.join(current_path, "datasets", "ThesisInput v2.xlsx")
        print(f"extracting files from {file_path}")
        
        # Define required columns
        required_columns = ['Work Product', 'ID', 'Description']

        # Read the Excel file
        excel_data = pd.read_excel(file_path, sheet_name=None)  

        # Extract all sheets
        sheets = excel_data.keys()
        filtered_data = {}

        for sheet in sheets:
            if sheet == "evi - process requirements":
                continue
            print(f"Processing sheet: {sheet}")

            # Remove entries that are not wished for the LLM
            if "Thesis" in excel_data[sheet].columns:
                excel_data[sheet] = excel_data[sheet][excel_data[sheet]["Thesis"] == "y"]
            
            # Standardize column names in the current sheet and the required columns
            standardized_columns = standardize_columns(excel_data[sheet].columns)
            standardized_required_columns = standardize_columns(required_columns)

            # Check if all required columns are present
            if all(col in standardized_columns for col in standardized_required_columns):
                # Select the columns in the original DataFrame, preserving the original names and order
                filtered_data[sheet] = excel_data[sheet][required_columns]
            else:
                missing_cols = [required_columns[i] for i, col in enumerate(standardized_required_columns) if col not in standardized_columns]
                print(colored(f"Warning: Missing columns {missing_cols} in sheet: {sheet}", "red"))

        # Check if there is any data to combine
        if filtered_data is None:  
            raise "No data to combine."
       
        # Data formating and cleaning
        print("Shape of the dataframe:")

        combined_df = pd.concat(filtered_data.values(), ignore_index=True)
        
        # For development purposes, consider only the two work products:
        if os.getenv("RESTRICT_WORK_PRODUCTS") == "true":
            combined_df = combined_df[
                (combined_df['Work Product']=='Software Requirements Specification') 
                | (combined_df['Work Product']=='Software Architecture Specification')
            ]
        print(f"- Concatenated: {combined_df.shape}")

        combined_df = combined_df.assign(**{
            'Work Product': combined_df['Work Product'].str.split('\n')
        }).explode('Work Product')
        print(f"- Splitting Work Products: {combined_df.shape}")

        combined_df.dropna(subset=['Work Product'], inplace=True)
        print(f"- Removing empty Work Products: {combined_df.shape}")
        
        combined_df['Standard Name'] = None
        combined_df['Version'] = None
        combined_df['Part'] = None
        combined_df['Clause'] = None
        combined_df['Section'] = None
        combined_df['Subsection'] = None
        combined_df['Subsubsection'] = None

        for idx, row in combined_df.iterrows():
            long_id = row['ID']
            if str(long_id).startswith("26262"):
                # ISO ID structure e.g., 26262-6:2018.5.4.3
                long_id_parts = str(long_id).split(':')

                # Split the first part to get '26262' and '6'
                long_id_beginning = long_id_parts[0].split('-')
                combined_df.at[idx, 'Standard Name'] = 'ISO 26262'
                combined_df.at[idx, 'Part'] = long_id_beginning[1]  # '6'

                # Split the second part to get '2018', '5', '4', '3'
                version_and_rest = long_id_parts[1].split('.')
                combined_df.at[idx, 'Version'] = version_and_rest[0]  # '2018'
                combined_df.at[idx, 'Clause'] = version_and_rest[1]   # '5'
                combined_df.at[idx, 'Section'] = version_and_rest[2]  # '4'
                combined_df.at[idx, 'Subsection'] = version_and_rest[3]  # '3'
                if version_and_rest.__len__() > 4:
                    combined_df.at[idx, 'Subsubsection'] = version_and_rest[4]
            else:
                combined_df.at[idx, 'Standard Name'] = 'ASPICE'

        print(colored("Printing first 5 entries:", "green"))
        print(combined_df.head())
        print(combined_df.shape)
        # Save the combined DataFrame to an csv file
        output_file_path = os.path.join(current_path, "datasets", "combined_data.csv")
        combined_df.to_csv(output_file_path, index=False)
        print(colored(f"Dataframe saved to {output_file_path}", "green"))
        return combined_df

    except Exception as e:
        print(colored(f"Error creating input file: {str(e)}", "red"))


def standardize_columns(columns):
    """
    Helper method for create_input.
    Standardize the column names by converting them to lowercase and removing leading/trailing whitespaces
    """
    return [col.strip().lower() for col in columns]
