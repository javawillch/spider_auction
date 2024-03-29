"""
Name: Will
----------------
purpose: read json file from google
pre-condition: 
post-condition: 
with Example.html
"""
import json
import requests

url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
jsonfile = "Book.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)
with open(jsonfile, 'w') as fp:
    json.dump(json_data, fp)