import openpyxl
import dash
import dash_cytoscape as dcyto
from dash import html as dhtml
from dash import dcc  # ^ use this instead
from dash.dependencies import Input, Output, State
import re
import json
from queue import Queue
dcyto.load_extra_layouts()
myApp1 = dash.Dash(__name__)

myApp1.layout = dhtml.Div([
    dcyto.Cytoscape(
        id='cytoscape-elements-basic',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '400px'},
        stylesheet=[{'selector': 'edge', 'style': {'curve-style': 'bezier'}}],
        elements=[
            # The nodes elements
            {'data': {'id': 'one', 'label': 'Node 1'},
             'position': {'x': 50, 'y': 50}},
            {'data': {'id': 'two', 'label': 'Node 2'},
             'position': {'x': 20, 'y': 200}
             },
            {'data': {'id': 'three', 'label': 'Node 3'},
             'position': {'x': 350, 'y': 200}
             },

            # The edge elements
            {'data': {'source': 'one', 'target': 'two', 'label': 'Node 1 to 2'}}
        ]
    )
])

if __name__ == '__main__':
    myApp1.run_server(debug=True)