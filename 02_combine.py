# -----------------------------------------------
#  2. Data Preparation:
# 
#  Objective: Combine multiple HTML files into 
#  a single document.
# 
#  Tools/Resources: Concatenate HTML text using 
#  python or javascript.
# -----------------------------------------------

import glob, os

# specify local directory
os.chdir("/workspaces/catalog-zmuen")

# concatenate all files into one
with open('data.html', 'w') as outfile:
    for file in glob.glob("data/*.html"):
        with open(file) as infile:
            outfile.write(infile.read())