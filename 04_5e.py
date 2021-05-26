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
    tag_a = soup.select("a[href]")
    print(tag_a)
    print("--------------------")

    tag_a = soup.select("a[href='http://example.com/q2']")
    print(tag_a)
    print("--------------------")

    tag_a = soup.select("a[href^='http://example.com']")  # startWtih
    print(tag_a)
    print("--------------------")

    tag_a = soup.select("a[href$='q3']")                  # endWith
    print(tag_a)
    print("--------------------")    

    tag_a = soup.select("a[href*='q']")                   # include
    print(tag_a)
    print("--------------------")      
