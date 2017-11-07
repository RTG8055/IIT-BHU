import zipfile
import json
import re

file = open("IR_paperIDs",'r')
all_pid=[]
for line in file:
	all_pid.append(line[:-1])
file.close()
new = open("paper_details.txt",'w')
p_det={}
print all_pid
with zipfile.ZipFile("zips/Papers.zip") as z:
	with z.open("Papers.txt") as f:
		i=0
		for line in f:
			i+=1
			if(i==1001):
				break
			l = line.split('\t')
			print "checking paper number ",i
			x=[]
			# print l[0]

			if (l[0] in all_pid):
				x.append(l[1])
				x.append(l[3])
				x.append(l[6])
				print i, "matched paper id", l[0]
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

# for k,v in p_det.items():
# 	new.write(k)
# 	new.write('\t')
# 	for i in v:
# 		new.write(i)
# 		new.write('\t')
# 	new.write('\n')


new.close()
