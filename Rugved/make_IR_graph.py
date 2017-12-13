import networkx as nx

file = open("400 for IR papers",'r')
papers={}
for line in file:
	parentID,refID = line.split('\t')
	refID.strip("\n|\r")
	paper[parentID] = refID.split(' ')

G = nx.DiGraph()

for k,v in papers:
	G.add_node(k)
	for i in v:
		G.add_node(i)
		G.add_edge(k,i)

nx.draw(G,with_labels=True,font_weight="bold")
nx.write_pajek(G,"IR_700_papers.net")
