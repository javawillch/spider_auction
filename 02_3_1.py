"""
Name: Will
----------------
purpose: change encoding setting
pre-condition: 
post-condition: 
"""
import requests

## "http://hueyanchen.myweb.hinet.net/test.html"  url already fail
url = "https://httpbin.org/get"
r = requests.get(url)
print(r.text)
print(r.encoding)

r = requests.get(url)
r.encoding = 'utf-8'
print(r.text)
print(r.encoding)
