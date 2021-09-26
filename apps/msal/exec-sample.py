# Use this file to examine JSON data file

import json

with open("me-todo-lists.json", "r", encoding="utf-8") as sample_data_file:
    json_data = json.load(sample_data_file)

