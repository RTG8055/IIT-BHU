import zipfile

with zipfile.ZipFile("author_papers.zip") as z:
	with z.open("author_papers.txt") as f:
		i=0
		for line in f:
			i+=1
			aid,no_papers,papers = line.strip('\r|\n').split('\t')
			# print aid,no_papers,papers
			papers = papers.strip("[|]|\n|\r")
			# print papers
			papers = papers.split(' ')
			# print papers
			papreids = [p.split('-')[0] for p in papers]
			print papreids
			break
