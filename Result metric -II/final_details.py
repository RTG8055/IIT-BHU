paperids={}
papers=set()
with open("output2/sample6/final_papers6_2.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		line = line.strip('\n|\r')
		# print repr(line)
		paperids[line] = i
		papers.add(line)

print i,len(paperids)

all_titles = {}
all_journals={}

f = open("output2/sample6/papers6_titles_journals.txt",'r')
for line in f:
	paperID,pJournaltitle = line.split('\t')
	pjournal,ptitle = pJournaltitle.split("<--")
	ptitle = ptitle.strip('\n')
	all_titles[paperID] = ptitle
	all_journals[paperID] = pjournal
f.close()


# print all_titles
new = open("output2/sample6/final_details6_2.txt",'w')
i=0
for p in paperids:
	i+=1
	new.write(p + "\t" + all_titles[p] + "\t" + all_journals[p] + "\n")

print i