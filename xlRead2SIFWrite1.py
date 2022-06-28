import networkx as nx
import plotly.graph_objects as go
from courseclass import Course
import matplotlib.pyplot as plt
import openpyxl

cprqfile = "C:/Users/John DeForest/PycharmProjects/dartyclassdb1/deltestexp.xlsx"
sheet1 = "MathOnly4networkTesting"
wb_obj = openpyxl.load_workbook(cprqfile)
# print(wb_obj.sheetnames)
mathSheet = wb_obj[wb_obj.sheetnames[0]]


with open('testExp.sif', 'w') as myOutFile:
    glbOrCtr=0
    for i in range(2, mathSheet.max_row):
        prContents = str(mathSheet.cell(row=i, column=12).value).strip().split(",")
        if str(prContents) != "['None']":
            orDict = {}  # RESETS FOR EACH COURSE, AVOIDING OVERLAPS
            for ea in prContents:
                print(ea)
                if "%" in ea:
                    curOR_ID = ea[ea.find("%"):ea.find("%")+3]
                    print(curOR_ID)

                    if curOR_ID not in orDict:
                        # add new mapping {line% : global%} in orDict
                        if glbOrCtr >= 10:
                            orDict[curOR_ID] = "or"+str(glbOrCtr)
                        elif glbOrCtr < 10:
                            orDict[curOR_ID] = "or0"+str(glbOrCtr)
                        # increment orCounter
                        glbOrCtr += 1
                        print(glbOrCtr)

                    # EITHER WAY set/replace to global mapping (new or existing mapping)
                    ea = ea.replace(curOR_ID, orDict[curOR_ID])

                myOutFile.write(str(ea))
                myOutFile.write('\n')


        #todO HANDLE MULTIPLE OR AND AND NODES-COUNTERS!

