#Imports OS and Regular Expression
import os
import re
from datetime import datetime

#Defining Function. 
def filter_log(input_file_path, output_directory):
    # Create a directory to store filtered logs if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a unique output file based on the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = os.path.join(output_directory, f"filtered_logs_{current_datetime}.log")

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # Use regular expression to extract the status code
            match = re.search(r'\s(\d{3})\s', line)
            
            # Check if the match is found and the status code is not 200
            if match and match.group(1) != '200':
                output_file.write(line)

    return output_file_path

if __name__ == "__main__":
    input_log_file = "D:\kpmg-task2\kpmg_assesment_2\Challenge_3\web_logs_2024_01_24.log"
    output_directory = "D:\kpmg-task2\kpmg_assesment_2\Challenge_3"

    filtered_file_path = filter_log(input_log_file, output_directory)

    print(f"Filtering completed. Non-200 requests written to {filtered_file_path}")
