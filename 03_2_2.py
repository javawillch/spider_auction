"""
Name: Will
----------------
purpose: 
pre-condition: 
post-condition: 
modules need to download: BeautifulSoup
"""
from bs4 import BeautifulSoup

with open("test.txt", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup.prettify())

    