import networkx as nx
from courseclass import Course
import matplotlib.pyplot as plt

math003 = Course("MATH", "003")
math008 = Course("MATH", "008", prereqs="MATH003")
math013 = Course("MATH", "013", prereqs="MATH008 OR MATH009") # still need to figure out how to store stuff, go back later?
math022 = Course("MATH", "022", prereqs="MATH013")
phys013 = Course("PHYS", "013", prereqs="MATH008")
phys014 = Course("PHYS", "014", prereqs="PHYS013")
engs022 = Course("ENGS", "022", prereqs="PHYS014 AND MATH013")
math009 = Course("MATH", "009")
# in future will read from excel (cleaned) file as per: https://networkx.org/documentation/stable/reference/readwrite/index.html
myListofCourses = [math003, math008, math009, math013, math022, phys013, phys014, engs022]

myG = nx.DiGraph()  # empty directed graph  https://networkx.org/documentation/stable/tutorial.html#directed-graphs
#myG.add_node()
myG.add_nodes_from(myListofCourses)
print(myG)
# aight I gotta go to bed but good progress
#TODO 6/22: add edges and attributes of courses...may take some thinking...
for i in myListofCourses:
    print("i:", i)
    if i.prereqs != "" or i.prereqs != None:
        for j in myListofCourses:
            print("j:", j)
            print(str(i.prereqs.lower()))
            if str(i.prereqs.lower()) == str(j).lower():
                myG.add_edge(j, i, type=j.dept +j.number +"req for: "+i.dept + i.number)

print(myG)
# added edges for testing, need to be able to display
# TODO 6/22: Get display/drawing of graph working-use matplotlib.pyplot?
nx.draw(myG,with_labels=True, font_weight='bold')
plt.show()

# so far so good, just need to handle ORs ANDs
# and ofc the more complex cases
# and cross-listing of courses - should I have them as essentially two sides/three of the same coin, or a linkage? leaning towards "coin" type framework




