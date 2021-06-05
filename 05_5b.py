"""
Name: Will
----------------
purpose: download picture
pre-condition: 
post-condition: 
with Example.html
"""
import requests
import re
from bs4 import BeautifulSoup

url = "http://www.google.com.tw"
path = "logo.png"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_a = soup.find(id="hplogo")

match = re.search(r"(/[^/#?]+)+\.(?:jpg|gif|png)", str(tag_a))
print(match.group())
url = url + str(match.group())
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb') as fp:
        for chunk in response:
            fp.write(chunk)
    print("檔案下載完畢")
else:
    print("錯誤！請求失敗")