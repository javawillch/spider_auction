"""
Name: Will
----------------
purpose: > 
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")

    tag_div = soup.find(id="q1")
    print(tag_div)
    print("----------------------")
    tag_div = soup.select("#q1 ~ .survey")
    for item in tag_div:
        print(item.p.a.string)
    print("----------------------")
    tag_div = soup.select("#q1 + .survey")
    for item in tag_div:
        print(item.p.a.string)
        