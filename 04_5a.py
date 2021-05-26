"""
Name: Will
----------------
purpose: " "
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

css_path = "html head title"

with open("Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_title = soup.select(css_path)
    print(tag_title[0].string)

    tag_a = soup.select("body div a")
    print(tag_a)