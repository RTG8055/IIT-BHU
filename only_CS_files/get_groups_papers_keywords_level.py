import zipfile
from functions import bsearch

groups=[]
groups_with_paperIDs_keywords=[]
groupno_parentID={}
required_groupnos =[]
required_fosIDs=[]
file = open("cs_group_nos_343_groups.txt",'r')
for line in file:
	required_groupnos = line.split(" ")
file.close()

G = open("../FOS_groups_level_sorted2.txt",'r')
i=0
for line in G:
	parent,l1,l2,l3=line.split('\t')
	i+=1
	l1= l1.strip('[|]|').replace('\'','').replace(' ','')
	l2= l2.strip('[|]').replace('\'','').replace(' ','')
	l3= l3.strip('[|]|\n').replace('\'','').replace(' ','')
	parent = parent.replace('\'','').replace(' ','')
	groupno_parentID[i]=parent

	print parent,l1,l2,l3
	if(i==5):
		break
print groupno_parentID