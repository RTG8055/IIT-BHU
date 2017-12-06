import zipfile
import json
import re

def bsearch(id,all,k,l):
	if(k<l):
		mid = k + (l-k)/2
		# print k,l,mid
		# print id,all[mid]
		if(id.strip() == all[mid]):
			return 1;
		elif(id < all[mid]):
			l = mid
			return bsearch(id,all,k,l)
		elif(id>all[mid]):
			k=mid+1
			return bsearch(id,all,k,l)
	else:
		return 0;


new = open("IR_paperIDs2",'w')
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
print fosid
fosid.sort()
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
			# match = re.search(r'\binformation\b \bretrieval\b',keyword,re.M|re.I)
			# if match:
				# print fid,keyword
				# print fosid[6]
				# print fid.strip() == fosid[6]
				# print type(fid)
				# print type(fosid[6])
				# p.append(pid)
			# match = re.search(r'\bretrieval\b',keyword,re.M|re.I)
			# if match:
			# 	print fid,keyword
			# 	p.append(pid)
			if(bsearch(fid,fosid,0,len(fosid)-1) == 1):
				# if(str(fid) in fosid):
				print fid,"found"
				p.append(pid)
				
			# if(bsearch(fid,fosid,0,len(fosid)-1) == 1):
			# if(str(fid) in fosid):
				# print fid
			# if(i==100000):
				# break
print "paperIDs"
print p
for i in p:
	print i
	new.write(str(i)+'\n')
new.close()


