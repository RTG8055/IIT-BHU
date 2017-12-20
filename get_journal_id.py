import zipfile


paperids={}
papers=set()
with open("output/sample1/paperids1_67.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		line = line.strip('\n|\r')
		# print repr(line)
		paperids[line] = i
		papers.add(line)


print i,paperids

journals={}
conf={}

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
			if(line[0] in papers):
				# print line
				if(line[5] != ''):
					journals[paperids[line[0]]]=line[5]
				if(line[6] != ''):
					conf[paperids[line[0]]]=line[6]
			if(i%1000000 == 0):
				print i
			# if(i==2000000):
				# break
# print paperids,journals,conf
print i,len(paperids),len(journals),len(conf)


j_names={}
with zipfile.ZipFile("zips/Journals.zip") as z:
	with z.open("Journals.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.strip('\r|\n')
			jid,jname = line.split('\t')
			# print line
			if(jid in journals.values()):
				j_names[jid]=jname
			# if(i==1000):
				# break

print j_names,i

c_names={}
with zipfile.ZipFile("zips/Conferences.zip") as z:
	with z.open("Conferences.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.strip('\r|\n')
			# print line
			cid,cshort,cname = line.split('\t')
			if(cid in conf.values()):
				c_names[cid]=cname
			# if(i==1000):
				# break

print c_names,i
new = open("output/sample1/paperids1_67_journals_conf.txt",'w')
# new2=open("output/sample2/paperids2_50_conf.txt",'w')
i=0
for k,v in paperids.items():
	i+=1
	if(journals.get(v) !=None):
		new.write(str(k) + "\t" + j_names.get(journals.get(v)) + "\n")
	elif(conf.get(v) != None):
		new.write(str(k) + "\t" + c_names.get(conf.get(v)) + "\n")
	else:
		new.write(str(k) + "\t" + "Information not present" + "\n")
print i
new.close()