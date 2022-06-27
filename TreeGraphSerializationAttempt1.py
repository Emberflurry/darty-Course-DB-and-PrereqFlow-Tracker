import networkx as nx
import plotly.graph_objects as go
from courseclass import Course
import matplotlib.pyplot as plt
import openpyxl
import re
import jsongraph
import urllib
import json

'''Test and usage example'''
single_graph_link = 'https://raw.githubusercontent.com/jsongraph/json-graph-specification/master/examples/usual_suspects.json'
multiple_graph_link = 'https://raw.githubusercontent.com/jsongraph/json-graph-specification/master/examples/car_graphs.json'

f = urllib.urlopen(single_graph_link)
sg = json.load(f)
f.close

f = urllib.urlopen(multiple_graph_link)
mg = json.load(f)
f.close

# Uses Github Master branch JSON Graph Specification file by default
print("Does JSON Graph Schema validate?")
jsongraph.validate_schema(schema='', verbose=True)

print("\nDoes Single Graph example validate?")
jsongraph.validate_jsongraph(sg, schema='', verbose=True)

print("\nShow Label of Single Graph")
graphs = jsongraph.load_graphs(sg, validate=False, schema='', verbose=False)
print("    Label: ", next(graphs)['label'])

print("\nShow Label's of Multiple Graphs")
graphs = jsongraph.load_graphs(mg, validate=False, schema='', verbose=False)
for graph in graphs:
    print("    Label: ", graph['label'])





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
