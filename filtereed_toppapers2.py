import re

sim1_pdetails={}
sim2_pdetails={}
i=0
filtered_papers2=set()
with open("output/sample2/filtered_paper_without_references2.txt",'r') as file:
	for line in file:
		line = line.strip('\r|\n')
		filtered_papers2.add(line)

with open("output/sample2/filtered_papers_titSim.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# print(repr(line))
		reg = re.match(r'(.*),(".*"),(.*),(.*)',line,re.M|re.I)
		pid,ptitle,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4)
		sim2=sim2.strip('\n|\r')
		if(pid in filtered_papers2):
			sim1_pdetails[pid]=float(sim1)
			sim2_pdetails[pid]=float(sim2)

topset=set()

i=0
for j in (sorted(sim1_pdetails,key=sim1_pdetails.__getitem__,reverse=True)):
	if(i<10):
		topset.add(j)
	else:
		break
	i+=1

print len(topset)

i=0
for j in (sorted(sim2_pdetails,key=sim2_pdetails.__getitem__,reverse=True)):
	if(i<10):
		topset.add(j)
	else:
		break
	i+=1

print len(topset)


new=open("output/sample2/filtered_paperids_with_ref_20.txt",'w')
i=0
for k in topset:
	i+=1
	new.write(k+'\n')
print i,"written papers top 10 of each sim1 and sim2"
new.close()