"""
Name: Will
----------------
purpose: css selector
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

css_path = "#q1 > ul > li:nth-child(1) > span" # BeautifulSoup not support nth-child(1) -> NotImplementedError: Only the following pseudo-classes are implemented: nth-of-type.
css_path = "#q1 > ul > li:nth-of-type(1) > span"

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_item = soup.select(css_path)
    print(tag_item[0].string)

    tag_first_div = soup.find("div")
    tag_div = tag_first_div.select("div:nth-of-type(3)")
    print(tag_div)

