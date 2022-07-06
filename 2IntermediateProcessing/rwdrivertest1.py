# 11/24/2021 - 11/28/2021 John DeForest
# Course prereq/otherdata dictionary loader and driver, still testing, still in text form (no useful prereq objs/etc)
# don't have linkages/backchaining set up yet w objs -- all in text format rn

from courseclass import Course

# straight import from excel? current method: update master doc, copy/paste to csv, delete header, save, rerun

# impfile = open("C:/Users/John DeForest/Desktop/dartyCourseTracker.xlsx", "r")
# how to read from only one SHEET of the doc if impt straight from excel?

# maybe open/save as csv?
classdbfilecsv = "C:/Users/John DeForest/Desktop/classdbtest1.csv"  # currently have to save as csv and then run this


# currently not used:
def prereq_interpreter(prereq_text):
    print("test" + prereq_text)  # will later use to turn xlist and prereq info from csv to actual lists/etc


# get data from ea entry of excel row, store in vars
def parse_line(line):
    section_split = line.split(",")
    departmentname = section_split[0].strip()
    coursenumber = section_split[1].strip()
    coursetitle = section_split[2].strip()
    professors = section_split[3].strip()
    pastterms = section_split[4].strip()
    curfutterms = section_split[5].strip()
    crosslisttext = section_split[6].strip()
    prerequisitestext = section_split[7].strip()
    prereqnotes = section_split[8].strip()
    extrafee = section_split[9].strip()
    distribs = section_split[10].strip()
    nroeligible = section_split[11].strip()
    typicalblocks = section_split[12].strip()
    courseregnumber = section_split[13].strip()
    coursetype = section_split[14].strip()
    worldculturedistribs = section_split[15].strip()
    associatedlab = section_split[16].strip()
    coursecredits = section_split[17].strip()

    return departmentname, coursenumber, coursetitle, professors, pastterms, curfutterms, crosslisttext, \
           prerequisitestext, prereqnotes, extrafee, distribs, nroeligible, typicalblocks, courseregnumber, coursetype, \
           worldculturedistribs, associatedlab, coursecredits


# run to get a dictionary of Course objs w all info, key is str of 4digDept+course#
def load_class_network(inputfile):
    newdict = {}
    workingfile = open(inputfile)
    for line in workingfile:
        # print(line)
        departmentName, coursenumber, coursetitle, professors, pastterms, curfutterms, crosslisttext, \
        prerequisitestext, prereqnotes, extrafee, distribs, nroeligible, typicalblocks, courseregnumber, coursetype, \
        worldculturedistribs, associatedlab, coursecredits = parse_line(line)

        course_i = Course(departmentName, coursenumber, coursetitle, professors, pastterms, curfutterms, crosslisttext,
                          prerequisitestext, prereqnotes, extrafee, distribs, nroeligible, typicalblocks,
                          courseregnumber, coursetype, worldculturedistribs, associatedlab, coursecredits)

        name_in_dict = str(departmentName) + str(coursenumber)
        newdict[name_in_dict] = course_i
        # print(name_in_dict)

    workingfile.close()
    return newdict


# testing:
classdict = load_class_network(classdbfilecsv)
for item in classdict:
    print(classdict[item].dept + " | " + classdict[item].number + " | " + classdict[item].title + " | " +
          classdict[item].profs + " | " + classdict[item].pastterms + " | " + classdict[item].curfutterms + " | " +
          classdict[item].xlist + " | " + classdict[item].prereqs + " | " + classdict[item].prereqnotes + " | " +
          classdict[item].xtrafee + " | " + classdict[item].distribs + " | " + classdict[item].isNROelig + " | " +
          classdict[item].typicalblocks + " | " + classdict[item].CRN + " | " + classdict[item].coursetype + " | " +
          classdict[item].worldcults + " | " + classdict[item].hasAssocLab + " | " + classdict[item].credits)

print(classdict["MATH008"])  # works!
