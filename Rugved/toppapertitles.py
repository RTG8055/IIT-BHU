import sys  

reload(sys)  
sys.setdefaultencoding('utf8')



papers=set()
with open("toppapers.txt",'r') as file:
	for p in file:
		papers.add(p.strip('\n'))
# papers.sort()

paper_titles={}
with open("../output/papers_with_titles.txt") as file:
	i=0
	for line in file:
		i+=1
		line = line.split('\t')
		# print repr(line[0])
			# if(bsearch(line[0],papers,0,len(papers)) == 1):
			# papers
		if line[0] in papers:
			papers.remove(line[0])
			paper_titles[line[0]] = line[1]
		if(i%1000 == 0):
			print i
		# if(i==100):
			# break
print i
# print paper_titles
new = open("toppapertitles_1692.txt",'w')
i=0
for k,v in paper_titles.items():
	i+=1
	new.write(k + "\t" + v)
print i
new.close()	