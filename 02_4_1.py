"""
Name: Will
----------------
purpose: get cookies
pre-condition: 
post-condition: 
"""
import requests

url = "http://example.com"
url1 = "http://www.google.com"

r = requests.get(url1)
v = r.cookies ##.get("cookie_name")
print(v)
print(r.cookies.get("cookie_name")) ### -> None
print(r.cookies["cookie_name"])     ### -> Error