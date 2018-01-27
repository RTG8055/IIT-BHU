import re
import zipfile

pdetails={} 
i=0


act_pid=""
with open("../Result metric -II/output2/sample6/all_papers_titSim.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# print(repr(line))
		reg = re.match(r'(.*),(".*"),(".*"),(.*),(.*)',line,re.M|re.I)
		pid,ptitle,pjournal,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4),reg.group(5)
		sim2=sim2.strip('\n|\r')
		if(float(sim1) == 1.0 or (float(sim2) == 1.0)):
			if(ptitle.strip('"').split(' ')[0] == "Hierarchical" and ptitle.strip('"').split(' ')[1] == "Clustering"):
				print ptitle,"\n enter same as actual or not(y/n)?\n",sim1,sim2
				ch = raw_input()
				if(ch=='y'):
					act_pid = pid
					break

		pdetails[pid]=[ptitle,pjournal,float(sim1),float(sim2)]

papers_to_be_considered=set()
papers_ref={}
i=0
with open("../output/sample6/papers_with_references6.txt",'r') as file:
	for line in file:
		i+=1
		# print line
		pid,refids = line.strip('\n|\r').split("\t")
		# print repr(pid),repr(refids)
		# print refids
		# if(i==3):
			# break
		papers_ref[pid] = refids


for p in papers_ref[act_pid].split(' '):
	# print p
	papers_to_be_considered.add(p)

print papers_to_be_considered

def act_ref(alll):
	new= set()
	for p in alll:
		if(papers_ref.get(p) == None):
			continue
		ref = papers_ref[p].split(' ')
		# print ref
		for r in ref:
			if(r not in alll):
				new.add(r)
	if(len(new) != 0):
		return act_ref(alll | new)
	else:
		return alll
print len(papers_to_be_considered)

papers_to_be_considered = act_ref(papers_to_be_considered)
# papers_to_be_considered.add(papers_ref[act_pid].split(' '))/

print len(papers_to_be_considered)

new = open('output3/sample6/actual_references1.txt','w')
i=0
for k in papers_to_be_considered:
	i+=1
	v1 = pdetails.get(k)
	v2 = papers_ref.get(k)
	if(v2 == None):
		v2 ='0'
	print k,v2
	new.write(k + "\t" +str(len(v2.split(' '))) + "\t" + v2 + "\t" + "\n")
print i
new.close()

i=0
paperids={}
for p in papers_to_be_considered:
	i+=1
	paperids[p]=i


journals={}
conf={}
titles={}
with zipfile.ZipFile("../only_CS_files/no_upload_id_tit_ye_doi_ven_jou_conf_ra.zip") as z:
	with z.open("id_tit_ye_doi_ven_jou_conf_ra.txt",'r') as f:
		i=0
		for line in f:
			i+=1
			line = line.strip('\r|\n')
			line = line.split('\t')
			# print repr(line)
			# line[5] --> journal
			# line[6] --> conf
			if(line[0] in papers_to_be_considered):
				# print line
				if(line[5] != ''):
					journals[paperids[line[0]]]=line[5]
				if(line[6] != ''):
					conf[paperids[line[0]]]=line[6]
				if(line[2] != ''):
					titles[line[0]] = line[1]
			if(i%1000000 == 0):
				print i
			# if(i==1000000):
				# break
# print paperids,journals,conf
print i,len(paperids),len(journals),len(conf),len(titles)


j_names={}
with zipfile.ZipFile("../zips/Journals.zip") as z:
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
with zipfile.ZipFile("../zips/Conferences.zip") as z:
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

new = open("output3/sample6/papers6_titles_journals.txt",'w')
# new3=open("output/sample3/paperids3_560_conf.txt",'w')
i=0
for k,v in paperids.items():
	i+=1
	if(titles.get(k) == None):
		print k,j_names.get(journals.get(v)),c_names.get(conf.get(v))
		continue
	if(journals.get(v) !=None):
		new.write(str(k) + "\t" + j_names.get(journals.get(v)) + "<---"+ titles.get(k)+ "\n")
	elif(conf.get(v) != None):
		new.write(str(k) + "\t" + c_names.get(conf.get(v)) + "<---"+ titles.get(k)+ "\n")
	else:
		new.write(str(k) + "\t" + "Information not present" + "<---"+ titles.get(k)+ "\n")
print i
new.close()