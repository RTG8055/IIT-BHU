import zipfile
import re
from functions import bsearch

new = open("Groups_paperIDs_keywods",'w')
groups=[]
groups_with_paperIDs_keywords={}
groupno_parentID={}

G = open("FOS_groups_level_sorted2.txt",'r')
i=0
for line in G:
	parent,l1,l2,l3=line.split('\t')
	l1= l1.strip('[|]|').replace('\'','').replace(' ','')
	l2= l2.strip('[|]').replace('\'','').replace(' ','')
	l3= l3.strip('[|]|\n').replace('\'','').replace(' ','')
	parent = parent.replace('\'','').replace(' ','')
	# print parent,l1,l2,l3
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
	# if(i==1):
		# break
	# print c
	groups.append(c)

# print groups[442]
# print groupno_parentID
# check whether a paper belonging to Beta ACP is there in chemistry or not where beta ACP is not a part

with open("../../../MAGNEW/PaperKeywords/PaperKeywords.txt") as f:
	i=0
	for line in f:
		i+=1
		# print line
		pid,keyword,fid = line.split('\t')
		# print pid,keyword,fid
		groupno=0
		while(groupno<len(groups)):
			# print fid,groupno
			# print "\n"
			if(bsearch(fid,groups[groupno],0,len(groups[groupno])-1)):
				# print "found" + fid, groupno
				parentID = groupno_parentID[groupno]
				if(groups_with_paperIDs_keywords.get(parentID) == None):
					c=[[],[]]
					c[0].append(pid)
					c[1].append(keyword)
					groups_with_paperIDs_keywords[parentID] = c
				else:
					x=groups_with_paperIDs_keywords[parentID]
					paperAlreadyThere=False
					keywordAlreadyThere=False
					for d in [0,1]:
						h=0
						for j in x[d]:
							h+=1
							#h==1 implies papers are checked
							#h==2 implies keywords are checked
							if(h==1):
								if(j.strip() == pid):
									paperAlreadyThere=True
									break
							if(h==2):
								if(j.strip() == keyword):
									keywordAlreadyThere = True
					if(not paperAlreadyThere):
						temp = groups_with_paperIDs_keywords[parentID][0] #get the list of papers in that group
						temp.append(pid)
						groups_with_paperIDs_keywords[parentID][0]=temp #update the paperIDs list
						print "added paper-"+pid +" to " + parentID + " Group"


					if(not keywordAlreadyThere):
						temp = groups_with_paperIDs_keywords[parentID][1] # get the list if keywords in that group
						temp.append(keyword)
						groups_with_paperIDs_keywords[parentID][1]= temp # update the Keywords list
						print "added keyword-"+keyword +" to " + parentID + "Group"

			# print "abcd",groupno
			groupno+=1
			# if(groupno==443):
				# break
		print "line " + str(i) + " done"
		# if(i==1000):
			# break

i=0
for k, v in groups_with_paperIDs_keywords.items():
	print v
	v[0].sort()
	v[1].sort()
	
	# text file format
	# groupParentID 	listOfPapers listOfKeyowrds

	new.write(str(k) + '\t'+ str(v[0]) + '\t' + str(v[1]) + '\t' + '\n\n')
	i+=1
new.close()
