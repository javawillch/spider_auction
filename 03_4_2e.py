"""
Name: Will
----------------
purpose: use find_all(name, attribute, 『recursive』, text, limit. **kwargs)
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.find("div", id="q2")
    # 找出所有<li>
    tag_list = tag_div.find_all("li")
    print(tag_list)
    # 不使用遞迴找出所有<li> -> 只搜尋『子』標籤
    tag_list = tag_div.find_all("li", recursive = False)
    print(tag_list)
