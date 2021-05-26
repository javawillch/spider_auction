"""
Name: Will
----------------
purpose:
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup.html.head.title.string)
    print(soup.html.head.meta["charset"])
    print(soup.html.body.div.div.p.a.string)
