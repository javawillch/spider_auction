"""
Name: Will
----------------
purpose: use find_all(name, attribute, recursive, 『text』, limit. **kwargs)
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.find("div", id="q2")
    # 找出全部文字內容清單
    tag_str_list = tag_div.find_all(text=True)
    print(tag_str_list)
    # 找出特定文字內容清單
    tag_str_list = tag_div.find_all(text=["20", "40"])
    print(tag_str_list)