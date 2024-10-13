import os
import importlib

import tasks.t_2_1

# Path to the folder
folder_path = 'tasks'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.py') and filename != '__init__.py':
        # Remove the .py extension to get the module name
        module_name = filename[:-3]

        # Import the module
        importlib.import_module(f"{folder_path}.{module_name}")

if __name__ == '__main__':
    user_input = input("Enter a number (1-16) to choose an option: ")
    match user_input:
        case '1':
            tasks.t_2_1.task()
        case _:
            print("Invalid")
