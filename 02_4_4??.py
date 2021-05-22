"""
Name: Will
----------------
purpose: Auth information
pre-condition: 
post-condition: 
"""
import requests

url = "https://api.github.com/user"
r = requests.get(url, auth = ('javawillch@gmail.com', 'redblue0413'))

if r.status_code == requests.codes.all_good:
    print(r.headers['Content-Type'])
    print(r.json())
else:
    print('HTTP請求錯誤')
    print(r.raise_for_status()) 
    # HTTPError: 401 Client Error: Unauthorized for url: https://api.github.com/user