"""
Name: Will
----------------
purpose: use find_all by regular expression for URL
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    url_regexp = re.compile("^http:")
    tag_href = soup.find(href=url_regexp)
    print(tag_href)
    print("--------------------------")
    tag_href_list = soup.find_all(href=url_regexp)
    print(tag_href_list)