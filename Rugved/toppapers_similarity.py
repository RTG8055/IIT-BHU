import re

pdetails={}
sum1=0
sum2=0
i=0
with open("toppaper_with_title_similarity_1692.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		print(repr(line))
		reg = re.match(r'(.*),(".*"),(.*),(.*)',line,re.M|re.I)
		pid,ptitle,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4)
		sim2=sim2.strip('\n|\r')
		pdetails[pid]=[ptitle,float(sim1),float(sim2)]
		sum1+=float(sim1)
		sum2+=float(sim2)
avg1=sum1/(i-1)
avg2=sum2/(i-1)
print avg1,avg2
new=open("toppapers_averagesimilarity_or_1692.csv",'w')
new2=open("toppapers_averagesimilarity_and_1692.csv",'w')
paperids_or=set()
paperids_and=set()
for k,v in pdetails.items():
	if v[1] >avg1:
		paperids_or.add(k)
		# new.write(k+','+','.join(v)+'\n')
	if(v[2]>avg2):
		paperids_or.add(k)
		# new.write(k+','+','.join(v)+'\n')
	if(v[1]>avg1 and v[2]>avg2):
		new2.write(k+','+v[0] +','+str(v[1]) +','+str(v[2]) +'\n')
new2.close()

for k,v in pdetails.items():
	if( k in paperids_or):
		# new.write(k+','+','.join(v)+'\n')
		new.write(k+','+v[0] +','+str(v[1]) +','+str(v[2]) +'\n')

new.close()