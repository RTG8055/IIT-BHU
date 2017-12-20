import zipfile


papers=set()
with open("output/sample6/papers6.txt",'r') as f:
	for p in f:
		papers.add(p.strip('\n'))

paper_refernces={}
with zipfile.ZipFile("only_CS_files/no_upload_cs_paper_refernces.zip") as z:
	with z.open("cs_paper_refernces.txt") as f:
		i=0
		for line in f:
			# print line
			line = line.strip("\n")
			pid,refids = line.split('\t')
			# print pid,count,refids
			if(pid in papers):
				papers.remove(pid)
				paper_refernces[pid] = refids
			i+=1
			if(i%1000000 == 0):
				print i
print len(paper_refernces)
new = open('output/sample6/papers_with_references6.txt','w')
i=0
for k,v in paper_refernces.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()