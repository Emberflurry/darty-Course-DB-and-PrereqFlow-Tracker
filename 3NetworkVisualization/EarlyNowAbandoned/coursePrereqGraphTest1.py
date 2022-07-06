import networkx as nx
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
                       "0011": "PHYS014",
                       "0012": "CHEM005"}


def get_key_by_value(find_val, dict):
    for key, value in dict.items():
        if find_val == value:
            return key
    return "key4: " + find_val + " DNE"


myG = nx.DiGraph()
for i in hash2coursenameDict:
    myG.add_node(hash2coursenameDict[i])
    # G.add_node(i)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

hash2prereqsDict = {"CHEM040": "MATH008/PHYS013:PHYS015:PHYS004/CHEM006:CHEM010",
                    "PHYS031": "PHYS013/PHYS016/PHYS014:PHYS015",
                    "CHEM006": "CHEM005"
                    }

global orCounter  # bc the OR nodes need to have unique IDs
orCounter = 0


def crsgraphcreator(courseHash):
    global orCounter
    courseName = hash2coursenameDict[courseHash]
    prereqString = hash2prereqsDict[courseName].strip()
    if prereqString != "" and prereqString is not None:
        allPrConditions = prereqString.split("/")
        print(allPrConditions)

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
    else:
        print(courseName + " hasNoPrqs")


for eaCrs in hash2prereqsDict:  # loops over prereq dict
    crsgraphcreator(get_key_by_value(eaCrs, hash2coursenameDict))
# crsgraphcreator("0008")
# crsgraphcreator("0009")
# crsgraphcreator("0002")

nx.draw(myG, with_labels=True, font_weight='bold', node_color='grey')
plt.show()
