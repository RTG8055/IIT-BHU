import zipfile
import re
# from functions import bsearch

comSci_id = '0271BC14'
groups={}
groups[comSci_id]=[0,0,0]

with zipfile.ZipFile("../zips/FieldOfStudyHierarchy.zip") as z2:
	with z2.open("FieldOfStudyHierarchy.txt") as f2:
		i=0
		for j in [0,1,2,3]:
			for line in f2:
				childFOSid,childFOSlevel,parentFOSid,parentFOSlevel,conf = line.split('\t')
				# conf = conf.strip('\\r|\\n')
				# print float(conf)
				# print repr(i),repr(conf)
				i=i+1;
				if(groups.get(parentFOSid)==None):
					pass
				else:
					temp = groups[parentFOSid]
					temp[0] +=1 # number of child fos ids
					temp[1] +=float(conf) #total of the child confidences
					childFOSlevel = childFOSlevel[1:]
					parentFOSlevel = parentFOSlevel[1:]
					groups[parentFOSid].append((childFOSid,float(conf),childFOSlevel,parentFOSlevel))
					if(groups.get(childFOSid)==None):
						groups[childFOSid]=[0,0,0]
				# if(i==1000000):
					# break


new = open("CS_all_groups_with_level.txt",'w')
# new = open("CS_all_groups.txt",'w')
i=0
for k, v in groups.items():
	# print v
	# print repr(v[0])
	if(v[0]==0):
		continue
	v[2] = v[1]/v[0]
	# print v
	new.write(str(k) + "\t" +str(v[0])+'\t' + str(v[1]) +'\t'+ str(v[2]) + '\t' + ' '.join([str(x) for x in v[3:]]) + "\n")

