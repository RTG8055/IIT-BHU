import networkx as nx
import random
# import sys
# sys.setdefaultencoding() does not exist, here!
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('utf8')

# fh=open("test.adjlist", 'rb')
# G=nx.read_adjlist(fh)
# # print G.number_of_nodes(),G.number_of_edges()
G = nx.read_gexf("test.gexf")
# print G.number_of_nodes()

path_traversed=set()

all_nodes = G.nodes()

# print type(all_nodes),len(all_nodes)

target = random.randint(0,len(all_nodes)-1)

print target
venues =  nx.get_node_attributes(G,'venue')

# print venues

i=0
for n in all_nodes:
	if(i==target):
		target = n
		print venues[target]
		if(venues[target] == 'False'):
			print venues[target]
			break
		else:
			target=i
			target+=1
	i+=1
source = target
path_traversed.add(source)
neigh =  G.neighbors(source)
print "target:",source

count =0
target = source
while(True):
	count+=1
	if(count==11):
		break
	neigh = G.neighbors(target)
	print 'new target',target
	total=0
	for x in neigh:
		total+=1
		# print repr(x)
	# print total,'total'
	if(total==1):
		break
	nex = random.randint(2,total)
	# print nex,'nex'
	i=0
	neigh = G.neighbors(target)
	for x in neigh:
		i+=1
		# print repr(x),'x'
		if(i==nex):
			if(x == ''):
				nex+=1
				continue
			target = x
			print target,'next'
			path_traversed.add(x)
			break
print path_traversed

venues_or_not = [venues[p] for p in path_traversed]

names =  nx.get_node_attributes(G,'name')

recommendation=[]

for p in path_traversed:
	print "\n",p,":"
	if(venues[p] == 'True'):
		recommendation.append(names[p])
		print names[p]
	else:
		print "False"
# print recommendation
