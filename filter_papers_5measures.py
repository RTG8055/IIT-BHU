i=0
indeg={}
outdeg={}
closeness={}
eigen={}
betweeness={}
auth_hub={}
avg1=0
avg2=0
avg3=0
avg4=0
avg5=0
with open("output/sample8/gephi_deg_clo_bw_auth_hub_eigen.csv",'r') as file:
# Id	Label	indegree	outdegree	Degree
				# closnesscentrality	betweenesscentrality	Authority	Hub	
				# eigencentrality

	for line in file:
		i+=1
		if(i==1):
			continue
		# if(i==10):
			# break
		line=line.split(',')
		# print repr(line),float(line[9])
		if(indeg.get(line[1])==None):
			indeg[line[1]]=int(line[2])
			
			avg1+=(int(line[2])+int(line[3]))
			
			outdeg[line[1]]=int(line[3])
			
			closeness[line[1]]=float(line[5])
			avg3+=float(line[5])
			
			betweeness[line[1]]=float(line[6])
			avg4+=float(line[6])

			auth_hub[line[1]] = float(line[7]) + float(line[8])
			avg2 += auth_hub[line[1]]

			eigen[line[1]]=float(line[9])
			avg5+=float(line[9])
print i,len(eigen)
k=0
topset=set()
avg1=float(avg1)/(i-1)
avg2/=(i-1)
avg3/=(i-1)
avg4/=(i-1)
avg5/=(i-1)
print(avg1)
print(avg2)
print(avg3)
print(avg4)
print(avg5)

for j in (sorted(indeg,key=indeg.__getitem__,reverse=True)):
	# k+=1
	# print j
	if(indeg.get(j)>avg1):
		# k+=1
		topset.add(j)
# print(k)
for j in (sorted(betweeness,key=betweeness.__getitem__,reverse=True)):
	if(betweeness.get(j)>avg1):
		topset.add(j)
for j in (sorted(auth_hub,key=auth_hub.__getitem__,reverse=True)):
	if(auth_hub.get(j)>avg2):
		topset.add(j)
for j in (sorted(closeness,key=closeness.__getitem__,reverse=True)):
	if(closeness.get(j)>avg3):
		topset.add(j)
for j in (sorted(eigen,key=eigen.__getitem__,reverse=True)):
	if(eigen.get(j)>avg4):
		topset.add(j)
for j in (sorted(outdeg,key=outdeg.__getitem__,reverse=True)):
	if(outdeg.get(j)>avg5):
		topset.add(j)


toppaper=open("output/sample8/filtered_papers_5measures.txt",'w')
for j in topset:
	toppaper.write(j)
	toppaper.write('\n')
print(len(topset))
