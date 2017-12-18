import zipfile

# file = open("cs_paperids2.txt",'r')
papers = set()
with zipfile.ZipFile("upload_cs_paperids2.zip") as z:
	with z.open("cs_paperids2.txt",'r') as file:
		i=0
		for line in file:
			i+=1
			line = line.strip("\n|\r")
			papers.add(line)
			# if(i==10):
				# break
			if(i%1000000==0):
				print i
# print papers
# papers.add("750851DD")

cs_paper_url={}

# with zipfile.ZipFile("../zips/PaperUrls.zip") as z:
# 	with z.open("PaperUrls.txt",'r') as f:
with open("../../../MAGNEW/PaperUrls/PaperUrls.txt") as f:
	i=0
	j=0
	for line in f:
		i+=1
		pid,url = line.split('\t')
		url = url.strip("\n|\r")
		if pid in papers:
			j+=1
			# print repr(pid),repr(url)
			# print cs_paper_url.get(pid)
			if(cs_paper_url.get(pid) == None):
				# print [url]
				cs_paper_url[pid] = [url]
				# print cs_paper_url
			else:
				c =cs_paper_url[pid]
				# print c
				c.append(url)
				cs_paper_url[pid] = c
				# print cs_paper_url
		# if(i==10):
			# break
		if(i%1000000==0):
			print i

print i,j

new = open("upload_cs_papers_urls.txt",'w')
i=0
for k,v in cs_paper_url.items():
	i+=1
	new.write(str(k) + "\t" + ' '.join(v) + "\n")
print i