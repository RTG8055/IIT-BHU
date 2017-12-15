import zipfile
from functions import bsearch



fos_details={}

# with zipfile.ZipFile("zips/PaperKeywords.zip") as z:
# 	with z.open("PaperKeywords.txt") as f:
with open("../../../MAGNEW/PaperKeywords/PaperKeywords.txt") as f:
	i=0
	for line in f:
		i+=1
		# print line
		pid,keyword,fid = line.split('\t')
		fid = fid.strip('\r|\n')
		if(fos_details.get(fid) == None):
			c = [set(),set()]
			c[0].add(pid)
			c[1].add(keyword)
			fos_details[fid] = c
		else:
			fos_details.get(fid)[0].add(pid)
			fos_details.get(fid)[1].add(keyword)
		if(i%1000000==0):
			print i
		if(i==10000000): # ran on server for all
			break
print i
new = open('fos_papers_keywords_server.txt','w')
i=0
for k,v in fos_details.items():
	i+=1
	# print k,v
	list(v[0]).sort()
	list(v[1]).sort()
	# text file format
	# groupParentID 	listOfPapers listOfKeyowrds

	new.write(str(k)+ '\t'+ str(' '.join(v[0])) + '\t' + str(','.join(v[1])) + '\n')
print len(fos_details)
new.close()
