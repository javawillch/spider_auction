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
    tag_div = soup.find(attrs={"data-custom": "important"})
    print(tag_div.string)


