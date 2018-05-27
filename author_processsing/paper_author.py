import zipfile
# import psutil

authors = set()
# print psutil.virtual_memory()
# with zipfile.ZipFile("no_upload_author_papers.zip") as z:
	# with z.open("author_papers.txt") as f:
with open("author_papers.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		aid,no_papers,papers = line.strip('\r|\n').split('\t')
		# print aid,no_papers,papers
		authors.add(aid)
print len(authors)
# print psutil.virtual_memory()

paper_authors={}

# with zipfile.ZipFile("../zips/PaperAuthorAffiliations.zip") as z:
	# with z.open("PaperAuthorAffiliations.txt") as f:
with open("../../../MAGNEW/PaperAuthorAffiliations.txt") as f:
	i=0
	for line in f:

		i+=1
		if(i%1000000==0):
			print i

		if(i%10000000==0):
			print len(paper_authors)
			# print psutil.virtual_memory()
			# break
			
		#paperid, authorid, affiliationid,original affiliation name, normalized, author sequence number
		pid,aid,afid,afname,_n,asn = line.strip('\r|\n').split('\t')

		if(aid in authors):
			if(paper_authors.get(pid) == None):
				paper_authors[pid] = [aid]
			else:
				paper_authors[pid].append(aid)
		else:
			continue


print len(paper_authors),i

new = open('paper_authors.txt','w')
i=0
for k,v in paper_authors.items():
	i+=1
	# print k,v
	# text file format
	# paper id 	number of authors 	list of authorid
	new.write(str(k)+ '\t'+ str(len(v)) +'\t' + str(' '.join(v))  + '\n')
print i
new.close()