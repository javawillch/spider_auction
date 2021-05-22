"""
Name: Will
----------------
purpose: use find() to get the tag by functions
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

def is_secondary_question(tag):
    return tag.has_attr("herf") and \
            tag.get("href") == "http://example.com/q2"

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    
print(is_secondary_question) 
tag_a = soup.find(is_secondary_question)
print(tag_a)