"""
Name: Will
----------------
purpose: read the file
pre-condition: 
post-condition: 
"""

with open("test.txt", "r", encoding="utf8") as fp:
    str = fp.read()
    print("檔案內容：")
    print(str)


    
    