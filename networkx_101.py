import networkx as nx

G = nx.DiGraph()
# G.add_node(1)
G.add_nodes_from(range(1,15))
# H = nx.path_graph(10)
# G.add_node(H)
# G.add_edge(1, 2)
# e = (2, 3)
# G.add_edge(*e)  # unpack edge tuple*

G.add_edges_from([(1, 3),(2,3),(2,4),(2,10),(3,5),(4,6),(10,13),(5,7),(7,8),(6,8),(6,9),(8,11),(9,12),(13,14)])
# G.add_node(1)
# G.add_edge(1, 2)
# G.add_node("spam")        # adds node "spam"
# G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
# G.add_edge(3, 'm')

# import matplotlib.pylab as plt 
# #import Matplotlib plotting interface
# g = nx.erdos_renyi_graph(100,0.15)
# nx.draw(g)
# nx.draw_random(g)\
nx.write_pajek(G,"test.net")