"""
Name: Will
----------------
purpose: check if the request is success
pre-condition: 
post-condition: 
"""
import requests

url1 = "http://www.google.com"
url2 = "http://www.google.com/404"

r = requests.get(url1)
print(r.status_code)
print(r.status_code == requests.codes.ok)
print(r.status_code == requests.codes.all_good)

r = requests.get(url2)
print(r.status_code)
print(r.status_code == requests.codes.ok)