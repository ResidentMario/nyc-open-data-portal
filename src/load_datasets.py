"""
Small command-line script which uses the raw JSON endpoint to query for every endpoint in the chosen domain. Saves
the raw output to disc locally.
"""

import json

from src.portal import get_datasets

domain = input("Your Socrata domain URI: ")
key = input("Your Socrata application token: ")
filename = input("The filename you want to save this output to: ")
datasets = get_datasets(domain, key)
with open(filename, "w") as f:
    f.write(json.dumps(datasets, indent=4))