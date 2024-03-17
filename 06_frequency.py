# -----------------------------------------------
#  6. Word Frequency Analysis:
# 
#  Objective: Perform a word frequency count 
#  on the course titles.
# 
#  Tools/Resources: You can use a “map reduce” 
#  style word counting approach.
# -----------------------------------------------

from collections import Counter, defaultdict
import pandas as pd
import json
import re

with open('titles.json') as file:
    titles = json.load(file)

# Filter out conjunctions and remove special characters
def clean_word(word):
    word = re.sub(r'[^A-Za-z\s]', '', word) 
    word = word.strip() 
    if word.lower() == 'the' or word[0].islower():
        return ''
    return word

# Group the courses by department index
courses_by_dep = defaultdict(list)
for title in titles:
    dep_index = title.split()[1]
    course_name = title.split(': ')[1]
    words = course_name.split()
    words = [clean_word(word) for word in words]
    words = [word for word in words if word]
    courses_by_dep[dep_index].extend(words)  # Extend the list of words for the department

data = []

# Iterate over department index and words to collect frequencies
for dep_index, words in courses_by_dep.items():
    frequencies = Counter(words)
    for word, count in frequencies.items():
        data.append({'Department Index': dep_index, 'Word': word, 'Frequency': count})

df = pd.DataFrame(data)
df.to_csv('department_word_frequencies.csv', index=False)