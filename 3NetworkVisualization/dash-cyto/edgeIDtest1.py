import openpyxl
import dash
import dash_cytoscape as dcyto
from dash import html as dhtml
from dash import dcc  # ^ use this instead
from dash.dependencies import Input, Output, State
import re
import json
from queue import Queue

directed_edges = [
    {'data': {'id': src+tgt, 'source': src, 'target': tgt}}
    for src, tgt in ['BA', 'BC', 'CD', 'DA']
]

print(directed_edges)
