"""
Name: Will
----------------
purpose: download picture
pre-condition: 
post-condition: 
with Example.html
"""
import urllib.request

url = "https://miro.medium.com/max/708/1*ifSob78knBe5rME04WHftg.png"
response = urllib.request.urlopen(url)
fp = open("miki2.png", "wb")
size = 0
while True:
    info = response.read(1000)
    if len(info) < 1:
        break
    size = size + len(info)
    fp.write(info)
print(size, "個字元下載...")
fp.close()
response.close()

