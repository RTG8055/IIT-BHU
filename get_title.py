import zipfile
from functions import bsearch

papers=set()
with open("output/papers.txt",'r') as f:
	for p in f:
		papers.add(p.strip('\n'))
# papers.sort()

paper_titles={}
with zipfile.ZipFile("zips/Papers.zip") as z:
	with z.open("Papers.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.split('\t')
			# print repr(line[0])

			# if(bsearch(line[0],papers,0,len(papers)) == 1):
				# papers
			if line[0] in papers:
				papers.remove(line[0])
				paper_titles[line[0]] = line[1]

			if(i%1000000 == 0):
				print i
			# if(i==100):
				# break
print i
# print paper_titles
new = open('output/papers_with_titles.txt','w')
i=0
for k,v in paper_titles.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()