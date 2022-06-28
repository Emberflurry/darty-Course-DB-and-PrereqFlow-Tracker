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

print(mathSheet.max_row)

with open('testExp.sif', 'w') as myOutFile:
    for i in range(2, mathSheet.max_row):
        prContents = str(mathSheet.cell(row=i, column=12).value).strip().split(",")
        # print(prContents)
        if str(prContents) != "['None']":
            for ea in prContents:
                myOutFile.write(str(ea))
                myOutFile.write('\n')


        #todO HANDLE MULTIPLE OR AND AND NODES-COUNTERS!

