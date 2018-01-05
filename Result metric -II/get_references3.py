import zipfile


papers=set()
# with open("output/sample2/papers2.txt",'r') as f:
# 	for p in f:
# 		papers.add(p.strip('\n'))

with open("output2/sample5/top_papers5.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		papers.add(line.split("\t")[0].strip('"'))
print i,papers


paper_refernces={}
with zipfile.ZipFile("../only_CS_files/no_upload_cs_paper_refernces.zip") as z:
# with open("output2/sample5/papers_with_references61.txt",'r') as f:
	with z.open("cs_paper_refernces.txt") as f:
		i=0
		for line in f:
			# print line
			line = line.strip("\n")
			pid,refids = line.split('\t')
			if(pid in papers):
				papers.remove(pid)
				paper_refernces[pid] = refids
			i+=1
			if(i%1000000 == 0):
				print i

			# if(i==10000):
				# break
print len(papers),i,len(paper_refernces)

new = open('output2/sample5/top_papers_references5.txt','w')
i=0
for k,v in paper_refernces.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()