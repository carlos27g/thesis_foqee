"""
Main script for generating checklists, this triggers the whole system.

This script performs the following steps:
1. Creates the input data by calling the `create_input` function.
2. Identifies the different work products from the input data.
3. Generates checklists for each identified work product by calling the `generate_checklists` 
    function.

This script is intended to be run as a standalone program.

"""

import os
import time
from termcolor import colored

from modules.create_input import create_input
from modules.gen_checklist import generate_checklists
from modules.gen_context import gen_context

def main():
    """Main script for FOQEE_CHECKLIST_GENERATOR."""
    start_time = time.time()

    # 1. Create the input
    print(colored("Creating input...", "blue"))
    input_data = create_input()

    # 2. Identify the different work products
    print(colored("Identifying work products...", "blue"))
    work_products = set(input_data['Work Product'])
    for i, work_product in enumerate(work_products, start=1):
        print(f"{i}. {work_product}")

    # 3. Generate the context for each work product
    context = None
    if os.getenv('ADD_WP_CONTEXT') == 'true':
        print(colored("Extracting context for work products...", "blue"))
        context = gen_context(input_data)

    # 4. Generate the checklist for each work product
    print(colored("Generating checklist for work products...", "blue"))
    generate_checklists(input_data, context)

    # Stop the timer
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
