import zipfile
import json
import re


new = open("FOS_topic.txt",'w')
only_IR={}
all_fields={}
with zipfile.ZipFile("zips/FieldsOfStudy.zip") as z, zipfile.ZipFile("zips/FieldOfStudyHierarchy.zip") as z2:
	with z.open("FieldsOfStudy.txt") as f, z2.open("FieldOfStudyHierarchy.txt") as f2:
		i=0
		for line in f:
			# print line;
			studyID,studyName = line.split('\t')
			if(studyName == None or studyName == "None"):
				continue
			i=i+1;
			x=[]
			x.append(studyName)
			# words = studyName.split()
			all_fields[studyID]=studyName
			match = re.search(r'\binformation\b \bretrieval\b',studyName,re.M|re.I)
			if match:
				only_IR[studyID]=x


			# if(studyName)
			# if(i==1000):
				# break
		i=0
		for line in f2:
			# print line
			childFOSid,childFOSlevel,parentFOSid,parentFOSlevel,conf = line.split('\t')
			i=i+1;
			x={}
			if(only_IR.get(parentFOSid)!=None):
				# x = [childFOSid,all_fields.get(childFOSid)]
				# x[parentFOSid]= only_IR[parentFOSid]
				x[childFOSid] = all_fields.get(childFOSid)
				# y= only_IR[parentFOSid]
				# y=dict(y.items()+x.items())
				# only_IR[parentFOSid] = y
				only_IR.update(x)
				print x
			# if(d.get(parentFOSid) != None):
				# print d.get(parentFOSid),parentFOSid
				# d[parentFOSid]=d[parentFOSid].append(childFOSid)
				print "found"
			# if(i==1000):
				# break
			
# print d
i=0
for k, v in only_IR.items():
	print v
	new.write(str(i)+ ")" + str(k) + '\t'+ str(v) + '\n\n')
	i+=1
# new.write(json.dumps(d))
new.close()

