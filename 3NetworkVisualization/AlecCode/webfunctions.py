from dash import html
import dash_cytoscape as dcyto

def aggregate_elements(nodes, edges):
    # aggregate nodes and edges and put in right format
    elements = []

    for key in nodes.keys():
        elements.append({'data':{'id': key, "label":key, 'title':nodes[key]["title"], 'desc':nodes[key]["desc"]}},)

    for edge in edges:
        elements.append({"data":{"id":edge["startNode"]+edge["endNode"], 
            "source":edge["startNode"], "target":edge["endNode"], "label":edge["label"]}})

    # Return graph
    return elements

