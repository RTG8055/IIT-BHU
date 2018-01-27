

venue_count={}

with open("output3/sample6/papers6_titles_journals.txt",'r') as file:
	for line in file:
		pid,pdetails = line.strip("\n|\r").split("\t")
		venue = pdetails.split("<---")[0]
		if(venue_count.get(venue) == None):
			venue_count[venue] =1
		else:
			venue_count[venue]+=1

print len(venue_count)
new = open("output3/sample6/venue_count6.txt",'w')
for v in sorted(venue_count,key=venue_count.__getitem__,reverse=True):
	new.write(v + "\t" + str(venue_count[v]) + "\n")
	print v,venue_count[v]
new.close()
# for k,v in venue_count.items():
	# print k,v