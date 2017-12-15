import zipfile

fos_keywords={}

with zipfile.ZipFile("zips/fos_papers_keywords_server.zip") as z2:
	with z2.open("fos_papers_keywords_server.txt") as f2:
		i=0
		for  line in f2:
			i+=1
			# print repr(line)
			fosid,papers,keywords = line.split('\t')
			keywords = keywords.strip('\n')
			# print repr(fosid),repr(papers),repr(keywords)
			fos_keywords[fosid] = (keywords,len(papers.split(' ')))
			# if(i==100):
				# break
while True:
	x = raw_input("enter fos:")
	print fos_keywords.get(x)
