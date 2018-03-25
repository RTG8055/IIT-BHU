import networkx as nx

file = open("output2/sample56/top_papers_references56_1.txt",'r')
papers={}
i=0
for line in file:
	i+=1
	parentID,refID = line.split('\t')
	refID.strip("\n|\r")
	papers[parentID] = refID.split(' ')
print i
file.close()

all_papers=set()


with open("output2/sample56/top_papers56_1.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		all_papers.add(line.split("\t")[0].strip('"'))



print i,len(all_papers)
G = nx.DiGraph()

added_papers=set()

no=0
removed =0
for k,v in papers.items():
	for i in v:
		if(i in all_papers):
			added_papers.add(i)
			added_papers.add(k)
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
			# try:
			# 	# nx.find_cycle(G,orientation='original')
			# 	G.remove_edge(k,i)
			# 	removed+=1
			#	 to_be_added=False
			# except Exception as e:
			# 	pass
			if(to_be_added):
				G.add_edge(k,i)
print no,removed
print G.number_of_nodes(),G.number_of_edges()
try:
	x = nx.find_cycle(G,orientation='original')
	while(True):
		print(x)
		x1=x[1]
		# print x1
		G.remove_edge(*x1)
		x = nx.find_cycle(G,orientation='original')
		print x
except Exception as e:
	print "no cycles",G.number_of_edges()
not_added_papers = all_papers - added_papers
print len(all_papers),len(not_added_papers),len(added_papers)

new = open("output2/sample56/all_paper_without_references56_1.txt",'w')
for p in not_added_papers:
	new.write(str(p) + "\n")
print "written not done filtered papers"

# nx.draw(G,with_labels=True,font_weight="bold")
print "done drawing"
nx.write_pajek(G,"output2/sample56/graph56_56_1.net")
nx.write_gml(G,"output2/sample56/graph56_56_1.gml")
print "done writing"

