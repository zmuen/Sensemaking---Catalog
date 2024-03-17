# -----------------------------------------------
#   4. Data Cleaning:
# 
#   Objective: Clean and preprocess the 
#   extracted data for analysis.
# -----------------------------------------------

import re

# Read the contents of the titles.json file
with open('titles.json', 'r') as file:
    data = file.read()

# Clean the data using regular expressions
cleaned_data = re.sub(r'\W+', ' ', data)

# Save the cleaned data back to the json file
with open('titles_cleaned.json', 'w') as file:
    file.write(cleaned_data)
