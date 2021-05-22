"""
Name: Will
----------------
purpose: use find_all by regular expression
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    regexp = re.compile("男-")
    tag_str = soup.find(text=regexp)
    print(tag_str)
    regexp = re.compile("\w+-") # 1..*個字母數字,然後- 為結尾
    tag_str_list = soup.find_all(text=regexp)
    print(tag_str_list)
