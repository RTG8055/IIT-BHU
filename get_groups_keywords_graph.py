import zipfile
import re


def find_level(a,b,c):
	if(a==0):
		if(b==0):
			return 2
		else:
			return 1
	else:
		return 0


# def get_all_children_words(child,):

file = open("FOS_groups_level_each_conf_sorted.txt",'r')

groups_keywords_required_for_graph={}
i=0
L1_groups=[]
for line in file:
	parent,l1,l2,l3=line.split('\t')
	# print repr(l3)
	i+=1
	parent = parent.replace('\'','').replace(' ','')
	l1=l1.split(';')
	l1_avg=float(l1[2])
	l2=l2.split(';')
	l2_avg=float(l2[2])
	l3=l3.split(';')
	l3_avg=float(l3[2])
	l1=str(l1[3:]).strip('[|]|"').strip("(|)").replace('\'','').replace(' ','').split("),(")
	l2=str(l2[3:]).strip('[|]|"').strip("(|)").replace('\'','').replace(' ','').split("),(")
	l3=str(l3[3:]).strip('[|]|"|\\n').strip("(|)").replace('\'','').replace(' ','').split("),(")

	# if(parent != '0271BC14'):
		# continue
	curr_level = find_level(l1_avg,l2_avg,l3_avg)
	curr_list=[]
	avg=0.5
	####
	#we know which list to check for using the current level
	####
	if(curr_level==0):
		curr_list=l1
		avg = l1_avg
	elif(curr_level==1):
		curr_list=l2
		avg = l2_avg
	else:		#(curr_level==2)
		curr_list=l3
		avg = l3_avg

	# print l1,l2,l3,l1_avg,l2_avg,l3_avg,avg
	###########
	# it has to be in either level0,level1 or level2 as level3 does not have children
	###########
	# curr_list is the list which is to be divided based on avg score
	###########
	lchildren=set()
	rchildren=set()
	for item in curr_list:
		fid,conf = item.split(',')
		conf=float(conf)
		if(conf > avg):
			rchildren.add(fid)
		else:
			lchildren.add(fid)
	groups_keywords_required_for_graph[parent] = [lchildren,rchildren]
	# print lchildren,rchildren,"\n"
	# print repr(l3),l3_avg
	# if(i==10):
		# break
print groups_keywords_required_for_graph["00137C13"]
file.close()

# for k in groups_keywords_required_for_graph.keys():
# 	lchildren=groups_keywords_required_for_graph.get(k)[0]
# 	rchildren=groups_keywords_required_for_graph.get(k)[1]
# 	lchanged=True
# 	rchanged=True
# 	for x in [0,1,2]:
# 		# three iterations for getting all the L1, L2 and L3 levels
# 		tempL=lchildren
# 		tempR=rchildren
# 		if(lchanged==True):
# 			lchanged=False
# 			for child in lchildren:
# 				if(groups_keywords_required_for_graph.get(child)!=None):
# 					newL = groups_keywords_required_for_graph.get(child)[0]
# 					if(newL<tempL):
# 						continue
# 					print child
# 					lchanged=True
# 					tempL = lchildren | newL
# 		if(rchanged==True):
# 			rchanged=False
# 			for child in rchildren:
# 				if(groups_keywords_required_for_graph.get(child)!=None):
# 					newR = groups_keywords_required_for_graph.get(child)[1]

# 					if(newR<tempR):
# 						continue
# 					rchanged=True
# 					tempR.add(child)
# 		if(lchanged==True):
# 			lchildren=tempL
# 		if(rchanged==True):
# 			rchildren=tempR
# 		lchanged=False
# 		rchanged=False
# 	groups_keywords_required_for_graph[k]=[lchildren,rchildren]


print groups_keywords_required_for_graph["00137C13"]




file = open('../fos_keywords_normalized_sorted.txt','r')

fid_groupno={}
keywords=[]
# fids=[]
i=0
for line in file:

	fosID,words=line.split('\t')
	fid_groupno[fosID]=i
	keywords.append([words.strip('\n')])
	i+=1
	# print fosID
	# if(i==100):
		# break
# print fid_groupno,keywords
print i
# give fosid get groupno index at that position get keywords

################################### 
#		 ADDING KEYWORDS TO THE DICTIONARY
###################################


