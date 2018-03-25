import re
import zipfile

pdetails={} 
i=0
avg_sim={}
journal_score={}

with open("../Result metric -II/output2/sample35/all_papers_titSim.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# print(repr(line))
		reg = re.match(r'(.*),(.*),(.*),(.*),(.*)',line,re.M|re.I)
		# print(reg)
		pid,ptitle,pjournal,sim1,sim2= reg.group(1),reg.group(2),reg.group(3),reg.group(4),reg.group(5)
		sim2=sim2.strip('\n|\r')
		# print "pid:",pid,",title:",ptitle,",journal:",pjournal,",sim1:",sim1,",sim2:",sim2
		avg =  float(sim1) + float(sim2) / 2
		avg_sim[pid] = avg
		if(journal_score.get(pjournal) == None):
			journal_score[pjournal] = avg
		else:
			journal_score[pjournal]+= avg
		pdetails[pid]=[ptitle,pjournal,float(sim1),float(sim2)]
print i

new=open("output3/sample35/topic_based_venue_count35.txt",'w')
for v in sorted(journal_score,key=journal_score.__getitem__,reverse=True):
	new.write(v + "\t" + str(journal_score[v]) + "\n")
	print v,journal_score[v]
new.close()