"""
Main script for generating checklists, this triggers the whole system.

This script performs the following steps:
1. Creates the input data by calling the `create_input` function.
2. Identifies the different work products from the input data.
3. Generates checklists for each identified work product by calling the `generate_checklists` 
   function.


Modules:
    time: Provides various time-related functions.
    modules.create_input: Contains the `create_input` function to generate input data.
    modules.gen_checklist: Contains the `generate_checklists` function to generate checklists.
    termcolor: Provides functions to print colored text in the terminal.

Execution:
    This script is intended to be run as a standalone program.

"""
import time

from termcolor import colored

from modules.create_input import create_input
from modules.gen_checklist import generate_checklists


start_time = time.time()

# 1. Create the input
print(colored("Creating input...", "blue"))
input_data = create_input()

# 2. Identify the different work products
print(colored("Identifying work products...", "blue"))
work_products = set(input_data['Work Product'])
for i, work_product in enumerate(work_products, start=1):
    print(f"{i}. {work_product}")

# 3. Generate the checklist for each work product
print(colored("Generating checklist for work products...", "blue"))
generate_checklists(input_data)

# Stop the timer
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
