import networkx as nx
import plotly.graph_objects as go
from courseclass import Course

math003 = Course("MATH", "003")
math008 = Course("MATH","008",prereqs="MATH003")
math013 = Course("MATH","013",prereqs="MATH008 OR MATH009") # still need to figure out how to store stuff, go back later?
math022 = Course("MATH","022",prereqs="MATH013")
phys013 = Course("PHYS","013",prereqs="MATH008")
phys014 = Course("PHYS","014",prereqs="PHYS013")
engs022 = Course("ENGS","022",prereqs="PHYS014 AND MATH013")
# in future will read from excel (cleaned) file as per: https://networkx.org/documentation/stable/reference/readwrite/index.html
myListofCourses = [math003, math008, math013, math022, phys013, phys014, engs022]

myG = nx.DiGraph()  # empty directed graph  https://networkx.org/documentation/stable/tutorial.html#directed-graphs
#myG.add_node()
myG.add_nodes_from(myListofCourses)
# aight I gotta go to bed but good progress
#TODO 6/22: add edges and attributes of courses...may take some thinking...
