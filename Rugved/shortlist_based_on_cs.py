import networkx as nx
import calculate_BC_CC

G = nx.read_gml("1692/toppapers_or_1692.gml")

G = calc_bc_cc(G)
G = nx.Graph()

G
