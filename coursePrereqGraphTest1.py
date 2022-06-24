import networkx as nx
import plotly.graph_objects as go
from courseclass import Course
import matplotlib.pyplot as plt

hash2coursenameDict = {"0001": "CHEM040",
                       "0002": "CHEM006",
                       "0003": "CHEM010",
                       "0004": "PHYS013",
                       "0005": "PHYS015",
                       "0006": "PHYS004",
                       "0007": "MATH008",
                       "0008": "CHEM040"}
G = nx.DiGraph()
for i in hash2coursenameDict:
    # G.add_node(i)
    G.add_node(hash2coursenameDict[i])
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

hash2prereqsDict = {"CHEM040": "MATH008/PHYS013:PHYS015:PHYS004/CHEM006,CHEM010"}

def crsgraphcreator(courseHash):
    courseName = hash2coursenameDict[courseHash]
    prereqString = hash2prereqsDict[courseName].strip()
    allPrConditions = prereqString.split("/")
    print( allPrConditions)


    # for ea in allPrConditions:
    #     if ":" in ea:



print(crsgraphcreator("0008"))

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
