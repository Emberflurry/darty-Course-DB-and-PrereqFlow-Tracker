from graphLoader import get_graph_data

from bfs import bfs

import dash
from dash import html, dcc
from dash import Input, Output, State
import dash_cytoscape as dcyto
import json

from webfunctions import aggregate_elements

dcyto.load_extra_layouts()

file = "../../2IntermediateProcessing/xlDBcleaning/deleteTestExportCURRENT3.xlsx"

nodes, edges = get_graph_data(file, "MATHglobalsRedo")

# print(bfs(list(nodes.values())[0], nodes, edges))

app = dash.Dash(__name__, title='Darty Course-Flow Vizualizer')

app.layout = html.Div([
    # HEADER? i barely know her
    html.H1(children='Dartmouth Course-Flow Vizualizer', style={'color': '#096A3F'}),
    # Sub header
    html.H4(
        children="""7/22 ORC data, dev/maint by John DeForest+Alec Bunn, viz w Plotly-Dash-Cytoscape off local DB"""),

    html.Div(className='eight columns', children=[
        dcyto.Cytoscape(
            id="cytoscape",
            elements=aggregate_elements(nodes, edges),
            stylesheet=[
                {
                    'selector': 'node',
                    'style': {
                        'label': 'data(id)'
                    }
                },
                {'selector': 'edge', 'style': {'mid-target-arrow-color': 'blue',
                                               'mid-target-arrow-shape': 'vee',
                                               'line-color': 'grey', 'arrow-scale': 3.5, }},
            ],
            style={'width': '100%', 'height': '450px'},
            layout={'name': 'dagre',
                    'roots': '[id = "MATH001"]'}
        ),
    ]),

    # html.selection
    # dcc.Dropdown(["Whole"] + [key for key in nodes.keys()], list(nodes.keys())[0], id='class_dropdown'),
    dcc.Dropdown(["Whole"] + [key for key in nodes.keys()], "Whole", id='class_dropdown'),
    dcc.RadioItems(['Prereqs', 'Postreqs', 'Both', 'Neither (what are you doing the whole point is to......nvmd smh my head)'], 'Prereqs', id="prereq_selector")

])


@app.callback(
    Output(component_id="cytoscape", component_property="elements"),
    Input(component_id="class_dropdown", component_property="value"),
    Input(component_id="prereq_selector", component_property="value"),
)
def create_graph(class_, prereq):
    if class_ == "Whole":
        return aggregate_elements(nodes, edges)
    else:
        prereq_nodes = dict()
        prereq_edges = list()
        if prereq == "Prereqs":
            prereq_nodes, prereq_edges = bfs(nodes[class_], nodes, edges, forward=False, nodes_visited=prereq_nodes,
                                             edges_visited=prereq_edges)
        elif prereq == "Postreqs":
            prereq_nodes, prereq_edges = bfs(nodes[class_], nodes, edges, forward=True, nodes_visited=prereq_nodes,
                                             edges_visited=prereq_edges)
        elif prereq == "Both":
            prereq_nodes, prereq_edges = bfs(nodes[class_], nodes, edges, forward=False, nodes_visited=prereq_nodes,
                                             edges_visited=prereq_edges)
            postreq_nodes, postreq_edges = bfs(nodes[class_], nodes, edges, forward=True, nodes_visited=prereq_nodes,
                                             edges_visited=prereq_edges)
            prereq_nodes = prereq_nodes | postreq_nodes
            prereq_edges += postreq_edges
        elif prereq == "Neither (what are you doing the whole point is to......nvmd smh my head)":
            prereq_nodes[class_] = nodes[class_]

        return aggregate_elements(prereq_nodes, prereq_edges)


if __name__ == '__main__':
    app.run_server(debug=True)

