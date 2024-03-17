# -----------------------------------------------
#  8. Export a Clean Formatted Dataset
#  of the Entire University Catalog:
# -----------------------------------------------

import json
import re
import pandas as pd

with open('/workspaces/catalog-zmuen/titles.json') as file:
    titles = json.load(file)

# Function to extract department index, course number, and course name from title
def extract_course_info(title):
    parts = title.split(': ')
    department_index, course_number = parts[0].split()[1], parts[0].split()[2]
    course_name = parts[1]
    return department_index, course_number, course_name

# Clean and format course titles data
clean_data = []
for title in titles:
    department_index, course_number, course_name = extract_course_info(title)
    clean_data.append({
        'Department Index': department_index,
        'Course Number': course_number,
        'Course Name': course_name
    })

# Create DataFrame from clean data
df = pd.DataFrame(clean_data)

# Export DataFrame to CSV
df.to_csv('/workspaces/catalog-zmuen/export/boston_university_catalog.csv', index=False)

# Document the structure of the dataset, including column descriptions, data types, and assumptions
dataset_structure = {
    'Department Index': 'string',
    'Course Number': 'integer',
    'Course Name': 'string',
}

dataset_assumptions = {
    'Assumption 1': 'Conjunctions have high frequencies but are irrelevant for analysis.',
    'Assumption 2': 'Calculating Word frequencies within each department could better analyze topics or themes emphasized under the context.'
}

# Save the dataset structure and assumptions to a text file
with open('/workspaces/catalog-zmuen/export/dataset_structure.txt', 'w') as f:
    f.write('Dataset Structure:\n')
    for column, data_type in dataset_structure.items():
        f.write(f'{column}: {data_type}\n')
    f.write('\nAssumptions:\n')
    for assumption, description in dataset_assumptions.items():
        f.write(f'{assumption}: {description}\n')
