"""
Name: Will
----------------
purpose: Comment object
pre-condition: 
post-condition: 
"""
from bs4 import BeautifulSoup

html_str = "<p><!-- this is comment --></p>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.p
print(tag.string)
print(tag.text)
print(tag.get_text())
print(tag.comment)
print(type(tag.string))