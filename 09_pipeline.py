# -----------------------------------------------
#  9. Data pipeline:
# 
#  Write a program that automates the 
#  sequential execution of previously created 
#  script files, ensuring that each script 
#  runs to completion before the next begins. 
#  This program aims to streamline the 
#  generation of outputs from all your 
#  previous files, consolidating the 
#  results into one sequence.
# -----------------------------------------------

import subprocess

# List of script files to execute in order
script_files = [
    "/workspaces/catalog-zmuen/01_pull.py",
    "/workspaces/catalog-zmuen/02_combine.py",
    "/workspaces/catalog-zmuen/03_parse.py",
    "/workspaces/catalog-zmuen/04_analyze.py",
    "/workspaces/catalog-zmuen/05_report.py",
    "/workspaces/catalog-zmuen/06_export.py",
    "/workspaces/catalog-zmuen/07_visualization.py"
    "/workspaces/catalog-zmuen/08_export.py"
]

# Execute each script file in order
for script_file in script_files:
    subprocess.run(["python", script_file])