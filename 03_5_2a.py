"""
Name: Will
----------------
purpose: use find_all by regular expression for Email
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:

    soup = BeautifulSoup(fp, "lxml")    
    email_regexp = re.compile("\w+@\w+\.\w+")
    tag_str = soup.find(text=email_regexp)
    print(tag_str)
    print("-------------------")
    tag_str_list = soup.find_all(text=email_regexp)
    print(tag_str_list)
    