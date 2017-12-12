import zipfile




papers = {}
# with zipfile.ZipFile("zips/PaperReferences.zip") as z:
	# with z.open("PaperReferences.txt") as f:
with open("../../../MAGNEW/PaperReferences/PaperReferences.txt") as f:

	i=0
	for line in  f:
		i+=1
		# print line
		pid,refID = line.split('\t')
		refID = refID.strip('\r|\n')
		# print pid,repr(refID)

		if(papers.get(pid) == None):
			c=[1]
			c.append(refID)
			papers[pid] =c
		else:
			temp = papers.get(pid)
			temp[0]+=1
			temp.append(refID)
		if(i%100000 == 0):
			print "line " + str(i)
		# if(i==1000000):
			# break

new = open("paper_no_refernces_refernces.txt",'w')

for k,v in papers.items():
	v[1:].sort()
	new.write(str(k) + "\t" + str(v[0]) + "\t" + ' '.join(v[1:]) + "\n")
new.close()