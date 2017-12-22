import zipfile

papers={}
file = open("output/sample26/paperids26_70_journals_conf.txt",'r')
i=0
for line in file:
	i+=1
	line = line.strip("\r|\n")
	pid,journal = line.split("\t")
	papers[pid]=[journal]
print i
file.close()

with open("output/sample26/filtered_papers26_with_titles26.txt") as f:
	i=0
	for line in f:
		i+=1
		line= line.strip('\r|\n')
		pid,title = line.split("\t")
		if(papers.get(pid) != None):
			papers[pid].append(title)
	print i

with open("output/sample26/papers_without_ref26_with_titles26.txt") as f:
	i=0
	for line in f:
		i+=1
		line= line.strip('\r|\n')
		pid,title = line.split("\t")
		if(papers.get(pid) != None):
			papers[pid].append(title)
	print i


new = open("output/sample26/papersids26_journals_titles.txt",'w')
i=0
for k,v in papers.items():
	i+=1
	# print k,v
	new.write(str(k) + "\t" + '<--'.join(v) + "\n")
print i
new.close()