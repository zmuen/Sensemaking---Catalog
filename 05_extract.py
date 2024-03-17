# -----------------------------------------------
#  5. Data Extraction:
# 
#  Objective: Extract course titles from 
#  the data you cleaned.
# -----------------------------------------------
import json

# Open the JSON file
with open('titles.json') as file:
    titles = json.load(file)

# Print the extracted titles
for title in titles:
    print(title)