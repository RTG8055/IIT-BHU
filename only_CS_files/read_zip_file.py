import zipfile

precise_ids =['000A1802']





with zipfile.ZipFile("../zips/fos_papers_keywords_server.zip") as z:
		with z.open("fos_papers_keywords_server.txt") as f:
			i=0
			relavent_papers=set()
			count = len(precise_ids)
			for line in f:
				i+=1
				fid,papers,keywords = line.split('\t')
				# if fid in precise_ids:
				# 	count-=1
				# 	papers = papers.split(' ')
				# 	for p in papers:
				# 		relavent_papers.add(p)
				# if(count ==0):
				# 	break
				# if(i==1):
					# break
			print i
			print len(relavent_papers)
			# return relavent_papers

