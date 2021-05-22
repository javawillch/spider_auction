"""
Name: Will
----------------
purpose: 
pre-condition: 
post-condition: 
modules need to download: BeautifulSoup
"""
from bs4 import BeautifulSoup
import requests

url = "https://term.ptt.cc/"

r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)