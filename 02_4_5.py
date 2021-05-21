"""
Name: Will
----------------
purpose: timeout handle
pre-condition: 
post-condition: 
"""
import requests

try:
    url = "http://www.google.com"
    r = requests.get(url, timeout = 0.03) # -> 故意設短產生Error
    print(r.text)
except requests.exceptions.Timeout as ex:
    print("錯誤：HTTP請求超過時間...\n" + str(ex))