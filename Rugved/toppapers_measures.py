i=0
indeg={}
outdeg={}
closeness={}
eigen={}
betweeness={}
avg1=0
avg2=0
avg3=0
avg4=0
avg5=0
with open("sample_2.csv",'r') as file:
	for line in file:
		i+=1
		if(i==1):
			continue
		# if(i==10):
			# break
		line=line.split(',')
		if(indeg.get(line[1])==None):
			indeg[line[1]]=int(line[3])
			avg1+=(int(line[3])+int(line[4]))
			outdeg[line[1]]=int(line[4])
			# avg2+=int(line[4])
			closeness[line[1]]=float(line[10])
			avg3+=float(line[10])
			betweeness[line[1]]=float(line[12])
			avg4+=float(line[12])
			eigen[line[1]]=float(line[13])
			avg5+=float(line[13])
k=0
topset=set()
avg1=float(avg1)/(i-1)
# avg2=float(avg2)/(i-1)
avg3/=(i-1)
avg4/=(i-1)
avg5/=(i-1)
print(avg1)
# print(avg2)
print(avg3)
print(avg4)
print(avg5)
# closeset=set()
# betweenset=set()
# eigenset=set()
# outset=set()
# print(sorted(indeg,key=indeg.__getitem__,reverse=True))
# print(sorted(betweeness,key=betweeness.__getitem__,reverse=True))
# print(sorted(closeness,key=closeness.__getitem__,reverse=True))
# print(sorted(eigen,key=eigen.__getitem__,reverse=True))
# print(sorted(outdeg,key=outdeg.__getitem__,reverse=True))
# print indeg
# sorted(indeg.items(), key=lambda x: x[1][1],reverse=True)
# print indeg

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
for j in (sorted(closeness,key=closeness.__getitem__,reverse=True)):
	if(closeness.get(j)>avg3):
		topset.add(j)
for j in (sorted(eigen,key=eigen.__getitem__,reverse=True)):
	if(eigen.get(j)>avg4):
		topset.add(j)
for j in (sorted(outdeg,key=outdeg.__getitem__,reverse=True)):
	if(outdeg.get(j)>avg5):
		topset.add(j)
	# print(j)
	# print(k)
# inset=set(sorted(outdeg,key=outdeg.__getitem__,reverse=True))
# outset=set(sorted(closeness,key=closeness.__getitem__,reverse=True))
# eigenset=set(sorted(eigen,key=eigen.__getitem__,reverse=True))
# betweenset=set(sorted(betweeness,key=betweeness.__getitem__,reverse=True))
toppaper=open("toppapers.txt",'w')
for j in topset:
	toppaper.write(j)
	toppaper.write('\n')
print(len(topset))
# print(indeg)
# print(y)