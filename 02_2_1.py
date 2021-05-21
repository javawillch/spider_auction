"""
Name: Will
----------------
purpose:
pre-condition:
post-condition:
"""
import requests

url = "http://www.google.com"
r = requests.get(url)
print(r.status_code)
