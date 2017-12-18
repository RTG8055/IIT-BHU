import networkx as nx

# file = open("../output/papers_with_references.txt",'r')
file = open("1692/papers_with_references_1692_orSimilarity.txt",'r')
papers={}
i=0
for line in file:
	i+=1
	parentID,refID = line.split('\t')
	refID.strip("\n|\r")
	papers[parentID] = refID.split(' ')
print i
file.close()

file = open("1692/toppapers_averagesimilarity_or_1692.csv",'r')

all_papers=set()

i=0
for line in file:
	i+=1
	all_papers.add(line.split(",")[0])

# i=0
# for line in file:
# 	i+=1
# 	line=line.strip("\n")
# 	all_papers.add(line)
G = nx.DiGraph()
print i,len(all_papers)

no=0
removed =0
for k,v in papers.items():
	for i in v:
		if(i in all_papers):
			G.add_node(k)
			no+=1
			G.add_node(i)
			edges = G.edges(i)
			to_be_added=True
			for ed in edges:
				if((i,k) == ed):
					removed+=1
					to_be_added=False
					break
			if(to_be_added):
				G.add_edge(k,i)
			# try:
			# 	# nx.find_cycle(G,orientation='original')
			# 	G.remove_edge(k,i)
			# 	removed+=1
			# except Exception as e:
			# 	pass
print no,removed
print G.number_of_nodes()
nx.draw(G,with_labels=True,font_weight="bold")
print "done drawing"
nx.write_pajek(G,"1692/toppapers_or_1692.net")
nx.write_gml(G,"1692/toppapers_or_1692.gml")
print "done writing"