from bs4 import BeautifulSoup as bs
import requests
from xlwt import Workbook

# FOR MATH UG DEPT

# open excel output, add titles:
wb1 = Workbook()
sheet1 = wb1.add_sheet('rawexport')

sheet1.write(0, 0, 'dept4dig')
sheet1.write(0, 1, 'course#')
sheet1.write(0, 2, 'name')
sheet1.write(0, 3, 'instructor')
sheet1.write(0, 4, 'xlisted_w')
sheet1.write(0, 5, 'ORCdescription')
sheet1.write(0, 6, 'prereqs')
sheet1.write(0, 7, 'Alldistribs')
sheet1.write(0, 8, 'coreqs')


baseUrl = "http://dartmouth.smartcatalogiq.com"
url = 'http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Mathematics/MATH-Mathematics-Undergraduate'

req = requests.get(url)
soup = bs(req.text, 'html.parser')

print("")
titles = soup.find_all('li', attrs={'class', 'hasChildren active'})
print(titles)
print("")

therightone = titles[2]
print(therightone)
print("")

mathclasses = therightone.find_all("a")[1:]
print(mathclasses)
print("yuh")

i = 0
while i < len(mathclasses):
    classes = [mathclasses[i]]   # [0] for MATH 1, and so on in list
    print(classes)
    #quit()
    for class_ in classes:
        newUrl = baseUrl + class_["href"]
        req = requests.get(newUrl)
        soup = bs(req.text, 'html.parser')
        content = soup.find_all("div", attrs={"id": "main"})[0]

        dept_num = content.h1.span.text
        name = ""
        numbar = ""
        for c in dept_num:
            if c.isdigit():
                cidx = dept_num.index(c)
                numbar = str(dept_num[cidx:])
                name = str(dept_num[0:cidx])
                break

        department = str(name).strip()
        cnumber = str(numbar).strip()
        print("starting "+department+"|"+cnumber)
        # quit()
        coursename = content.h1.text.replace(dept_num, "").strip()

        description = content.find_all("div", attrs={"class": "desc"})[0].p.text
        try:
            instructor = content.find_all("div", attrs={"id": "instructor"})[0].text.replace("Instructor", "")
        except:
            instructor = ""

        #instructor = content.find_all("div", attrs={"id": "instructor"})[0].text.replace("Instructor", "")
        prereqs = content.find_all("div", attrs={"class": "sc_prereqs"})[0].text.replace("Prerequisite", "").strip()

        coreqs = content.find_all("div", attrs={"class": "sc_coreqs"})[0].text.strip()  # untested :) note: could not find any ORC listings with coreqs (all were listed as prereqs even if they were coreqs lol)

        alltextcontent = content.text
        sub1 = "Culture"
        sub2 = "The Timetable"
        try:
            idx1 = alltextcontent.index(sub1)
            idx2 = alltextcontent.index(sub2)
            distribs = alltextcontent[idx1 + len(sub1) + 1:idx2].replace("Dist:", "").strip()
        except:
            distribs = ""

        subt1 = "Cross Listed Courses"
        if prereqs != "" or None:
            subt2 = "Prerequisite"
        elif coreqs != "" or None:
            subt2 = "Co"
        elif distribs != "" or None:
            subt2 = "Distributive"
        else:
            subt2 = "The Timetable of Class"

        if subt1 in alltextcontent:
            indx1 = alltextcontent.index(subt1)
            indx2 = alltextcontent.index(subt2)
            xlisted = alltextcontent[indx1+len(subt1)+1:indx2].strip()
        else:
            xlisted = ""

        # WRITE TO EXCEL?
        sheet1.write(i+1, 0, department)
        sheet1.write(i+1, 1, cnumber)
        sheet1.write(i+1, 2, coursename)
        sheet1.write(i+1, 3, instructor)
        sheet1.write(i+1, 4, xlisted)
        sheet1.write(i+1, 5, description)
        sheet1.write(i+1, 6, prereqs)
        sheet1.write(i+1, 7, distribs)
        sheet1.write(i+1, 8, coreqs)

        i += 1
        print("finished"+department+"|"+cnumber)

print("finished all, saving workbook...")
wb1.save('orcMathUGScrape1.xls')
print("workbook saved successfully. you may now exit/close.")

