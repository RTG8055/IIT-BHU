import re
from functions import bsearch



g_file = open("FOS_groups_level_sorted2.txt",'r')
required_group_nos=[]
parentID_groupno={}
groups={}

i=0
for line in g_file:
	parent,l1,l2,l3=line.split('\t')
	l1= l1.strip('[|]|').replace('\'','').replace(' ','')
	l2= l2.strip('[|]').replace('\'','').replace(' ','')
	l3= l3.strip('[|]|\n').replace('\'','').replace(' ','')
	parent = parent.replace('\'','').replace(' ','')
	# print parent,l1,l2,l3
	parentID_groupno[parent]=i
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

fos_ids=[]
file = open('required_fos_ids.txt','r')
for line in file:
	fos_ids.append(line.strip('\n'))
i=0
j=0
for e in fos_ids:
	i+=1
	if(parentID_groupno.get(e)):
		j+=1
		required_group_nos.append(parentID_groupno.get(e))
print i,j # 35981 Ids # 769 groups

# print required_group_nos


new = open("required_group_nos.txt",'w')

new.write(" ".join([str(k) for k in required_group_nos]))
new.close()