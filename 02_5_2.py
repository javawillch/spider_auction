"""
Name: Will
----------------
purpose: Save as a txt file
pre-condition: 
post-condition: 
"""
import requests

url = "http://www.google.com"
r = requests.get(url)

fp = open("test.txt", "w", encoding="utf-8")
fp.write(r.text)
print("寫入檔案test.txt..")
fp.close()