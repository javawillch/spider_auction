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
    tag_list = soup.find_all("p", class_="question")
    print(tag_list)

    for question in tag_list:
        print(question.a.string)