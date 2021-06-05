"""
Name: Will
----------------
purpose: download picture
pre-condition: 
post-condition: 
with Example.html
"""
import requests

url = "https://miro.medium.com/max/708/1*ifSob78knBe5rME04WHftg.png"
path = "miki.png"
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb')as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖片已經下載")
else:
    print("錯誤！請求失敗")