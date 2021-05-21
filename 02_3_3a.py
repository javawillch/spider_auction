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
print(r.headers)
print(r.headers.get('X-Frame-Options'))
print(r.headers.get('X-XSS-Protection'))
print(r.headers.get('Content-Encoding'))
print(r.headers.get('Content-Type'))
print(r.headers.get('Cache-Control'))
print(r.headers.get('Date'))
print(r.headers.get('Server'))
print(r.headers.get('Content-Length'))