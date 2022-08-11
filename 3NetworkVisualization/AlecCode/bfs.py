# This is not really BFS bc not really searching for anything
# Just finding all nodes that can get to this one / this one can get to
# Also the way I implemented it ended up being depth first search lol
# Doesn't matter though cause checking all connecting nodes anyway

def bfs(startNode, edges, forward=True, nodes_visited=set(), edges_visited=list()):
	nodes_visited.add(startNode)
	# All the nodes you can get to is this node plus all the nodes your children can get to.
	for edge in edges:
		if forward and edge["startNode"] == startNode:
			
			if not edge in edges_visited:
				edges_visited.append(edge)

			if not edge["endNode"] in nodes_visited:
				nodes_visited, edges_visited = bfs(edge["endNode"], edges,
					forward=forward, nodes_visited=nodes_visited, edges_visited=edges_visited)
			

		if not forward and edge["endNode"] == startNode:
			if not edge in edges_visited:
				edges_visited.append(edge)

			if not edge["startNode"] in nodes_visited:
				nodes_visited, edges_visited = bfs(edge["startNode"], edges,
					forward=forward, nodes_visited=nodes_visited, edges_visited=edges_visited)

	return nodes_visited, edges_visited