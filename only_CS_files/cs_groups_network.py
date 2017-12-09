import networkx as nx
import re
import matplotlib.pyplot as plt

class FOS:
	def __init__(self,fid,conf):
		self.conf_level= round(float(conf),3)
		self.fosID=fid
f= open("CS_all_groups_sorted.txt",'r')
groupno_parentID={}
parentID_groupno={}
i=1
groups={}

for line in f:
	# print repr(line)
	parentID,outDeg,no_of_groups,avg_conf,subGroups = line.split('\t')
	parentID_groupno[parentID]=i
	groupno_parentID[i]=parentID
	# print repr(parentID)
	subGroups = subGroups.strip('\n').replace(r", ",",")
	subGroups = subGroups.split(' ')
	# print repr(subGroups)
	FOSlist = []
	h=0
	for x in subGroups:
		x= x.strip("(|)").replace("'","").split(',')
		obj = FOS(x[0],x[1])
		# print obj.conf_level,obj.fosID
		FOSlist.append(obj)
	i+=1
	groups[parentID]=FOSlist
	if(i==1000):
		break
# print groups,
# print "\n"
# print parentID_groupno,groupno_parentID
# print parentID_groupno["0007022E"]
# print groups["0007022E"],parentID_groupno["0007022E"],groupno_parentID[parentID_groupno["0007022E"]]
G = nx.DiGraph()

for parent,children in groups.items():
	parentID = parentID_groupno.get(parent,999)
	G.add_node(parentID)
	for child in children:
		childID=parentID_groupno.get(child.fosID,999)
		wt = child.conf_level
		G.add_node(childID)
		G.add_edge(parentID,childID,weight = wt)
		# print(,parentID_groupno.get(childID),wt)
		# print parentID_groupno.get(parent,99),parentID_groupno.get(child.fosID,99),child.conf_level
		# G.add_edge(parentID,childID)

# elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
# esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G,pos,node_size=700)
# nx.draw_networkx_edges(G,pos,edgelist=elarge,width=1)
# nx.draw_networkx_edges(G,pos,edgelist=esmall,width=1,alpha=0.5,edge_color='b',style='dashed')
# nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
# plt.axis('off')
# plt.savefig("weighted_graph.png") # save as png
# plt.show() # display
# plt.figure()
nx.draw(G,with_labels=True,font_weight="bold")
# plt.show()
nx.write_pajek(G,"CS_network_new.net")