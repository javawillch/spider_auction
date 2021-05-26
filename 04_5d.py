"""
Name: Will
----------------
purpose: find element by class and id
pre-condition: 
post-condition: 
with Example.html
"""
import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    tag_div = soup.select("#q1")
    print(tag_div)
    tag_span = soup.select("span#email")
    print(tag_span)
    print("--------------------")
    tag_div = soup.select("#q1, #q2")
    for item in tag_div:
        print(item.a.string)
    print("--------------------")
    tag_div = soup.select("div.question")
    print(tag_div)
    print("--------------------")
    tag_div = soup.select("div .question")
    print(tag_div)
    print("--------------------")
    tag_div = soup.find("div")
    tag_p = tag_div.select(".question")
    for item in tag_p:
        if item != None:
            print(item.a["href"])
    print("--------------------")
    tag_li = soup.select("[class~=selected]")
    for item in tag_li:
        print(item)       