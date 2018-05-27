import zipfile
import psutil
import re
# cs_paperids=set()

# with zipfile.ZipFile("../only_CS_files/upload_cs_paperids2.zip") as z:
# 	with z.open("cs_paperids2.txt") as f:
# 		i=0
# 		for line in f:
# 			i+=1
# 			line = line.strip("\r|\n")
# 			# cs_paperids.add(line)
# 			if(i%1000000 == 0):
# 				print psutil.virtual_memory()


# print i
# print psutil.virtual_memory()

# with zipfile.ZipFile("../zips/PaperAuthorAffiliations.zip") as z:
# 	with z.open("PaperAuthorAffiliations.txt") as f:
# 		i=0
# 		for line in f:
# 			i+=1
# 			if(i%1000000 ==0):
# 				print psutil.virtual_memory()
# 			if(i==10000000):
# 				break

# print i
# print psutil.virtual_memory()
with zipfile.ZipFile("no_upload_venue_authors.zip") as z:
	with z.open("venue_authors.txt") as f:
		i=0
		total =0
		for line in f:
			i+=1
			# if(i==1):
				# print i
				# break
				# continue
			# print line
			afid,no_authors_afname,authors = line.strip("\r|\n").split("\t")
			# no_authors = no_authors_afname.match(r"(\d+)(.*)")
			no_authors = int(re.match(r"(\d+).*",no_authors_afname).groups()[0])
			total +=int(no_authors)
			if(i%10000==0):
				print i,total
		print i,total