"""
Name: Will
----------------
purpose: get cookies
pre-condition: 
post-condition: 
"""
import requests

url = "http://httpbin.org/cookies"

cookies = dict(name='Elon Musk')
r = requests.get(url, cookies = cookies)
print(r.text)
print(r.cookies.get('name'))