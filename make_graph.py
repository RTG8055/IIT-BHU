import networkx as nx

file = open("output/sample2/papers_with_references2.txt",'r')
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


file = open("output/sample2/papers2.txt",'r')

i=0
for line in file:
	i+=1
	line=line.strip("\n")
	all_papers.add(line)


G = nx.DiGraph()
print i,len(all_papers)

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
			if(to_be_added):
				G.add_edge(k,i)
print no,removed
print G.number_of_nodes()
not_added_papers = all_papers - added_papers
print len(all_papers),len(not_added_papers),len(added_papers)


new = open("output/sample2/paper_without_references2.txt",'w')
for p in not_added_papers:
	new.write(str(p) + "\n")
print "written not done papers"

nx.draw(G,with_labels=True,font_weight="bold")
print "done drawing"
nx.write_pajek(G,"output/sample2/graph2_1.net")
nx.write_gml(G,"output/sample2/graph2_1.gml")
print "done writing"

