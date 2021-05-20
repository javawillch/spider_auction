"""
Name: Will
----------------
purpose:
pre-condition:
post-condition:
modules need to download: BeautifulSoup
"""
import requests

url = "http://www.google.com"
r = requests.get(url)
if r.status_code == 200:
    print("請求成功")
else:
    print("請求失敗")