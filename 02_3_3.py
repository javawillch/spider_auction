"""
Name: Will
----------------
purpose: get the headers from response
pre-condition: 
post-condition: 
"""
import requests

url = "http://www.google.com"
r = requests.get(url)

# print(r.headers)
print(r.headers['Content-Type'])
print(r.headers['Cache-Control'])
print(r.headers['Date'])
print(r.headers['Server'])
print(r.headers['Content-Length'])
# print(r.headers['Set-Cookie'])
