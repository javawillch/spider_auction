"""
Name: Will
----------------
purpose: BeautifulSoup object
pre-condition: 
post-condition: 
"""
from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikout'>Hello World!</div>"
soup = BeautifulSoup(html_str, "lxml")
print(soup.name)
print(type(soup))