import zipfile
import sys
myset=set()
with open("cs_paperids2.txt",'r') as csid:
	for line in csid:
		line=line.strip('\r|\n')
		myset.add(line)
		# print repr(line)
i=0
j=0
csdetail=open("id_tit_ye_doi_ven_jou_conf_ra.txt",'w')
with zipfile.ZipFile("../zips/Papers.zip") as z:
	with z.open("Papers.txt",'r') as file:
		for line in file:
			i+=1
			if(i%1000000==0):
				print(i)
			# line=line.decode("utf-8")
			line=line.split('\t')
			if(line[0] in myset):
				csdetail.write(line[0])
				csdetail.write('\t')
				try:
					csdetail.write(line[1])
				except Exception as e:
					print e
					j+=1
					print(line[1])
					print(j)
					continue
				csdetail.write('\t')
				csdetail.write(line[3])
				csdetail.write('\t')
				csdetail.write(line[5])
				csdetail.write('\t')
				csdetail.write(line[6])
				csdetail.write('\t')
				csdetail.write(line[8])
				csdetail.write('\t')
				csdetail.write(line[9])
				csdetail.write('\t')
				csdetail.write(line[10])
				# csdetail.write('\n')
			# if(i==10000):
				# print j
				# break
csdetail.close()