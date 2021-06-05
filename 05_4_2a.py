"""
Name: Will
----------------
purpose: wrtie json file 
pre-condition: 
post-condition: 
with Example.html
"""
import json

data = {
    "name": "Jakuta",
    "score": "91",
    "tel": "0912345876"
}

jsonfile = "Example.json"
with open(jsonfile, "w") as fp:
    json.dump(data, fp)