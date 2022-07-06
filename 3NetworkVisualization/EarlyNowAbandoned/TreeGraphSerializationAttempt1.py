import networkx as nx
import matplotlib.pyplot as plt

# do NOT use jsongraph-outdated and does not install.





# class Node:
#     def __init__(self, value = None, children=None):
#         self.value = value
#         self.children = children
#
# math003 = Course("MATH", "003")
# math008 = Course("MATH", "008", prereqs="MATH003")
# math013 = Course("MATH", "013", prereqs="MATH008 OR MATH009") # still need to figure out how to store stuff, go back later?
# math022 = Course("MATH", "022", prereqs="MATH013")
# phys013 = Course("PHYS", "013", prereqs="MATH008")
# phys014 = Course("PHYS", "014", prereqs="PHYS013")
# engs022 = Course("ENGS", "022", prereqs="PHYS014 AND MATH013")
# math009 = Course("MATH", "009")
# myListofCourses = [math003, math008, math009, math013, math022, phys013, phys014, engs022]
myCprereqdict={"m74": "m74#|m54,o|m101,o|m31,m71|||"}
# pieced = myCprereqdict["m74"].split("|")
# pieced = filter(None, re.split("[|,]", myCprereqdict["m74"]))
# print(pieced)
prstring = myCprereqdict["m74"]
print(prstring)
myG = nx.DiGraph()
i=0
while i <= len(prstring)-1:
    if prstring[i]=="#":
        break
    i+=1
# print(i)
myG.add_node(prstring[0:i])
# def addNode(eanode):
#
#     if eanode.children
#     return addNode() # on children


nx.draw(myG, with_labels=True, font_weight='bold', node_color='grey')
plt.show()
