import zipfile
import psutil

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

with open("venue_authors.txt") as f:
	i=0
	for line in f:
		i+=1
		print line

		if(i==10):
			break