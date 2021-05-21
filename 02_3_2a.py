"""
Name: Will
----------------
purpose: get further error msg
pre-condition: 
post-condition: 
"""
import requests

url = "http://www.google.com/404"

r = requests.get(url)
print(r.status_code)
print(r.status_code == requests.codes.all_good)
print('------------------------')
print(r.raise_for_status())