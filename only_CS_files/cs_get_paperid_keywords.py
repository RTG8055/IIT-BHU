import zipfile
from functions import bsearch



fos_ids=[]


with open("cs_fos_ids.txt",'r') as file:
	i=0
	for line in file:
		i+=1
		line = line.strip('\r|\n')
		fos_ids.append(line)
		# if(i==10):
			# break
	print i

fos_ids.sort()
print len(fos_ids)

cs_paperid_keyword ={}
with zipfile.ZipFile("../zips/PaperKeywords.zip") as z:
	with z.open("PaperKeywords.txt",'r') as file:
		i=0
		for line in file:
			i+=1
			pid,keyword,fosid = line.strip("\r|\n").split("\t")
			# print i,fosid
			if(bsearch(fosid,fos_ids,0,len(fos_ids)-1) == 0):
				if(cs_paperid_keyword.get(pid)== None):
					cs_paperid_keyword[pid] = [keyword]
				else:
					cs_paperid_keyword[pid].append(keyword)
				# print 
			if(i%1000000==0):
				print i
				# break
		print i
print len(cs_paperid_keyword)


file = open("cs_paperid_keyword.txt",'w')
i=0
for pid,keywords in cs_paperid_keyword.items():
	i+=1
	file.write(pid + "\t" + ",".join(keywords) + "\n")
print i
