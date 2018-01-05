import re

pdetails={}
i=0

sim1_pdetails={}
sim2_pdetails={}

with open("output2/sample5/all_papers_titSim.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# print(repr(line))
		reg = re.match(r'(.*),(".*"),(".*"),(.*),(.*)',line,re.M|re.I)
		pid,ptitle,pjournal,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4),reg.group(5)
		sim2=sim2.strip('\n|\r')
		sim1_pdetails[pid]=float(sim1)
		sim2_pdetails[pid]=float(sim2)
		pdetails[pid]=[ptitle,pjournal,float(sim1),float(sim2)]

topset=set()

i=0
for j in (sorted(sim1_pdetails,key=sim1_pdetails.__getitem__,reverse=True)):
	if(i<500):
		topset.add(j)
	else:
		break
	i+=1

print len(topset)

i=0
for j in (sorted(sim2_pdetails,key=sim2_pdetails.__getitem__,reverse=True)):
	if(i<500):
		topset.add(j)
	else:
		break
	i+=1

print len(topset)


new=open("output2/sample5/top_papers5.txt",'w')
i=0
for k in topset:
	i+=1
	new.write(k + '\t' + '\t'.join(str(x) for x in pdetails[k]) +'\n')
print i,"written papers top 500 of each sim1 and sim2"
new.close()
