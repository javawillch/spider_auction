"""
Name: Will
----------------
purpose: use find() to get the tag by unique id
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.find(id="q2")
    tag_a = tag_div.find("a")
    print(tag_a.string)