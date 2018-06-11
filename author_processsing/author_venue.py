import zipfile

with zipfile.ZipFile('no_upload_paper_authors.zip') as z:
	with z.open("paper_authors.txt") as f:
		i=0
		for line in f:
			print line
			i+=1
			if(i==10):
				break