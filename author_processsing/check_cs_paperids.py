import zipfile
cs_paperids=set()

with zipfile.ZipFile("../only_CS_files/upload_cs_paperids2.zip") as z:
	with z.open("cs_paperids2.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.strip("\r|\n")
			cs_paperids.add(line)

print len(cs_paperids),i
count=0
with zipfile.ZipFile("../only_CS_files/no_upload_id_tit_ye_doi_ven_jou_conf_ra.zip") as z:
	with z.open("id_tit_ye_doi_ven_jou_conf_ra.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.split('\t')
			# print repr(line[0])

			print repr(line[1])
			if line[0] in cs_paperids:
				count+=1
				# print "found"

			if(i%1000000 == 0):
				print i,count
				break
print count