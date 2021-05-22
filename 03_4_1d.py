"""
Name: Will
----------------
purpose: use find() to get the tag by custom attrs 
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_str = soup.find(text="請問你的性別？")
    print(tag_str)
    tag_str = soup.find(text="10")
    print(tag_str)
    print(type(tag_str))
    print(tag_str.parent.name)
    tag_str = soup.find(text="男-")
    print(tag_str)