import csv
import json

# Define the input and output file paths
csv_file_path = 'data/forestfires.csv'
json_file_path = 'data/forestfires.json'

# Read the CSV file and convert to a list of dictionaries
forest_fires = []

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Convert numeric values from strings to appropriate types
        for key, value in row.items():
            try:
                if key in ['X', 'Y']:
                    row[key] = int(value)
                elif key in ['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']:
                    row[key] = float(value)
            except ValueError:
                # Keep as string if conversion fails
                pass
        forest_fires.append(row)

# Write to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(forest_fires, json_file, indent=2)

print(f"Conversion completed successfully.")
print(f"CSV data from '{csv_file_path}' has been converted to JSON and saved to '{json_file_path}'.")
print(f"Total records: {len(forest_fires)}") 