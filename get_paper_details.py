import zipfile
import json
import re
from functoins import bsearch



file = open("IR_IDs2_sorted",'r')
all_pid=[]
for line in file:
	all_pid.append(line[:-1])
file.close()
new = open("paper_details2.txt",'w')
p_det={}
print all_pid
with zipfile.ZipFile("zips/Papers.zip") as z:
	with z.open("Papers.txt") as f:
		i=0
		k=0
		for line in f:
			i+=1
			# if(i==100001):
				# break
			l = line.split('\t')
			print "checking paper number ",i
			x=[]
			# print l[0]
			if(bsearch(l[0],all_pid,0,len(all_pid)-1) == 1):
			# if (l[0] in all_pid):
				k=k+1
				x.append(l[1])
				x.append(l[3])
				x.append(l[6])
				print k, "matched paper id", l[0]
				if (l[8]== ''):
					x.append(l[9])
				else:
					x.append(l[8])
				x.append(l[10])
				p_det[l[0]] = x
				new.write(l[0])
				new.write('\t')
				for j in x:
					new.write(j)
					new.write('\t')
				new.write('\n')
			# if(l[0] == '7ED39B38'):
				# break

# for k,v in p_det.items():
# 	new.write(k)
# 	new.write('\t')
# 	for i in v:
# 		new.write(i)
# 		new.write('\t')
# 	new.write('\n')


new.close()
