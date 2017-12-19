import networkx as nx

def calc_bc_cc(graph):
	##############
	# networkx graph 
	# return a graph with bc and cc of all nodes
	##############
	# G = nx.DiGraph()
	G2 = graph
	all_nodes = list(G2.nodes())

	for node in all_nodes:
		G2.node[node]['bc'] = 0
		G2.node[node]['cc'] = 0

		edges = list(G2.out_edges(node))
		for edge in edges:
			dest_node = edge[1]
			indegree = G2.in_degree(dest_node)
			G2.node[node]['bc'] += indegree-1
		edges = list(G2.in_edges(node))
		for edge in edges:
			source_node = edge[0]
			outdegree = G2.out_degree(source_node)
			G2.node[node]['cc'] += outdegree -1

	return G2

def calc_cscore(graph,interest_node):
	# G2 = graph
	G2 = nx.DiGraph()
	H = G.to_undirected()
	all_nodes = list(H.nodes())

	for node in all_nodes:
		if(node == interest_node):
			continue
		bc = H.node[node]['bc']
		cc = H.node[node]['cc']
		d = nx.shortest_path_length(H,source = node,target = interest_node)
		H.node[node]['cs'] = float(bc+cc) / float(d)

	return H.to_directed()



# G = nx.DiGraph()
# nx.add_path(G, [0, 1, 2, 3])
# nx.add_path(G,[4,1])
# nx.add_path(G,[4,2])

# print G.nodes(data = True)
# G = calc_bc_cc(G)
# print G.nodes(data = True)
# G = calc_cscore(G,1)
# print G.nodes(data = True)


# # print nx.shortest_path_length(G,source=1,target=3)
# # try:
# # 	print nx.shortest_path_length(G,source=1,target=4)
# # except Exception as e:
# # 	print "vice-a-versa"
# # 	print nx.shortest_path_length(G,source=4,target=1)

# # nx.write_pajek(G,"bc_cc.net")
# nx.write_gml(G,"bc_cc.gml")