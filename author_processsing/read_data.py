import zipfile


author_papers={}
with zipfile.ZipFile("../zips/PaperAuthorAffiliations.zip") as z:
	with z.open("PaperAuthorAffiliations.txt") as f:
		i=0
		for line in f:
			#paperid, authorid, affiliationid,original affiliation name, normalized, author sequence number
			# print line
			pid,aid,_a,_o,_n,asn = line.strip('\r|\n').split('\t')
			# print repr(pid),repr(aid),repr(asn)
			i+=1
			if(i%100000 ==0):
				print i
			if(author_papers.get(aid) == None):
				author_papers[aid] = [(pid,asn)]
			else:
				author_papers[aid].append((pid,asn))
# print author_papers

new = open('author_papers.txt','w')
i=0
for k,v in author_papers.items():
	i+=1
	v.sort()
	# print k,v
	# text file format
	# author id 	list of (paper, sequence number)
	new.write(str(k)+ '\t'+ str(' '.join([x[0] + '-' + x[1] for x in v]))  + '\n')
print len(author_papers)
new.close()



