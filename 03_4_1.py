"""
Name: Will
----------------
purpose: use find() to get the tag by tag name
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_a = soup.find("a")
    print(tag_a.string)
    tag_p = soup.find(name="p")
    print(tag_p.a.text)
    tag_a = tag_p.find(name="a")
    print(tag_a.get_text())

