"""
Name: Will
----------------
purpose: change encoding setting
pre-condition: 
post-condition: 
"""
import requests

url = "http://httpbin.org/user-agent"
r = requests.get(url)
print(r.text)
print(type(r.text))
print("-----------------------")
print(r.json())
print(type(r.json))