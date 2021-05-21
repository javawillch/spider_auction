"""
Name: Will
----------------
purpose: read the file
pre-condition: 
post-condition: 
"""

fp = open("test.txt", "r", encoding="utf8")
str = fp.read()
print("檔案內容：")
print(str)