"""
I need a script to go through all csv files and edit names.  The user will input the current name, the desired change name,
and the script will report back how many entries it found, then ask to confirm the change.
"""

"""
Here's what chatGPT came up with...
"""

import os
import csv

def find_and_replace_in_csv(folder_path, search_term, replace_term):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            updated_rows = []

            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    updated_row = [cell.replace(search_term, replace_term) for cell in row]
                    updated_rows.append(updated_row)

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(updated_rows)

            print(f"Updated entries in {filename}")

if __name__ == "__main__":
    folder_path = "csv input"
    search_term = "1A WOODWARD GRANGER AIDEN TOPALOVICH 2024"
    replace_term = "1A WOODWARD GRANGER AIDEN TOPOLAVICH 2024"

    find_and_replace_in_csv(folder_path, search_term, replace_term)
