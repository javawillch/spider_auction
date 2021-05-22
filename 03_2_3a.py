"""
Name: Will
----------------
purpose: NavigableString object
pre-condition: 
post-condition: 
modules need to download: BeautifulSoup
"""
from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikout'>Hello World!</div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div

print(tag.string)
print(tag.text)
print(tag.get_text())
print("tag.string:     "+ str(type(tag.string)))
print("tag.text:       "+ str(type(tag.text)))
print("tag.get_text(): "+ str(type(tag.get_text())))

