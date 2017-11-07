import zipfile
import json
import re

new = open("IR_paperIDs",'w')
p=[]
FOSids = open("FOS_for_IR.txt",'r')
fosid=[]
for line in FOSids:
	if(line == '\n'):
		continue
	l=line.split(')')
	# print l
	# fid,keyword = l[1].split('\t')

	fosid.append(l[1][0:8])
# print fosid
with zipfile.ZipFile("zips/PaperKeywords.zip") as z:
	with z.open("PaperKeywords.txt") as f:
		i=0
		for line in f:
			i+=1
			# print line
			pid,keyword,fid = line.split('\t')
			# print fid
			# print keyword
			# print fosid
			match = re.search(r'\binformation\b \bretrieval\b',keyword,re.M|re.I)
			if match:
				# print fid,keyword
				p.append(pid)
			# match = re.search(r'\bretrieval\b',keyword,re.M|re.I)
			# if match:
			# 	print fid,keyword
			# 	p.append(pid)

			if(fid in fosid):
				print fid
				p.append(pid)
			# if(i==100000):
				# break
print "paperIDs"
for i in p:
	print i
	new.write(str(i)+'\n')
new.close()


