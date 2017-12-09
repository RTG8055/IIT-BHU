import zipfile
import re



all_fields={}

with zipfile.ZipFile("zips/FieldsOfStudy.zip") as z:
	with z.open("FieldsOfStudy.txt") as f:
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
			if(i==100000):
				break

inv_map = {v: k for k, v in all_fields.iteritems()}
while(1):
	name = raw_input("enter FOS name:")
	print(inv_map.get(name))
	fosid_input = raw_input("enter id:")
	print(all_fields.get(fosid_input))