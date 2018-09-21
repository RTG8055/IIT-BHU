import zipfile

file = open("cs_paperids2.txt",'r')
cs_papers=set()
i=0
for line in file:
	i+=1
	cs_papers.add(line.strip('\r|\n'))
	if(i%1000000==0):
		print i
	# print repr(line)
	# break
print len(cs_papers)

paper_refernces={}
with zipfile.ZipFile("../zips/paper_no_refernces_refernces.zip") as z:
	with z.open("paper_no_refernces_refernces.txt") as f:
		i=0
		for line in f:
			# print line
			line = line.strip("\n")
			pid,count,refids = line.split('\t')
			# print pid,count,refids
			if(pid in cs_papers):
				cs_papers.remove(pid)
				paper_refernces[pid] = refids
			i+=1
			if(i%1000000 == 0):
				print i

			# if(i==10000):
				# break
print len(paper_refernces)

new = open("cs_paper_refernces.txt",'w')
i=0
for k,v in paper_refernces.items():
	new.write(k + '\t' + v + '\n')
	i+=1
print i