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
                       "0008": "CHEM040",
                       "0009": "PHYS031",
                       "0010": "PHYS016",
                       "0011": "PHYS014"}
myG = nx.DiGraph()
for i in hash2coursenameDict:
    myG.add_node(hash2coursenameDict[i])
    # G.add_node(i)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

hash2prereqsDict = {"CHEM040": "MATH008/PHYS013:PHYS015:PHYS004/CHEM006:CHEM010",
                    "PHYS031": "PHYS013/PHYS016/PHYS014:PHYS015"
                    }

global orCounter
orCounter=0
def crsgraphcreator(courseHash):
    global orCounter
    courseName = hash2coursenameDict[courseHash]
    prereqString = hash2prereqsDict[courseName].strip()
    allPrConditions = prereqString.split("/")
    print(allPrConditions)

    # orCounter = 0
    for ea in allPrConditions:
        if ":" in ea:  # OR List
            orItems = ea.strip().split(":")
            print(orItems)

            newOrNode = str("or" + str(orCounter))
            myG.add_node(newOrNode)
            myG.add_edge(newOrNode, courseName)

            for eaOrPrq in orItems:
                myG.add_edge(eaOrPrq, newOrNode)
            orCounter += 1

        else:  # single course
            myG.add_edge(ea, courseName)


crsgraphcreator("0008")
crsgraphcreator("0009")

nx.draw(myG, with_labels=True, font_weight='bold',node_color='grey')
plt.show()
