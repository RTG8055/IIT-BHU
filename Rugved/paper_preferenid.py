from itertools import islice
import zipfile
x={}
files=open("400paper_referenceids.txt",'w')
i=0
#with zipfile.ZipFile("Paperid_paperrefid_whole.zip") as z:
with open("Paperid_paperrefid_whole.txt",'r') as file:
	print("inside")#while True:#line = list(islice(file, 1))
	# firstl=file.readline()
	# next(file)
	# file.next()
	for line in islice(file,2,None):
		i+=1
		# print(line)
		if(i==1):
			continue
		#print(repr(line))
		l=line.split('\t')
		print(l)
		l[0]=l[0].strip()
		l[2]=l[2].strip()
		if(x.get(l[0])==None):
			x[l[0]]=[]
		else:
			x[l[0]].append(l[2])
		if(i==10):
			break
j=0
with open("pids.csv",'r') as p:
	for lines in p:
		#print(lines)
		j+=1
		if(j==1):
			continue
		li=lines.split(',')
		files.write(str(li[0]))
		files.write('\t')
		files.write(str(x.get(li[0])))
		files.write('\n')
files.close()
