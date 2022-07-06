from bs4 import BeautifulSoup as bs
import requests
from lxml import etree

baseUrl = "http://dartmouth.smartcatalogiq.com"
url = 'http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Mathematics/MATH-Mathematics-Undergraduate'

req = requests.get(url)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('li', attrs={'class', 'hasChildren active'})
therightone = titles[2]

classes = therightone.find_all("a")[1:]
classes = [classes[21]]   # [0] for MATH 1, and so on in list

for class_ in classes:
    newUrl = baseUrl + class_["href"]
    req = requests.get(newUrl)
    soup = bs(req.text, 'html.parser')
    content = soup.find_all("div", attrs={"id": "main"})[0]

    dept_num = content.h1.span.text
    coursename = content.h1.text.replace(dept_num, "").strip()
    description = content.find_all("div", attrs={"class": "desc"})[0].p.text
    instructor = content.find_all("div", attrs={"id": "instructor"})[0].text.replace("Instructor", "")
    prereqs = content.find_all("div", attrs={"class": "sc_prereqs"})[0].text.replace("Prerequisite", "").strip()
    # note: could not find any ORC listings with coreqs (all were listed as prereqs even if they were coreqs lol)
    coreqs = content.find_all("div", attrs={"class": "sc_coreqs"})[0].text.strip()  # untested :)

    alltextcontent = content.text
    sub1 = "Culture"
    sub2 = "The Timetable"
    idx1 = alltextcontent.index(sub1)
    idx2 = alltextcontent.index(sub2)
    distribs = alltextcontent[idx1+len(sub1)+1:idx2].replace("Dist:", "").strip()

    subt1 = "Cross Listed Courses"
    if prereqs != None:
        subt2 = "Prerequisite"
    elif coreqs != None:
        subt2 = "Co"
    elif distribs != None:
        subt2 = " Distributive"
    else:
        subt2 = "The Timetable of Class"

    indx1 = alltextcontent.index(subt1)
    indx2 = alltextcontent.index(subt2)
    xlisted = alltextcontent[indx1+len(subt1)+1:indx2].strip()

    print(dept_num+"|"+coursename)
    #print(description)
    #print(instructor+"|"+prereqs+"|"+coreqs)
    #print(distribs)
    print(xlisted)
