"""
Name: Will
----------------
purpose: comapre different methods to get str
pre-condition: 
post-condition: 
tag.string cannot get str if there are child tags, pros -> can get comment 
"""
from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikout'>Hello World! <p> Final Test </p></div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div                          # -> get first <div>

print(tag.string)
print(tag.text)
print(tag.get_text())
print(tag.get_text(";"))
print(tag.get_text(",", strip=True))