"""

# for node click, draw per/post reqs
@myApp.callback(Output(myCyto_id, 'stylesheet'),
                [Input(myCyto_id, 'tapNodeData'),
                 # Input('inputEdgeColor1', 'value'),
                 # Input('outputEdgeColor1', 'value'),
                 Input('reqDropdown1', 'value')])
def generate_stylesheet(node, requisiteDisplayChoice):
    global resetNodeSelection
    # print(resetNodeSelection)
    if not node:
        return myDefaultStylesheet
    if resetNodeSelection:
        resetNodeSelection = False
        return myDefaultStylesheet
    else:
        stylesheet = [{"selector": 'node',
                       'style': {'opacity': 0.3, 'text-justification': 'center', 'text-halign': 'center',
                                 'text-valign': 'center'
                                 }
                       },
                      {'selector': 'edge',
                       'style': {'opacity': 0.2, "curve-style": "bezier",
                                 }
                       },
                      {"selector": 'node[id = "CLER001"]', 'style': {'shape': 'rectangle', 'width': 75, 'height': 40}},

                      # {  # "selector": 'node[id = "{}"]'.format(node['data']['id']),
                      #     "selector": '[title *= a]',
                      #     "style": {  # note: FIXED - (don't) NEED TO KEEP THIS CHUNK EVEN IF IT DOESNT DO ANYTHING BC WEIRD ERROR
                      #         # 'background-color': '#B10DC9',
                      #         # "border-color": "purple",
                      #         # "border-width": 2,
                      #         # "border-opacity": 1,
                      #         # "opacity": 1,
                      #         #
                      #         # "label": "data(label)",
                      #         # "color": "#B10DC9",
                      #         # "text-opacity": 1,
                      #         # "font-size": 12,
                      #         # 'z-index': 9999
                      #     }
                      # }
                      ]
        if requisiteDisplayChoice == 'both':

            prereqNodes, prereqEdges = nodeBFSTracer(node['id'], "fwd")  # FORWARD REQS

            #note: 3lines below JUST FOR TESTING, will separate in dif IF statements for interactive viz options
            bprNodes, bprEdges = nodeBFSTracer(node['id'], "bck")   # BACKWARD REQS
            prereqNodes += bprNodes
            prereqEdges += bprEdges

        elif requisiteDisplayChoice == 'postrequisites':
            prereqNodes, prereqEdges = nodeBFSTracer(node['id'], "fwd")  # FORWARD REQS
        elif requisiteDisplayChoice == 'prerequisites':
            prereqNodes, prereqEdges = nodeBFSTracer(node['id'], "bck")  # BACKWARD REQS
        elif requisiteDisplayChoice == 'neither (why would you do this?)':
            prereqNodes, prereqEdges = [node], []  # empty, for testing

            curNodeID = node['id']  #NOTE this stuff is required for correct formatting without selection
            stylesheet.append({"selector": 'node[id ="{}"]'.format(curNodeID),
                               "style": {'background-color': '#2c4c96',
                                         "border-color": "purple",
                                         "border-width": 2,
                                         "border-opacity": 1,
                                         "opacity": 1,

                                         "color": "#fafbfc",
                                         "text-opacity": 1,
                                         "font-size": 18,
                                         'z-index': 9999}
                               })
        else:
            return "ERROR WITH variable requisiteDisplayChoice - not one of both, prerequisites, postrequisites"

        for eaN in prereqNodes:
            if '%' in eaN:
                stylesheet.append({"selector": 'node[id ="{}"]'.format(eaN),
                                   "style": {'background-color': '#2c4c96',
                                             "border-color": "blue",
                                             "border-width": 5.5,
                                             "border-opacity": 1,
                                             "opacity": .55,  # note: changed-ORs faded

                                             "color": "#fafbfc",
                                             "text-opacity": .75,  # note: changed-ORs faded
                                             "font-size": 18,
                                             'z-index': 9999}
                                   })
            elif '&' in eaN:
                stylesheet.append({"selector": 'node[id ="{}"]'.format(eaN),
                                   "style": {'background-color': '#2c4c96',
                                             "border-color": "red",
                                             "border-width": 6,
                                             "border-opacity": .9,
                                             "opacity": .75,  # note: changed-ANDs faded, less than ORs tho

                                             "color": "#fafbfc",
                                             "text-opacity": .75,  # note: changed-ANDs faded
                                             "font-size": 18,
                                             'z-index': 9999}
                                   })

            else:
                stylesheet.append({"selector": 'node[id ="{}"]'.format(eaN),
                                   "style": {'background-color': '#2c4c96',
                                             "border-color": "purple",
                                             "border-width": 2,
                                             "border-opacity": 1,
                                             "opacity": 1,

                                             "color": "#fafbfc",
                                             "text-opacity": 1,
                                             "font-size": 18,
                                             'z-index': 9999}
                                   })
        for eaE in prereqEdges:
            eaEID = eaE['data']['id']
            if '%' in eaE['data']['target']:
                stylesheet.append({"selector": 'edge[id ="{}"]'.format(eaEID),
                                   "style": {'background-color': '#2c4c96',
                                             "border-color": "blue",
                                             "border-width": 2,
                                             "border-opacity": 1,
                                             "opacity": .75,

                                             "color": "#fafbfc",
                                             "text-opacity": 1,
                                             "font-size": 18,
                                             'z-index': 9999}
                                   })
            else:
                stylesheet.append({"selector": 'edge[id ="{}"]'.format(eaEID),
                                   "style": {'background-color': '#2c4c96',
                                             "border-color": "purple",
                                             "border-width": 2,
                                             "border-opacity": 1,
                                             "opacity": 1,

                                             "color": "#fafbfc",
                                             "text-opacity": 1,
                                             "font-size": 18,
                                             'z-index': 9999}
                                   })

        stylesheet.append(
            {'selector': 'node', 'style': {'label': 'data(id)', 'shape': 'rectangle', 'width': 100, 'height': 60}})
        stylesheet.append({'selector': 'edge', 'style': {'curve-style': 'bezier'}})
        stylesheet.append({'selector': 'edge', 'style': {'mid-target-arrow-color': 'blue',
                                                         'mid-target-arrow-shape': 'vee',
                                                         'line-color': 'grey', 'arrow-scale': 3.5, }}, )
        stylesheet.append(
            {"selector": 'node[id = "CLER001"]', 'style': {'shape': 'rectangle', 'width': 100, 'height': 60}})
        stylesheet.append({'selector': 'node[id *= "%"]',
                           'style': {'label': orLabel}})
        # note: default stylesheet below, copied and appended to new stylesheet cuz i had to readd for some reason

        return stylesheet


# for node click, pulls node data
@myApp.callback(Output('tap-node-data-output1', 'children'),
                [Input(myCyto_id, 'tapNodeData')])
def displayTapNodeData(data):
    if data == None:
        return "select a node to display ORC information here"
    return str(json.dumps(data, indent=2)).strip("{").strip("}")  # indent=2 ?


# for hover over node, pulls node name/title basic info
@myApp.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
                Input(myCyto_id, 'mouseoverNodeData'))
def displayTapNodeData(data):
    global resetNodeSelection
    if data:
        if data['id'] == 'CLER001':
            resetNodeSelection = True
        return "Hovered Node: " + data['id'] + ": " + data['title']



# does dropdown layout menu stuff
# @myApp.callback(Output('cytoscape-update-layout', 'layout'),
#                 Input('dropdown-update-layout', 'value'))
# def update_layout(layout):
#     return {'name': layout, 'animate': True}


if __name__ == '__main__':
    myApp.run_server(debug=True)
"""