########## FIRST ITERATION TO ADD THE KEYWORDS OT THE GROUPS ##################
i=0
for k in groups_keywords_required_for_graph.keys():
	i+=1
	lwords=set()
	rwords=set()
	parent_words=set()
	lchildren=groups_keywords_required_for_graph.get(k)[0]
	rchildren=groups_keywords_required_for_graph.get(k)[1]
	for child in lchildren:
		if(fid_groupno.get(child)==None):
			continue
		for word in keywords[fid_groupno.get(child)]:
			lwords.add(word)
	for child in rchildren:
		if(fid_groupno.get(child)==None):
			continue
		for word in keywords[fid_groupno.get(child)]:
			rwords.add(word)
	if(fid_groupno.get(k)!=None):
		parent_words = keywords[fid_groupno.get(k)]
	groups_keywords_required_for_graph[k].append(lwords) #[2]
	groups_keywords_required_for_graph[k].append(rwords) #[3]
	groups_keywords_required_for_graph[k].append(parent_words) #[4]

print i,"first iter done"

print groups_keywords_required_for_graph["00137C13"]

i=0
for k in groups_keywords_required_for_graph.keys():
	i+=1
	lchildren=groups_keywords_required_for_graph.get(k)[0]
	rchildren=groups_keywords_required_for_graph.get(k)[1]
	lwords=groups_keywords_required_for_graph.get(k)[2]
	rwords=groups_keywords_required_for_graph.get(k)[3]
		
	for child in lchildren:
		# recur_words = get_all_children_words(child,)
		merged_words=set()
		if(groups_keywords_required_for_graph.get(child)==None):
			if(fid_groupno.get(child)==None):
				continue
			merged_words=keywords[fid_groupno.get(child)]
		else:
			l2children = groups_keywords_required_for_graph.get(child)[0]
			r2children=groups_keywords_required_for_graph.get(child)[1]
			l2words=groups_keywords_required_for_graph.get(child)[2]
			r2words=groups_keywords_required_for_graph.get(child)[3]

			merged_words = l2words | r2words

			for l2child in l2children:
				merged_words2=set()
				if(groups_keywords_required_for_graph.get(l2child)==None):
					if(fid_groupno.get(l2child)==None):
						continue
					merged_words2 =keywords[fid_groupno.get(l2child)]
				else:
					l3children = groups_keywords_required_for_graph.get(l2child)[0]
					r3children=groups_keywords_required_for_graph.get(l2child)[1]
					l3words=groups_keywords_required_for_graph.get(l2child)[2] #rite now they contain only the parent words
					r3words=groups_keywords_required_for_graph.get(l2child)[3]
					#l2words already present adding l3words thats why l3words and r3words
					merged_words2 = l3words | r3words

					for l3child in l3children:
						merged_words3=set()
						# if(groups_keywords_required_for_graph.get(l3child)==None):
						if(fid_groupno.get(l3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(l3child)]

						for w in merged_words3:
							l3words.add(w)
							merged_words2.add(w)
					
					groups_keywords_required_for_graph[l2child][2]=l3words #update the new l3 and r3 words

					for r3child in r3children:
						merged_words3=set()
						if(fid_groupno.get(r3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(r3child)]

						for w in merged_words3:
							r3words.add(w)
							merged_words2.add(w)

					groups_keywords_required_for_graph[l2child][3]=r3words
				
				for w in merged_words2:
					l2words.add(w)
					merged_words.add(w)

			groups_keywords_required_for_graph[child][2] = l2words

			for r2child in r2children:
				merged_words2=set()
				if(groups_keywords_required_for_graph.get(r2child)==None):
					if(fid_groupno.get(r2child)==None):
						continue
					merged_words2 =keywords[fid_groupno.get(r2child)]
				else:
					l3children = groups_keywords_required_for_graph.get(r2child)[0]
					r3children=groups_keywords_required_for_graph.get(r2child)[1]
					l3words=groups_keywords_required_for_graph.get(r2child)[2] #rite now they contain only the parent words
					r3words=groups_keywords_required_for_graph.get(r2child)[3]

					merged_words2 = l3words | r3words

					for l3child in l3children:
						merged_words3=set()
						# if(groups_keywords_required_for_graph.get(l3child)==None):
						if(fid_groupno.get(l3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(l3child)]
						for w in merged_words3:
							l3words.add(w)
							merged_words2.add(w)

					groups_keywords_required_for_graph[r2child][2]=l3words #update the new l3 and r3 words

					for r3child in r3children:
						merged_words3=set()
						if(fid_groupno.get(r3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(r3child)]
						for w in merged_words3:
							r3words.add(w)
							merged_words2.add(w)

					groups_keywords_required_for_graph[r2child][3]=r3words
				
				for w in merged_words2:
					r2words.add(w)
					merged_words.add(w)

			groups_keywords_required_for_graph[child][3] =r2words

		for w in merged_words:
			lwords.add(w)

	groups_keywords_required_for_graph[k][2] = lwords
			
	for child in rchildren:
		# recur_words = get_all_children_words(child,)
		merged_words=set()
		if(groups_keywords_required_for_graph.get(child)==None):
			if(fid_groupno.get(child)==None):
				continue
			merged_words=keywords[fid_groupno.get(child)]
		else:
			l2children = groups_keywords_required_for_graph.get(child)[0]
			r2children=groups_keywords_required_for_graph.get(child)[1]
			l2words=groups_keywords_required_for_graph.get(child)[2]
			r2words=groups_keywords_required_for_graph.get(child)[3]

			merged_words = l2words | r2words

			for l2child in l2children:
				merged_words2=set()
				if(groups_keywords_required_for_graph.get(l2child)==None):
					if(fid_groupno.get(l2child)==None):
						continue
					merged_words2 =keywords[fid_groupno.get(l2child)]
				else:
					l3children = groups_keywords_required_for_graph.get(l2child)[0]
					r3children=groups_keywords_required_for_graph.get(l2child)[1]
					l3words=groups_keywords_required_for_graph.get(l2child)[2] #rite now they contain only the parent words
					r3words=groups_keywords_required_for_graph.get(l2child)[3]
					#l2words already present adding l3words thats why l3words and r3words
					merged_words2 = l3words | r3words

					for l3child in l3children:
						merged_words3=set()
						# if(groups_keywords_required_for_graph.get(l3child)==None):
						if(fid_groupno.get(l3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(l3child)]

						for w in merged_words3:
							l3words.add(w)
							merged_words2.add(w)
					
					groups_keywords_required_for_graph[l2child][2]=l3words #update the new l3 and r3 words

					for r3child in r3children:
						merged_words3=set()
						if(fid_groupno.get(r3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(r3child)]

						for w in merged_words3:
							r3words.add(w)
							merged_words2.add(w)

					groups_keywords_required_for_graph[l2child][3]=r3words
				
				for w in merged_words2:
					l2words.add(w)
					merged_words.add(w)

			groups_keywords_required_for_graph[child][2] = l2words

			for r2child in r2children:
				merged_words2=set()
				if(groups_keywords_required_for_graph.get(r2child)==None):
					if(fid_groupno.get(r2child)==None):
						continue
					merged_words2 =keywords[fid_groupno.get(r2child)]
				else:
					l3children = groups_keywords_required_for_graph.get(r2child)[0]
					r3children=groups_keywords_required_for_graph.get(r2child)[1]
					l3words=groups_keywords_required_for_graph.get(r2child)[2] #rite now they contain only the parent words
					r3words=groups_keywords_required_for_graph.get(r2child)[3]

					merged_words2 = l3words | r3words

					for l3child in l3children:
						merged_words3=set()
						# if(groups_keywords_required_for_graph.get(l3child)==None):
						if(fid_groupno.get(l3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(l3child)]
						for w in merged_words3:
							l3words.add(w)
							merged_words2.add(w)

					groups_keywords_required_for_graph[r2child][2]=l3words #update the new l3 and r3 words

					for r3child in r3children:
						merged_words3=set()
						if(fid_groupno.get(r3child)==None):
							continue
						merged_words3=keywords[fid_groupno.get(r3child)]
						for w in merged_words3:
							r3words.add(w)
							merged_words2.add(w)

					groups_keywords_required_for_graph[r2child][3]=r3words
				
				for w in merged_words2:
					r2words.add(w)
					merged_words.add(w)

			groups_keywords_required_for_graph[child][3] =r2words

		for w in merged_words:
			rwords.add(w)
	groups_keywords_required_for_graph[k][3] = rwords


######
# merged_words contain words of all the l3 children and lr and r2 words
# this has to be merged in the above layer
#####
print i,"all iter done"

print groups_keywords_required_for_graph["00137C13"]

# ###can dissolve the 47000 dictionary###
keywords =[]
fid_groupno.clear()
# ####

# i=0
# new = open("graph_backbone.txt",'w')
# for k,v in groups_keywords_required_for_graph.items():
# 	i+=1
# 	# k is the group parent fos id
# 	# v[0] is the lchildren set 
# 	# v[1] is the rchildren set
# 	# v[2] is the lkeywords set (recursive)
# 	# v[3] is the rkeywirds set (recursive)
# 	# v[4] is the parent keywords list
# 	print k,len(v[0]),len(v[1]),len(v[2]),len(v[3]),len(v[4])
# 	new.write(str(k) + '\t' + ' '.join(list(v[0])) + '\t' + ' '.join(list(v[1])) + '\t' + ','.join(list(v[2])) + '\t' + ','.join(list(v[3])) + '\t' + ','.join(list(v[4])) + '\n')
# print i

while True:
	d=raw_input("enter id:")
	v=groups_keywords_required_for_graph.get(d)
	print len(v[0]),len(v[1]),len(v[2]),len(v[3]),len(v[4]),v[4]
