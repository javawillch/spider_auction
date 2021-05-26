"""
Name: Will
----------------
purpose: children attribute
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.select("#q2")
    tag_ul = tag_div[0].ul
    for child in tag_ul.children:
        print('-----------------')
        print(child)
        print(type(child))