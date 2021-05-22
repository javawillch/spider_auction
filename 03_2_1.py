"""
Name: Will
----------------
purpose: 
pre-condition: 
post-condition: 
modules need to download: BeautifulSoup
"""
from bs4 import BeautifulSoup

html_str = "<p>Hello World!<p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)