"""
Name: Will
----------------
purpose: save .html as txt file after prettify format by bs4
pre-condition: 
post-condition: 
modules need to download: BeautifulSoup
"""
from bs4 import BeautifulSoup
import requests

url = "https://onlineonly.christies.com/s/jewels-online/lots/2028?filters=&lang=zh-cht&page=2&searchphrase=&sortby=LotNumber&themes="

##"https://www.p337.info/pokemongo/pages/shiny-release-dates/"
##"https://twpkinfo.com/ipoke.aspx"
##"http://www.google.com"
r = requests.get(url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "lxml")

with open("test2.txt", "w", encoding="utf8") as fp:
    fp.write(soup.prettify())
    print("寫入檔案test2.txt...")
    fp.close()