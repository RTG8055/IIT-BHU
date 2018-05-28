# import networkx
import zipfile
import psutil

co_authors = {}
paper_authors = {}
author_list=[]
print psutil.virtual_memory()

with zipfile.ZipFile("no_upload_paper_authors.zip") as z:
	with z.open("paper_authors.txt") as f:
		i=0
		for line in f:
			i+=1
			pid,no_authors,authors = line.strip('\r|\n').split("\t")
			authors = authors.split(' ')
			if(i%1000000==0):
				print i
				print psutil.virtual_memory()
				# break
			if(no_authors < 2):
				print pid
				continue
			paper_authors[pid] = authors
			
			# paper_authors[pid] = i
			# author_list.append(authors)
		print i
print psutil.virtual_memory()


with zipfile.ZipFile("no_upload_author_papers.zip") as z:
	with z.open("author_papers.txt") as f:
		i=0
		for line in f:
			i+=1
			aid,no_papers,papers = line.strip('\r|\n').split('\t')
			papers = papers.strip("[|]|\n|\r")
			papers = papers.split(' ')
			paperids = [p.split('-')[0] for p in papers]
			co_authors[aid] = set()
			if(i%1000==0):
				print i
				break
			for p in paperids:
				co_authors[aid].add(set(paper_authors[p]))
			print psutil.virtual_memory()



		print i,total,psutil.virtual_memory()

print co_authors,len(co_authors),psutil.virtual_memory()

paper_authors.clear()

new = open('co_authors.txt','w')
i=0
for k,v in co_authors.items():
	i+=1
	# print k,v
	# text file format
	# aid 	number of co-authors	list of authorid
	new.write(str(k)+ '\t'+ str(len(v)) +'\t' + str(' '.join(list(v)))  + '\n')
print i
new.close()
