import zipfile


papers=set()
# with open("output/papers.txt",'r') as f:
	# for p in f:
		# papers.add(p.strip('\n'))

with open("Rugved/1692/toppapers_averagesimilarity_and_1692.csv",'r') as f:
	i=0
	for line in f:
		i+=1
		papers.add(line.split(",")[0])
print i


paper_refernces={}
with zipfile.ZipFile("only_CS_files/cs_paper_refernces.zip") as z:
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

			# if(i==10000):
				# break
print paper_refernces
new = open('Rugved/1692/papers_with_references_1692_andSimilarity.txt','w')
i=0
for k,v in paper_refernces.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()