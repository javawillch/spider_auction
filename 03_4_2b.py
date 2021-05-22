"""
Name: Will
----------------
purpose: use find_all(name, attribute, recursive, text, limit. **kwargs)
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.find("div", id="q2")

    print(tag_div)
    print("------------------------")
    tag_all = tag_div.find_all(True)
    print(tag_all)