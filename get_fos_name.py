import zipfile
import re



all_fields={}

with zipfile.ZipFile("../../../data_science/IIT-BHU/zips/FieldsOfStudy.zip") as z:
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


while(1):
	fosid_input = raw_input("enter id:")
	print(all_fields.get(fosid_input))