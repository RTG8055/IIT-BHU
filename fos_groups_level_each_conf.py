import zipfile
import re


groups={}
l0=0
l1=0
l2=0
l3=0

with zipfile.ZipFile("zips/FieldsOfStudy.zip") as z, zipfile.ZipFile("zips/FieldOfStudyHierarchy.zip") as z2:
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
				levels = [[0,0,0],[0,0,0],[0,0,0]]
				# groups[parentFOSid] = levels
				# 0th element is the number of fields in that level
				# 1th element is the total of the fields in that level
				c=[0,0,0]
				c[0]=c[0]+1
				c[1]=c[1]+float(conf)
				c.append((childFOSid,float(conf)))
				if(int(childFOSlevel)==1):
					l1+=1
					levels[0]= c
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
				# for d in [0,1,2]:
				h=0
				for j in x[int(childFOSlevel)-1]:
					h+=1
					if(h<=3): # skip the indexes with count, total and average
						continue
					if(j[0].strip() == childFOSid):
						alreadythere=True
						break
				if(alreadythere):
					print "abcd"
					break
				if(not alreadythere):
					temp = x[int(childFOSlevel)-1]
					temp[0]=temp[0]+1
					temp[1]=temp[1]+float(conf)
					temp.append((childFOSid,float(conf)))
					x[int(childFOSlevel)-1] = temp
					groups[parentFOSid] = x
			# if(i==100):
				# break
			if(i%10000 == 0):
				print i
print i

new = open("FOS_groups_level_each_conf.txt",'w')
i=0
for k, v in groups.items():
	print v
	if(v[0][0]!=0):
		v[0][2] = v[0][1]/v[0][0]
	if(v[1][0]!=0):
		v[1][2] = v[1][1]/v[1][0]
	if(v[2][0]!=0):
		v[2][2] = v[2][1]/v[2][0]
	v[0][3:].sort()
	v[1][3:].sort()
	v[2][3:].sort()
	v[0][0] = str(v[0][0])
	v[1][0] = str(v[1][0])
	v[2][0] = str(v[2][0])
	v[0][1] = str(v[0][1])
	v[1][1] = str(v[1][1])
	v[2][1] = str(v[2][1])
	v[0][2] = str(v[0][2])
	v[1][2] = str(v[1][2])
	v[2][2] = str(v[2][2])
	
	# text file format
	# parentFOSid 		listOfChildFOSIDs
	new.write(str(k) + '\t'+ str(';'.join(v[0][0:3])) + ";" + str(v[0][3:]) + '\t' + str(';'.join(v[1][0:3])) + ";" + str(v[1][3:]) + '\t' + str(';'.join(v[2][0:3])) + ";" + str(v[2][3:]) + '\n\n')
	i+=1
new.close()
print l0," ",l1," ",l2," ",l3