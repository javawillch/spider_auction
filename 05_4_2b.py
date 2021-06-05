"""
Name: Will
----------------
purpose: read json file 
pre-condition: 
post-condition: 
with Example.html
"""
import json

jsonfile = "Example.json"
with open(jsonfile, "r") as fp:
    data = json.load(fp)

json_str = json.dumps(data)
print(json_str)