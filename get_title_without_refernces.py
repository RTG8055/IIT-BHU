import zipfile
from functions import bsearch
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')



papers=set()
# with open("output/papers1.txt",'r') as f:
with open("output/paper_without_references1.txt",'r') as f:
	for p in f:
		papers.add(p.strip('\n'))
# papers.sort()
print len(papers)
paper_titles={}
with zipfile.ZipFile("only_CS_files/no_upload_id_tit_ye_doi_ven_jou_conf_ra.zip") as z:
	with z.open("id_tit_ye_doi_ven_jou_conf_ra.txt") as f:
		i=0
		for line in f:
			i+=1
			line = line.split('\t')
			# print repr(line[0])

			# if(bsearch(line[0],papers,0,len(papers)) == 1):
				# papers
			if line[0] in papers:
				papers.remove(line[0])
				paper_titles[line[0]] = line[1]

			if(i%1000000 == 0):
				print i
			# if(i==100):
				# break
print i
# print paper_titles
new = open('output/papers_without_refernces_titles1.txt','w')
i=0
for k,v in paper_titles.items():
	i+=1
	new.write(k + "\t" + v + "\n")
print i
new.close()