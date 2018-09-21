import zipfile
import sys
myset=set()
with open("bio_paperids.txt",'r') as csid:
	for line in csid:
		line=line.strip('\r|\n')
		# print line
		myset.add(line)
		# print repr(line)
print(len(myset))
i=0
j=0
bio_detail=open("id_tit_ye_doi_ven_jou_conf_ra.txt",'w')
with zipfile.ZipFile("../../MAG Dataset/Papers.zip") as z:
# with zipfile.ZipFile("../zips/Papers.zip") as z:
	with z.open("Papers.txt",'r') as file:
		for line in file:
			i+=1
			if(i%1000000==0):
				print(i)
				# break
			# line=line.decode("utf-8")
			line=line.split('\t')
			if(line[0] in myset):
				bio_detail.write(line[0])
				bio_detail.write('\t')
				try:
					bio_detail.write(line[1])
				except Exception as e:
					print(e)
					j+=1
					print(line[1])
					print(j)
					continue
				bio_detail.write('\t')
				bio_detail.write(line[3])
				bio_detail.write('\t')
				bio_detail.write(line[5])
				bio_detail.write('\t')
				bio_detail.write(line[6])
				bio_detail.write('\t')
				bio_detail.write(line[8])
				bio_detail.write('\t')
				bio_detail.write(line[9])
				bio_detail.write('\t')
				bio_detail.write(line[10])
				# bio_detail.write('\n')
			# if(i==10000):
				# print j
				# break
bio_detail.close()