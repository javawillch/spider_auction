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
    tag_a = soup.select("p > a")
    # print(tag_a)

    tag_li = soup.select("ul > li:nth-of-type(2)")
    # print(tag_li)

    tag_span = soup.select("div > #email")
    print(tag_span)