import json
import re
import zipfile

x={}
enm=open("Paperid_paperrefid.txt",'w')
# with zipfile.ZipFile("zips/PaperReferences.zip") as z:
	# with z.open("PaperReferences.txt",'r') as f:
with open("../../../MAGNEW/PaperKeywords/PaperKeywords.txt") as f:
	i=0
	c=[]
	for line in f:
		i+=1
		line=line.decode("utf-8")
		l=line.split('\t')
		l[0]=l[0].strip()
		l[1]=l[1].strip()
		if(x.get(l[0])==None):
			x[l[0]]=[]
			x[l[0]].append(0)
		else:
			x[l[0]][0]+=1
			x[l[0]].append(l[1])
		print(i)
y=0
for v,k in x.items():
	if(k[0]==0):
		continue
	enm.write(str(v))
	enm.write('\t')
	enm.write(str(k[0]))
	enm.write('\t')
	for j in k[1:]:
		enm.write(str(j))
		enm.write(' ')
	enm.write('\n')
enm.close()