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
    # 找出所有<p>, <span>標籤
    tag_list = tag_div.find_all(["p", "span"])
    print(tag_list)
    # 找出class屬性值question or selected的所有標籤
    tag_list = tag_div.find_all(class_=["question", "selected"])
    print(tag_list)