import re
import json
import zipfile

x={}
files=open("400paper_referenceids.txt",'w')
with open("paperid_paperreferenceid.txt",'r') as file:
	for line in file:
		l=line.split('\t')
		if(x.get(l[0])==None):
			x[l[0]]=[]
		else:
			x[l[0]].append(l[2])
with open("	/pids.csv",'r') as p:
	for lines in p:
		li=lines.split(',')
		x[li[0]]
		files.write(str(li[0]))
		files.write(x[li[0]])
files.close()