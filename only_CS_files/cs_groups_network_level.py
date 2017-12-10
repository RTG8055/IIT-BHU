import networkx as nx
import re
import matplotlib.pyplot as plt

class FOS:
	def __init__(self,fid,conf,pl,cl):
		self.conf_level= round(float(conf),3)
		self.fosID=fid
		self.parentLevel = int(pl)
		self.childLevel = int(cl)
f= open("CS_all_groups_with_level.txt",'r')
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
		# print repr(x)
		obj = FOS(x[0],x[1],x[2],x[3])
		# print obj.conf_level,obj.fosID,obj.parentLevel,obj.childLevel
		FOSlist.append(obj)
		# break
	i+=1
	groups[parentID]=FOSlist
	if(i==100):
		break
# print groups,
# print "\n"
# print parentID_groupno,groupno_parentID
# print parentID_groupno["0007022E"]
# print groups["0007022E"],parentID_groupno["0007022E"],groupno_parentID[parentID_groupno["0007022E"]]
G = nx.DiGraph()
# px=0
py=0
# cx=0
x0=0
x1=0
x2=0
x3=0
cy=0
# print groups
for parent,children in groups.items():
	print children
	parentNo = parentID_groupno.get(parent,999)
	# G.add_node(parentNo,x =px,y= py)
	# px+=10
	# py+=10
	# cx=px
	j=0
	for child in children:
		print child.childLevel,child.parentLevel
		if(child.childLevel - child.parentLevel >1):
			continue
		childNo=parentID_groupno.get(child.fosID,999)
		wt = child.conf_level
		cx=1000
		if(child.childLevel == 1):
			cx=x1
			x1+=50
			cy = 100
			py=0
		elif(child.childLevel == 2):
			cx=x2
			x2+=50
			cy= 200
			py=100
		else:
			cx=x3
			x3+=50
			cy=300
			py=100
		if(j==0):
			G.add_node(parent,x=cx*0.5,y=py)
		j+=1
		# cx+=10
		G.add_node(child.fosID,x =cx,y=cy)
		G.add_edge(parent,child.fosID,weight = wt)
		# print(,parentID_groupno.get(childNo),wt)
		# print parentID_groupno.get(parent,99),parentID_groupno.get(child.fosID,99),child.conf_level
		# G.add_edge(parentNo,childNo)
	# break

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
x = nx.get_node_attributes(G,'x')
y=nx.get_node_attributes(G,'y')
# x[999]=-20000
# y[999]=200
pos={}
for k,v in x.items():
	pos[k]=(v,y[k])
print pos

# pos[k]=(v,v2)
nx.draw(G,pos,with_labels=True,font_weight="bold")
# nx.write_pajek(G,"CS_network_new2.net")
nx.write_gml(G,"network.gml")
nx.write_adjlist(G,"test.adjlist")
# plt.show()