import re
from functions import bsearch

g_file = open("../FOS_groups_level_sorted2.txt",'r')



#Physics, computer science, engineering, chemistry, mathematics

required_group_ids=['0271BC14']
groupno_parentID={}
groups={}

i=0
for line in g_file:
	parent,l1,l2,l3=line.split('\t')
	l1= l1.strip('[|]|').replace('\'','').replace(' ','')
	l2= l2.strip('[|]').replace('\'','').replace(' ','')
	l3= l3.strip('[|]|\n').replace('\'','').replace(' ','')
	parent = parent.replace('\'','').replace(' ','')
	# print parent,l1,l2,l3
	groupno_parentID[i]=parent
	i+=1
	c = ''
	if l1 != '':
		if c != '':
			c=c+','+l1
		else:
			c=l1
	if l2 != '':
		if c != '':
			c=c+','+l2
		else:
			c=l2
	if l3 != '':
		if c!= '':
			c=c+','+l3
		else:
			c=l3
	c= c.split(',')
	c.sort()
	# if(i==1):
		# break
	# print c

	#making groups
	groups[parent] = c

required_group_ids.sort()
# print required_group_ids

# for j in [0,1,2]:
for j in [0,1,2,3]:
	new_group_ids=[]
	if(j==0):
		new_group_ids = new_group_ids + groups["0271BC14"]
	else:
		for k in groups.keys():
			if(bsearch(k,required_group_ids,0,len(required_group_ids)-1) == 1):
				# this group is required.
				new_group_ids = new_group_ids + groups[k]
				#add all the ids in this groups to the required group
	# print required_group_ids
	required_group_ids = list(set(required_group_ids + new_group_ids)) # update the required ids. 
						# set to remove the duplicates
						
	#repeat the process only 3 times should be enough for getting all the L1,L2 and L3 groups L0 already present
	required_group_ids.sort()
	# break
# print required_group_ids
new = open("CS_fos_ids.txt",'w')
# new = open("required_group_ids_try2.txt",'w')
i=0

for g in required_group_ids:
	i+=1
	print g
	new.write(g+"\n")
	# if(i==1):
		# break
print i
new.close()












