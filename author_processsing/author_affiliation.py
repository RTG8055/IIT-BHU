import zipfile
import psutil

authors = set()
print psutil.virtual_memory()
with zipfile.ZipFile("author_papers.zip") as z:
	with z.open("author_papers.txt") as f:
# with open("author_papers.txt",'r') as f:
		i=0
		for line in f:
			i+=1
			aid,no_papers,papers = line.strip('\r|\n').split('\t')
			# print aid,no_papers,papers
			authors.add(aid)
print len(authors)
print psutil.virtual_memory()

venue_authors={}

with zipfile.ZipFile("../zips/PaperAuthorAffiliations.zip") as z:
	with z.open("PaperAuthorAffiliations.txt") as f:
# with open("../../../MAGNEW/PaperAuthorAffiliations/PaperAuthorAffiliations.txt") as f:
		i=0
		for line in f:

			i+=1
			if(i%1000000==0):
				print i
			if(i%10000000==0):
				print psutil.virtual_memory()
				
			#paperid, authorid, affiliationid,original affiliation name, normalized, author sequence number
			_p,aid,afid,afname,_n,asn = line.strip('\r|\n').split('\t')

			if(aid in authors):
				if(venue_authors.get(afid) == None):
					venue_authors[afid] = [afname, set()]
					venue_authors[afid][1].add(aid)
				else:
					venue_authors[afid][1].add(aid)
			else:
				continue


print len(venue_authors),i

new = open('venue_authors.txt','w')
i=0
for k,v in venue_authors.items():
	i+=1
	# print k,v
	# text file format
	# affiliation id 	number of authors	affilation_name		list of authorid
	new.write(str(k)+ '\t'+ str(len(v[1])) +'\t' + v[0]+ '\t' + str(' '.join(list(v[1])))  + '\n')
print i
new.close()
