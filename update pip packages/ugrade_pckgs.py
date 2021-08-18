# Upgrading all python packages

# Updating Python Packages On Windows Or Linux

# 1-Output a list of installed packages into a requirements file (requirements.txt):

# pip freeze > requirements.txt

# 2- Edit requirements.txt, and replace all ‘==’ with ‘>=’. Use the ‘Replace All’ command in the editor.

# 3 - Upgrade all outdated packages

# pip install -r requirements.txt --upgrade 