import re

pdetails={}
sum1=0
sum2=0
i=0
with open("output/sample2/filtered_papers_titSim.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# print(repr(line))
		reg = re.match(r'(.*),(".*"),(.*),(.*)',line,re.M|re.I)
		pid,ptitle,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4)
		sim2=sim2.strip('\n|\r')
		pdetails[pid]=[ptitle,float(sim1),float(sim2)]
		sum1+=float(sim1)
		sum2+=float(sim2)
avg1=sum1/(i-1)
avg2=sum2/(i-1)

print avg1,avg2

paperids_or=set()
for k,v in pdetails.items():
	if v[1] >avg1:
		paperids_or.add(k)
		# new.write(k+','+','.join(v)+'\n')
	if(v[2]>avg2):
		paperids_or.add(k)
		# new.write(k+','+','.join(v)+'\n')


new=open("output/sample2/filtered_papers_titSim_or_avg.csv",'w')
i=0
for k,v in pdetails.items():
	# i+=1
	if( k in paperids_or):
		i+=1
		new.write(k+','+v[0] +','+str(v[1]) +','+str(v[2]) +'\n')
print i,"written papers greater than avg of sim1 or sim2"
new.close()


sim1_pdetails={}
sim2_pdetails={}
i=0
with open("output/sample2/papers_without_refernces_titSim.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# print(repr(line))
		reg = re.match(r'(.*),(".*"),(.*),(.*)',line,re.M|re.I)
		pid,ptitle,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4)
		sim2=sim2.strip('\n|\r')

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


new=open("output/sample2/paperids_without_ref_or_20.txt",'w')
i=0
for k in topset:
	i+=1
	new.write(k+'\n')
print i,"written papers top 10 of each sim1 and sim2"
new.close()
