import csv
import pandas as pd

runner_data = pd.read_csv("all_players.csv",header=0)

# List of items to match
items_to_match = [
    'DOWLING',
    'JOHNSTON',
    'ANKENY',
    'NORWALK',
    'CEDAR FALLS',
    'WEST DES MOINES VALLEY',
    'IOWA CITY HIGH',
    'CR KENNEDY',
    'PLEASANT VALLEY',
    'SOUTHEAST POLK',
    'WAUKEE NW',
    'DUBUQUE HEMPSTEAD',
    'SIOUX CITY NORTH',
    'CR PRAIRIE',
    'URBANDALE'
    ]  # Add your items here

# List of items to exclude
items_to_exclude = [
    'ANKENY CENTENNIAL',
    'ANKENY CHRISTIAN',
    ]  # Add your items here

print(items_to_match)

# Input CSV file
input_csv_filename = 'all_players.csv'

# Output CSV file
output_csv_filename = 'race_prediction.csv'

# Filter items from the list that are also found in the extracted items
matching_items = []

#find matches
for runner in runner_data['handle']:
    for match_item in items_to_match:
        if match_item in runner:
            matching_items.append(runner)

#remove excluded
for excluded_item in items_to_exclude:
    for matched_item in matching_items:
        if excluded_item in matched_item:
            matching_items.remove(matched_item)
    

# Write the matching items to the output CSV
with open(output_csv_filename, 'w', newline='') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)
    csv_writer.writerow(['handle'])
    for item in matching_items:
        csv_writer.writerow([item])

print("Output CSV file created with matching items.")
