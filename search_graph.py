import zipfile


groups = {} # pfid: lchildren,rchildren,lwords,rwords,pwords 
with open("graph_backbone.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		parent,lchildren,rchildren,lwords,rwords,pwords = line.split('\t')
		pwords = pwords.strip("\n")
		groups[parent]=[lchildren,rchildren,lwords,rwords,pwords]
print i


def word_list_score(word,list_words):
	###########################
	#	given word to be comapred to the list_words
	#	list_words is a string with comma separated keywords to be searched in
	#		returns a score based on the word and the list similarity
	###########################

	score=0
	list_words = list_words.split(',')
	# print list_words
	for w in list_words:
		if(w == word):
			# print w
			score+=1
	return score

def search_in_all_fos(list_fosids,given_words,level): #return lchildren or rchildren  

	# print list_fosids,given_words
	##########################
	# list_fosids = list of parent elements whose children to be searched
	##########################
	# return the required fos_ids
	##########################
	if(level==2):
		#############
		# groups dictionary doesn't contain any keywords for L3 level ids
		# fetch from the file and check if relavant
		#############
		final_list=[]
		with open("fos_keywords_normalized_sorted.txt") as f:
			for line in f:
				fid,keywords = line.split("\t")
				if fid not in list_fosids:
					continue
				keywords = keywords.strip("\n")
				score=0
				for g in given_words:
					score = score + word_list_score(g,keywords)
				if(score>0):
					# even if score is greater than 0 we consider that fid as we are dong an exact match
					final_list.append(fid)

		return final_list

	maxScore=0
	maxlscore_list=0
	maxrscore_list=0
	maxpscore_list=0
	maxlchildren_list=0
	maxrchildren_list=0
	maxpid_list=0
	####################
	# to choose one of the fids to proceed to choose the one which has the maximum total of rscore, lscore and pscore
	####################
	for fid in list_fosids:
		# print fid,level
		if(groups.get(fid)==None):
			print fid,"not there directly ",level
			with open("fos_keywords_normalized_sorted.txt") as f:
				for line in f:
					fid2,keywords = line.split("\t")
					if(fid2 != fid):
						continue
					keywords = keywords.strip("\n")
					score=0
					for g in given_words:
						score = score + word_list_score(g,keywords)
					print "score:",score
					if(score> maxScore):
						maxScore = score
						maxpid=fid
						maxpscore = score
					break
			continue
		v=groups.get(fid)
		##############################
		# lchildren --> v[0]
		# rchildren --> v[1]
		# lwords --> v[2]
		# rwords --> v[3]
		# pwords --> v[4]
		###########################
		lscore=0
		rscore=0
		pscore=0
		for g in given_words:
			lscore = lscore + word_list_score(g,v[2])
			rscore = rscore + word_list_score(g,v[3])
			pscore = pscore + word_list_score(g,v[4])

		# print lscore,rscore,pscore,maxScore
		if(lscore+rscore+pscore>maxScore):
			maxlscore_list=[lscore]
			maxrscore_list=[rscore]
			maxpscore_list=[pscore]
			maxlchildren_list=[v[0]]
			maxrchildren_list=[v[1]]
			maxpid_list=[fid]
			maxScore = lscore+rscore+pscore
		elif(lscore+rscore+pscore > 0 and lscore+rscore+pscore == maxScore):
			maxlscore_list.append(lscore)
			maxrscore_list.append(rscore)
			maxpscore_list.append(pscore)
			maxlchildren_list.append(v[0])
			maxrchildren_list.append(v[1])
			maxpid_list.append(fid)

		# print maxpid_list
	fos_list_required=[]
	for x in range(0,len(maxpid_list)):
		maxlscore = maxlscore_list[x]
		maxrscore = maxrscore_list[x]
		maxpscore = maxpscore_list[x]
		maxlchildren = maxlchildren_list[x]
		maxrchildren = maxrchildren_list[x]
		maxpid = maxpid_list[x]



		if(maxpscore> maxlscore and maxpscore > maxrscore):
			# it is a general category paper
			maxpid = maxpid.split(' ')
			# print maxpscore,maxlscore,maxrscore,level
			fos_list_required.append(maxpid)
			continue
			# return maxpid
		if(maxlscore>maxrscore):
			maxlchildren = maxlchildren.split(' ')
			print "left",level,maxpid#,maxScore,maxpscore,maxlscore
			if(maxpscore == maxlscore):
				fos_list_required.append(' '.join(search_in_all_fos(maxlchildren,given_words,level+1) + maxpid.split(' ')))
				continue

			fos_list_required.append(' '.join(search_in_all_fos(maxlchildren,given_words,level+1)))
			continue
		elif(maxrscore>0):
			maxrchildren = maxrchildren.split(' ')
			maxlchildren = maxlchildren.split(' ')
			print "right",level,maxpid
			if(maxpscore == maxrscore and maxrscore == maxlscore):
				fos_list_required.append(' '.join(search_in_all_fos(maxrchildren,given_words,level+1) + maxpid.split(' ') + search_in_all_fos(maxlchildren,given_words,level+1)))
			elif(maxrscore == maxlscore):
				# print maxrchildren,"hahahaha",maxlchildren
				fos_list_required.append(' '.join(search_in_all_fos(maxrchildren,given_words,level+1) + search_in_all_fos(maxlchildren,given_words,level+1)))

			elif(maxpscore == maxrscore):
				fos_list_required.append(' '.join(search_in_all_fos(maxrchildren,given_words,level+1) + maxpid.split(' ')))
			else:
				fos_list_required.append(' '.join(search_in_all_fos(maxrchildren,given_words,level+1)))
		else:
			print maxlscore,maxrscore,maxpscore,level
			print "all scores are Zero"
			# return []
		# print fos_list_required
	# print fos_list_required
	return fos_list_required



def get_relavent_papers(given_keywords,given_fos):
	##################
	#given_keywords string comma separated normalized keywords
	#given_fos is the code of any one L0 group
	#################
	# return the relavant paper ids
	#################

	# with zipfile.ZipFile("zips/fos_papers_keywords_server.zip") as z2:
		# with z2.open("fos_papers_keywords_server.txt") as f2:

	general_category=False
	# with open("graph_backbone.txt",'r') as f:
	i=0
	precise_ids=[]
	for k in groups.keys():
		i+=1
		v=groups.get(k)
		# print v
		##############################
		# lchildren --> v[0]
		# rchildren --> v[1]
		# lwords --> v[2]
		# rwords --> v[3]
		# pwords --> v[4]
		###########################
		# print k,given_fos
		to_be_searched_words=""
		list_L1=""
		if(k == given_fos):
			given_keywords = given_keywords.split(',')
			print "insode"
			to_be_searched_words = ','.join([v[2],v[3],v[4]])
			# print to_be_searched_words
			lscore=0
			rscore=0
			pscore=0
			for g in given_keywords:
				lscore = lscore + word_list_score(g,v[2])
				rscore = rscore + word_list_score(g,v[3])
				pscore = pscore + word_list_score(g,v[4])
			print lscore,rscore,pscore
			if(lscore<pscore and rscore<pscore):
				precise_ids = list(k)
				break
			if(lscore >= rscore):
				if(lscore == rscore):
					list_L1+=v[1]
				print "left -1"
				if(lscore == pscore):
					general_category=True
				list_L1+= " " + v[0]

			else:
				print "right -1"
				if(rscore == pscore):
					general_category=True
				list_L1+= " " + v[1]
			
			################
			# if only in general category it would not reach here
			################
			list_L1 = list_L1.split(' ')
			# print list_L1,given_keywords
			print list_L1
			precise_ids = search_in_all_fos(list_L1,given_keywords,0)
			# print precise_ids
			if(general_category):
				precise_ids += k.split(' ')
			break
		# if(i==1):
			# break

	#############
	# outside for loop
	#############
	new_precise_ids=[]
	for p in precise_ids:
		new_precise_ids +=p.split(' ')
	precise_ids = new_precise_ids
	print precise_ids

	with zipfile.ZipFile("zips/fos_papers_keywords_server.zip") as z:
		with z.open("fos_papers_keywords_server.txt") as f:
			i=0
			relavent_papers=set()
			count = len(precise_ids)
			for line in f:
				i+=1
				fid,papers,keywords = line.split('\t')
				if fid in precise_ids:
					count-=1
					papers = papers.split(' ')
					for p in papers:
						relavent_papers.add(p)
				if(count ==0):
					break
				# if(i==1):
					# break
			print len(relavent_papers)
			return relavent_papers



