"""
Name: Will
----------------
purpose: json 
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

json_str = json.dumps(data)
print(json_str)
data2 = json.loads(json_str)
print(data2)