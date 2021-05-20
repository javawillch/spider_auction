"""
Name: Will
----------------
purpose: use test website to simulate get request process
pre-condition: 
post-condition: http://httpbin.org/get?name=%E8%B5%A4%E9%9D%92&Score=95 (u will get a url which have encoded.)
"""
import requests

url = "http://httpbin.org/get"
url_params = {'name': '赤青','Score': 95}
r = requests.get(url, params = url_params)
print(r.url)
