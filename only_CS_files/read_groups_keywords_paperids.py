import zipfile
import matplotlib.pyplot as plt

z=zipfile.ZipFile("Groups_paperIDs_keywords_cs_1.zip")

file = z.open("Groups_paperIDs_keywords_cs_1",'r')
i=0
parentID_groupno_found = {}
no_of_papers=[]
no_of_keywords=[]
# plt.figure()
points={}
for line in file:
	if(line == "\n"):
		continue
	parentID_groupno_found[line[0:8]] = i
	i+=1
	print i
	# print repr(line[0:])
	parentID,groupPapers,groupKeywords,newline = line.split('\t')
	# print parentID,len(groupPapers.split(' ')),len(groupKeywords.split(' '))
	no_of_papers.append(len(groupPapers.split(' ')))
	no_of_keywords.append(len(groupKeywords.split(' ')))
	points[parentID] = (len(groupPapers.split(' ')),len(groupKeywords.split(' ')))
	# points[parentID] = (groupKeywords,len(groupKeywords.split(' ')))
	# groupno_parentID.append(line[0:8])
	if(i==500):
		break
# groupno_parentID.sort()
# points.sort()
# sorted(points,key = lambda x: x[0])
# print points
while True:
	d = raw_input("enter id:")
	print points.get(d)
# zip(*points)
# plt.plot(*zip(*points[:-1]))
# plt.xlabel("papers")
# plt.ylabel("keywords")
# plt.show()
file.close()

# required_groupnos=[]
# file = open("cs_group_nos_343_groups.txt",'r')
# for line in file:
# 	required_groupnos = line.split(" ")
# file.close()
# print(len(required_groupnos))
# print required_groupnos

# # for g in required_groupnos:
# # 	if(groupno_parentID.get(g) == None):
# # 		print g
# # print groupno_parentID
# print len(groupno_parentID)
# print groupno_parentID

# file = open("CS_all_groups_with_level.txt",'r')
# groupno_parentID_cs={}
# parentID_groupno_cs={}
# i=0
# for line in file:
# 	groupno_parentID_cs[i]=line[0:8]
# 	parentID_groupno_cs[line[0:8]]=i
# 	i+=1
# file.close()

# g_file = open("../FOS_groups_level_sorted2.txt",'r')
# groupno_parentID={}
# i=0
# for line in g_file:
# 	parent,l1,l2,l3=line.split('\t')
# 	parent = parent.replace('\'','').replace(' ','')
# 	groupno_parentID[i]=parent
# 	i+=1
# g_file.close()

# required_groupnos=[]
# file = open("cs_group_nos_343_groups.txt",'r')
# for line in file:
# 	required_groupnos = line.split(" ")
# file.close()
# i=0
# for g in required_groupnos:
# 	g= int(g)
# 	i+=1
# 	# print i,"\n",g
# 	print groupno_parentID.get(g),parentID_groupno_found.get(groupno_parentID.get(g))

# count=0
# for i in required_groupnos:
# 	i=int(i)
# 	if(groupno_parentID_cs.get(i) != None and groupno_parentID.get(i) !=None):
# 		print str(i)+" in both"
# 	else:
# 		print i,groupno_parentID.get(i),parentID_groupno_cs.get(groupno_parentID.get(i))
# 		if(parentID_groupno_cs.get(groupno_parentID.get(i)) == None):
# 			count+=1
# print count
