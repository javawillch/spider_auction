"""
Name: Will
----------------
purpose: use test website to simulate post request process 
pre-condition: 
post-condition: 
"""
import requests

url = "https://httpbin.org/post"
post_data = {'name': '紅寶石1.5ct', 'price': 10000}
r = requests.post(url, data = post_data)
print(r.text)