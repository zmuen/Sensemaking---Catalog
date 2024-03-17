# -----------------------------------------------
#   3. Data Parsing:
# 
#   Objective: Parse course data leveraging
#   HTML elements structure.
# -----------------------------------------------

from bs4 import BeautifulSoup
import json

# save titles in json format
def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data saved to', file)

# get titles
f = open('data.html', 'r')
html = f.read()
html = html.replace('\n', ' ').replace('\r', '')
soup = BeautifulSoup(html, 'html.parser')
def has_strong_tag(tag):
    return tag.name == 'a' and tag.strong is not None

results = soup.find_all(has_strong_tag)
titles = [result.strong.text for result in results]

# create titles set
titles = set()
for result in results:
    title = result.strong.text
    if title not in titles:
        titles.add(title)

# convert titles set back to list
titles = list(titles)

# save titles to json
store_json(titles, 'titles.json')
