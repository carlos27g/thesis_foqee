from termcolor import colored 

from modules.create_input import create_input
from modules.gen_checklist import generate_checklists

import time


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
