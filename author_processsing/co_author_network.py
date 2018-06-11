import networkx as nx
import zipfile
from random import randint
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
l_3=0
b_3_10=0
g_10=0
list_author = set()
G = nx.Graph()
count = 0
with zipfile.ZipFile("no_upload_co_authors.zip") as z:
	with z.open("no_upload_co_authors.txt") as f:
		i=0
		j=0
		for line in f:
			j+=1
			x=0
			# print x
			i+=1
			aid,no_author,authors = line.strip("\r|\n").split("\t")
			no_author = int(no_author)
			# print authors
			if(no_author<=3):
				x=1
				l_3+=no_author
			elif(no_author<10):
				b_3_10+=no_author
			else:
				if(no_author>50):
					continue
				g_10+=no_author
			if(x==0):
				continue
			if(i%500==0):
				print i
				break
			count+=no_author
			authors = authors.split(" ")
			# print authors
			G.add_node(aid,venue='False')
			list_author.add(aid)
			for a in authors:
				if(a == aid):
					continue
				G.add_node(a,venue='False')
				list_author.add(a)
				G.add_edge(a,aid)
print i,l_3,b_3_10,g_10,j,count
print G.number_of_nodes(),G.number_of_edges()


with zipfile.ZipFile("no_upload_venue_authors.zip") as z:
	with z.open("venue_authors.txt") as f:
		i=0
		total =0
		for line in f:
			i+=1
			# if(i==1):
				# print i
				# break
				# continue
			# print line
			afid,no_authors_afname,authors = line.strip("\r|\n").split("\t")
			# no_authors = no_authors_afname.match(r"(\d+)(.*)")
			no_authors = int(re.match(r"(\d+).*",no_authors_afname).groups()[0])
			afname = re.match(r"(\d+)(.*)",no_authors_afname).groups()[1]
			authors = authors.split(" ")
			auth= set()
			for a in authors:
				auth.add(a)
			for e in list_author:
				if(e in auth):
					G.add_node(afid,name =afname,venue='True')
					G.add_edge(afid,e)
					total+=1

			if(i%10000==0):
				print i,total
		print i,total
print G.number_of_nodes(),G.number_of_edges()


# nx.draw(G,with_labels=True,font_weight="bold")
fh=open("test.adjlist",'wb')
nx.write_adjlist(G, fh)
nx.write_gml(G,"sample5.gml")
nx.write_gexf(G, "test.gexf")
