"""
Name: Will
----------------
purpose: read the file
pre-condition: 
post-condition: 
"""
with open("test.txt", "r", encoding = "utf8") as fp:
    list1 = fp.readlines()
    for line in list1:
        print(line, end = "")
 