import zipfile
import re
from functions import bsearch

groups=[]
groups_with_paperIDs_keywords={}
groupno_parentID={}
required_groupnos =[]
required_fosIDs=[]
file = open("required_group_nos_789_groups.txt",'r')
for line in file:
	required_groupnos = line.split(" ")
file.close()

file = open("required_fos_ids_35981.txt",'r')
for line in file:
	required_fosIDs.append(line.strip())
# print required_fosIDs


G = open("FOS_groups_level_sorted2.txt",'r')
i=0
for line in G:
	parent,l1,l2,l3=line.split('\t')
	l1= l1.strip('[|]|').replace('\'','').replace(' ','')
	l2= l2.strip('[|]').replace('\'','').replace(' ','')
	l3= l3.strip('[|]|\n').replace('\'','').replace(' ','')
	parent = parent.replace('\'','').replace(' ','')
	groupno_parentID[i]=parent
	i+=1
	c = parent
	if l1 != '':
		c=c+','+l1
	if l2 != '':
		c=c+','+l2
	if l3:
		c=c+','+l3
		# c+=l3
	c= c.split(',')
	c.sort()
	groups.append(c)

# check whether a paper belonging to Beta ACP is there in chemistry or not where beta ACP is not a part

with open("../../../MAGNEW/PaperKeywords/PaperKeywords.txt") as f:
# with zipfile.ZipFile("zips/PaperKeywords.zip") as z:
# 	with z.open("PaperKeywords.txt") as f:

	i=0
	for line in f:
		i+=1
		# print line
		pid,keyword,fid = line.split('\t')
		# print pid,keyword,fid
		for groupno in required_groupnos:
			groupno=int(groupno)
			if(bsearch(fid,groups[groupno],0,len(groups[groupno])-1)):
				# print "found" + fid, groupno
				parentID = groupno_parentID.get(groupno)
				if(groups_with_paperIDs_keywords.get(parentID) == None):
					c=[set(),set()]
					c[0].add(pid)
					c[1].add(keyword)
					groups_with_paperIDs_keywords[parentID] = c
				else:
					groups_with_paperIDs_keywords.get(parentID)[0].add(pid)
					groups_with_paperIDs_keywords.get(parentID)[1].add(keyword)
		print "line " + str(i)
		# if(i==100000):
			# break

new = open("Groups_paperIDs_keywords_required",'w')
i=0
for k, v in groups_with_paperIDs_keywords.items():
	# print v
	i+=1
	list(v[0]).sort()
	list(v[1]).sort()
	# print v
	# text file format
	# groupParentID 	listOfPapers listOfKeyowrds

	new.write(str(k) + '\t'+ str(' '.join(v[0])) + '\t' + str(' '.join(v[1])) + '\t' + '\n\n')
	# print i
new.close()