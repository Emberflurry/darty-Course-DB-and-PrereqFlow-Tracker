import networkx as nx
import plotly.graph_objects as go

#TODO 6/22/22: LEARN NODE AND EDGE SPECIFICS, decide how to store/retrieve/check prereqs esp cpx ones
# start here: https://networkx.org/documentation/stable/tutorial.html
myG = nx.random_geometric_graph(200, 0.125) # rando testing generator, replace with from DB?
edge_xs = []
edge_ys = []
for edge in myG.edges():
    x0, y0 = myG.nodes[edge[0]]['pos']
    x1, y1 = myG.nodes[edge[1]]['pos']
    edge_xs.append(x0)
    edge_xs.append(x1)
    edge_xs.append(None)
    edge_ys.append(y0)
    edge_ys.append(y1)
    edge_ys.append(None)

edge_trace = go.Scatter(
    x=edge_xs, y=edge_ys,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in myG.nodes():
    x, y = myG.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))
node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(myG.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>testing networkX for graphNodeFunctionality',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()