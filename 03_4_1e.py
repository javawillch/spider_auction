"""
Name: Will
----------------
purpose: use find() to get the tag by multiple filters
pre-condition: 
post-condition: 
with Example.html
"""
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.find("div", attrs = {"class": "question"})
    tag_div = soup.find("div", class_ = "question")
    print(tag_div)
    tag_p = soup.find("p", class_="question")
    print(tag_p)