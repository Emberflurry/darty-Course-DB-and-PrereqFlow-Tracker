from bs4 import BeautifulSoup as bs
import requests
from lxml import etree
from xlwt import Workbook
import re
"""
multi = "aaaa30.04"
name = ""
numbar = ""
for c in multi:
    if c.isdigit():
        cidx = multi.index(c)
        numbar = str(multi[cidx:])
        name = str(multi[0:cidx])
        break

print(name+"|"+numbar) """


# finding index of a char in string, then deleting prev chars
line = "asdfghqwerth"
print(line[1])
i = 0
while i < len(line):
    if line[i] == "h":
        idx = i
        break
    i += 1
print(i)
print(line[i:])



