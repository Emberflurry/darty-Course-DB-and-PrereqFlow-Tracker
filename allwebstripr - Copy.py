from bs4 import BeautifulSoup as bs
import requests
from xlwt import Workbook

# FOR All UG Depts listed (correctly) on the ORC page as of 1/2/2022 (and added to csv in current folder

# get list of urls of department sites (with sublisted courses) -- done manually from orc, transcribed to excel
# currently need to manually save excel doc as csv, then run this
xlcsv_urlslist = "temppglist.csv"
urlsopenedlist = open(xlcsv_urlslist)

depturlslist = []

for line in urlsopenedlist:
    i = 0
    while i < len(line):
        if line[i] == "h":
            idx = i
            break
        i += 1
    else:
        idx = 0

    cleanedline = line[idx:]
    depturlslist.append(cleanedline.strip())

print(depturlslist)


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

rownumber = 0
for url in depturlslist:
    
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
 
    print("Alltitle-sidebarlistings: ")
    titles = soup.find_all('li', attrs={'class', 'hasChildren active'})
    print(titles)
    print("")

    print("correcttitlelisting: ")
    thecorrect_title_entry = titles[2]  # trial and error, baby
    print(thecorrect_title_entry)
    print("")

    specdeptclasses = thecorrect_title_entry.find_all("a")[1:]
    print(specdeptclasses)
    print("yuh")

    i = 0
    while i < len(specdeptclasses):
        classes = [specdeptclasses[i]]   # [0] for MATH 1/etc, and so on in list
        print(classes)

        for class_ in classes:
            newUrl = baseUrl + class_["href"]
            req = requests.get(newUrl)
            soup = bs(req.text, 'html.parser')
            content = soup.find_all("div", attrs={"id": "main"})[0]
            try:
                dept_num = content.h1.span.text
            except:
                dept_num = ""
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

            coursename = content.h1.text.replace(dept_num, "").strip()

            try:
                description = content.find_all("div", attrs={"class": "desc"})[0].p.text
            except:
                description = ""
            try:
                instructor = content.find_all("div", attrs={"id": "instructor"})[0].text.replace("Instructor", "")
            except:
                instructor = ""
            try:
                prereqs = content.find_all("div", attrs={"class": "sc_prereqs"})[0].text.replace("Prerequisite", "").strip()
            except:
                prereqs = ""
            try:
                coreqs = content.find_all("div", attrs={"class": "sc_coreqs"})[0].text.strip()  # untested :) note: could not find any ORC listings with coreqs (all were listed as prereqs even if they were coreqs lol)
            except:
                coreqs = ""
            alltextcontent = content.text
            sub1 = "and/or World Culture"
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
                subt2 = "The Timetable "

            if subt1 in alltextcontent:
                print(distribs)
                print(subt2)
                indx1 = alltextcontent.index(subt1)
                indx2 = alltextcontent.index(subt2)


                xlisted = alltextcontent[indx1+len(subt1)+1:indx2].strip()
            else:
                xlisted = ""

            # WRITE TO EXCEL?
            sheet1.write(rownumber+1, 0, department)
            sheet1.write(rownumber+1, 1, cnumber)
            sheet1.write(rownumber+1, 2, coursename)
            sheet1.write(rownumber+1, 3, instructor)
            sheet1.write(rownumber+1, 4, xlisted)
            sheet1.write(rownumber+1, 5, description)
            sheet1.write(rownumber+1, 6, prereqs)
            sheet1.write(rownumber+1, 7, distribs)
            sheet1.write(rownumber+1, 8, coreqs)

            i += 1
            rownumber += 1
            print("finished"+department+"|"+cnumber)

        print("finished allofDEPT, saving workbook...")
        wb1.save('orcALL_UGScrape1.xls')
        print("saveSuc")

print("workbook saved successfully. you may now exit/close.")
wb1.save('orcALL_UGScrape1.xls')

