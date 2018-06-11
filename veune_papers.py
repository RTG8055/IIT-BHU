import zipfile

# with zipfile.ZipFile("only_CS_files/no_upload_id_tit_ye_doi_ven_jou_conf_ra.zip") as z:
# 	with z.open("id_tit_ye_doi_ven_jou_conf_ra.txt") as f:

# 		i=0
# 		for line in file:
# 			i+=1
# 			line = line.split('\t')
			
venues={}
x=0
with zipfile.ZipFile("only_CS_files/no_upload_id_tit_ye_doi_ven_jou_conf_ra.zip") as z:
	with z.open("id_tit_ye_doi_ven_jou_conf_ra.txt",'r') as f:
		i=0
		for line in f:
			i+=1
			line = line.strip('\r|\n')
			line = line.split('\t')
			# print repr(line)
			# line[5] --> journal
			# line[6] --> conf
			# if(line[0] in papers):
				# print line
			# if(line[5] != ''):
			# 	journals[paperids[line[0]]]=line[5]
			# if(line[6] != ''):
			# 	conf[paperids[line[0]]]=line[6]
			if(line[6]!=''):
				continue
			if(line[4]==''):
				# print i
				x+=1
				continue
			if(venues.get(line[4]) == None):
				venues[line[4]] = 1
			else:
				venues[line[4]] +=1
			# if(line[2] != ''):
			# 	titles[line[0]] = line[1]
			if(i%1000000 == 0):
				print i
			# break
			# if(i==1000000):
				# break
# print paperids,journals,conf
print i,len(venues),x


count1=0
count2=0
count3=0
i=0
for k,v in venues.items():
	i+=1
	if(i%100000==0):
		print i
	if(v<=3):
		count1+=1
	elif(v<10):
		count2+=1
	else:
		count3+=1
print "count1:",count1
print "count2:",count2
print "count3:",count3



# j_names={}
# with zipfile.ZipFile("zips/Journals.zip") as z:
# 	with z.open("Journals.txt") as f:
# 		i=0
# 		for line in f:
# 			i+=1
# 			line = line.strip('\r|\n')
# 			jid,jname = line.split('\t')
# 			# print line
# 			if(jid in journals.values()):
# 				j_names[jid]=jname
# 			# if(i==1000):
# 				# break

# print len(j_names),i

# c_names={}
# with zipfile.ZipFile("zips/Conferences.zip") as z:
# 	with z.open("Conferences.txt") as f:
# 		i=0
# 		for line in f:
# 			i+=1
# 			line = line.strip('\r|\n')
# 			# print line
# 			cid,cshort,cname = line.split('\t')
# 			if(cid in conf.values()):
# 				c_names[cid]=cname
# 			# if(i==1000):
# 				# break

# print len(c_names),i