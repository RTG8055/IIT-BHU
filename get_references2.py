import zipfile


papers=set()
# with open("output/sample2/papers2.txt",'r') as f:
# 	for p in f:
# 		papers.add(p.strip('\n'))

with open("output/sample61/filtered_papers_titSim_or_avg.csv",'r') as f:
	i=0
	for line in f:
		i+=1
		papers.add(line.split(",")[0])
print i


paper_refernces={}
# with zipfile.ZipFile("only_CS_files/no_upload_cs_paper_refernces.zip") as z:
with open("output/sample61/papers_with_references61.txt",'r') as f:
	# with z.open("cs_paper_refernces.txt") as f:
	i=0
	for line in f:
		# print line
		line = line.strip("\n")
		pid,refids = line.split('\t')
		if(pid in papers):
			papers.remove(pid)
			paper_refernces[pid] = refids
		i+=1
		if(i%1000 == 0):
			print i

		# if(i==10000):
			# break
print papers,i

new = open('output/sample61/filtered_papers_with_references61.txt','w')
i=0
for k,v in paper_refernces.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()