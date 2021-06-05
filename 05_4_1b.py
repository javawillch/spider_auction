"""
Name: Will
----------------
purpose: write csv file from W3schools
pre-condition: 
post-condition: 
with Example.html
"""
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.w3schools.com/html/html_media.asp"

csvfile = "VideoFormat.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find(class_="w3-table-all")  #find all <table>
rows = tag_table.findAll("tr")

with open(csvfile, "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        rowList = []
        for cell in row.findAll(["td", "th"]):
            rowList.append(cell.get_text().replace("\n", "").replace("\r", ""))
        writer.writerow(rowList)
