"""
Name: Will
----------------
purpose: find element by class and id
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_a = soup.select_one("a[href]")
    print(tag_a)
    