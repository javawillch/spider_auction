"""
Name: Will
----------------
purpose: use find() to get the tag by class 
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_li = soup.find(attrs={"class": "response"})
    tag_span = tag_li.find("span")
    print(tag_span.string)
