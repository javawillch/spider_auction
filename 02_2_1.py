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
print(r.status_code)
