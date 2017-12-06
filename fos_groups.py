import zipfile
import re


new = open("FOS_groups_level_sorted.txt",'w')
groups={}
l0=0
l1=0
l2=0
l3=0

with zipfile.ZipFile("../../../data_science/IIT-BHU/zips/FieldsOfStudy.zip") as z, zipfile.ZipFile("../../../data_science/IIT-BHU/zips/FieldOfStudyHierarchy.zip") as z2:
	with z.open("FieldsOfStudy.txt") as f, z2.open("FieldOfStudyHierarchy.txt") as f2:
		i=0
		for line in f2:
			# print line
			childFOSid,childFOSlevel,parentFOSid,parentFOSlevel,conf = line.split('\t')
			i=i+1;
			childFOSlevel =  childFOSlevel[1:]
			parentFOSlevel = parentFOSlevel[1:]
			if(groups.get(parentFOSid)==None):
				# first time the parent fos id is found make a new group by creating a list with 3 dictionaries l1,l2,l3
				levels = [[],[],[]]
				# groups[parentFOSid] = levels
				c=[]
				c.append(childFOSid)
				if(int(childFOSlevel)==1):
					levels[0]= c
					l1+=1
				elif(int(childFOSlevel) == 2):
					levels[1] = c
					l2+=1
				elif(int(childFOSlevel) == 3):
					levels[2] = c
					l3+=1
				groups[parentFOSid] = levels
				if(int(parentFOSlevel) == 0):
					l0+=1;
					# print parentFOSid
				elif(int(parentFOSlevel)==1):
					l1+=1
				elif(int(parentFOSlevel) == 2):
					l2+=1
				elif(int(parentFOSlevel) == 3):
					l3+=1

			else:
				x=groups[parentFOSid] #get the list of levels in which each is a list of  already existing children
				alreadythere=False
				if(int(childFOSlevel)==1):
					l1+=1
				elif(int(childFOSlevel) == 2):
					l2+=1
				elif(int(childFOSlevel) == 3):
					l3+=1

				# check in all the levels if already exists
				for d in [0,1,2]:
					for j in x[d]:
						if(j.strip() == childFOSid):
							alreadythere=True
							break
					if(alreadythere):
						break
				if(not alreadythere):
					temp = x[int(childFOSlevel)-1]
					temp.append(childFOSid)
					x[int(childFOSlevel)-1] = temp
					groups[parentFOSid] = x

			# if(i==1000):
				# break
		# print groups

i=0
for k, v in groups.items():
	print v
	v[0].sort()
	v[1].sort()
	v[2].sort()
	# text file format
	# parentFOSid 		listOfChildFOSIDs
	new.write(str(k) + '\t'+ str(v[0]) + '\t' + str(v[1]) + '\t' + str(v[2]) + '\n\n')
	i+=1
new.close()
print l0," ",l1," ",l2," ",l3