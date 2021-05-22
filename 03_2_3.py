"""
Name: Will
----------------
purpose: get tag and attrs of tag
pre-condition: 
post-condition: 
modules need to download: BeautifulSoup
"""
from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikout'>Hello World!</div><div id='msg' class='body strikout'>Hello E!</div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div
print(tag)
print(type(tag))
print(tag['id'])
print(tag["class"])
print(tag.attrs)