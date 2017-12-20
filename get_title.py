import zipfile
from functions import bsearch
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')



papers_without_ref=set()
with open("output/sample6/paper_without_references6.txt",'r') as f:
	for p in f:
		papers_without_ref.add(p.strip('\n'))

filtered_papers=set()
with open("output/sample6/filtered_papers_5measures.txt",'r') as f:
	for p in f:
		filtered_papers.add(p.strip('\n'))


paper_titles_without_ref={}
filtered_papers_title={}
with zipfile.ZipFile("only_CS_files/no_upload_id_tit_ye_doi_ven_jou_conf_ra.zip") as z:
	with z.open("id_tit_ye_doi_ven_jou_conf_ra.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.split('\t')
			# print repr(line[0])

			if line[0] in papers_without_ref:
				papers_without_ref.remove(line[0])
				paper_titles_without_ref[line[0]] = line[1]

			if line[0] in filtered_papers:
				filtered_papers.remove(line[0])
				filtered_papers_title[line[0]] = line[1]

			if(i%1000000 == 0):
				print i
			# if(i==100):
				# break
print i
# print paper_titles_without_ref
new = open('output/sample6/papers_without_ref6_with_titles6.txt','w')
i=0
for k,v in paper_titles_without_ref.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()

new = open('output/sample6/filtered_papers6_with_titles6.txt','w')
i=0
for k,v in filtered_papers_title.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()