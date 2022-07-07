import dash
import dash_cytoscape as dcyto
from dash import html as dhtml

myApp = dash.Dash(__name__)
# OG NODES
# myNodes = [
#     {
#         'data': {'id': short, 'label': label},
#         'position': {'x': 20 * lat, 'y': -20 * long}
#     }
#     for short, label, long, lat in (
#         ('la', 'Los Angeles', 34.03, -118.25),
#         ('nyc', 'New York', 40.71, -74),
#         ('to', 'Toronto', 43.65, -79.38),
#         ('mtl', 'Montreal', 45.50, -73.57),
#         ('van', 'Vancouver', 49.28, -123.12),
#         ('chi', 'Chicago', 41.88, -87.63),
#         ('bos', 'Boston', 42.36, -71.06),
#         ('hou', 'Houston', 29.76, -95.37)
#     )
# ]
myNodes = [
    {
        'data': {'id': short, 'label': label},
        # 'position': {'x': 20 * lat, 'y': -20 * long}
    }
    for short, label in (
        ('la', 'Los Angeles'),
        ('nyc', 'New York'),
        ('to', 'Toronto'),
        ('mtl', 'Montreal'),
        ('van', 'Vancouver'),
        ('chi', 'Chicago'),
        ('bos', 'Boston'),
        ('hou', 'Houston')
    )
]

myEdges = [{'data': {'source': source, 'target': target, 'label': myLabel}}
           for source, target, myLabel in (
               ('van', 'la','N'),
               ('la', 'chi', 'P'),
               ('hou', 'chi','R'),
               ('to', 'mtl','N'),
               ('mtl', 'bos','N'),
               ('nyc', 'bos','IP required'),
               ('to', 'hou','aksdj'),
               ('to', 'nyc','grade >=B+'),
               ('la', 'nyc','p'),
           )]
allElements = myEdges + myNodes
myDefaultStylesheet = [
            {'selector': 'node', 'style': {'label': 'data(id)'}},  # NODES
            #{'selector': 'edge', 'style': {'label': 'data(label)'}},  # EDGES
            {'selector': 'edge', 'style': {'curve-style': 'bezier'}},
            {'selector': 'edge', 'style':{'mid-target-arrow-color':'blue','mid-target-arrow-shape':'vee','line-color':'blue','arrow-scale':2,}}
                        ]

# directed_edges = [ # testing other edge set that had working edge arrows
#     {'data': {'id': src+tgt, 'source': src, 'target': tgt}}
#     for src, tgt in ['BA', 'BC', 'CD', 'DA']
# ]
# print(directed_edges) #demo
# print(myEdges) #mine
# print("asd")
# print([{'data': {'id': id_}} for id_ in 'ABCD'] )


myApp.layout = dhtml.Div([
    dcyto.Cytoscape(
        id='cytoscape',
        elements=allElements,
        # {'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 50, 'y': 50}},
        #             {'data': {'id': 'two', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 200}},
        #             {'data': {'source': 'one', 'target': 'two','label': 'Node 1 to 2'}}

        stylesheet=myDefaultStylesheet,

        # [
        #     # {'selector': 'node', 'style': {'label': 'data(id)'}}
        #     # {'selector': 'node', 'style': {'label': 'data(label)'}},  # NODES
        #     # {'selector': 'edge', 'style': {'label': 'data(label)'}},  # EDGES
        #     # {'selector': 'edge', 'style': {'curve-style': 'bezier'}},
        #     # {'selector': 'edge', 'style': {'mid-target-arrow-color': 'blue','mid-target-arrow-shaoe': 'vee','arrow-scale':4,'line-color':'blue'}}
        # ],

        #layout={'name': 'preset'}  # for default, requires location input
        layout={'name': 'breadthfirst',  # cose for physics-based  https://dash.plotly.com/cytoscape/layout
            'roots': '[id = "nyc"]'}
    )
])

if __name__ == '__main__':
    myApp.run_server(debug=True)
