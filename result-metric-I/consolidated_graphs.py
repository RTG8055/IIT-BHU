import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# file_name = "Final"
file_name = "Precision"

all_sheets = pd.ExcelFile(file_name+".xlsx")

# plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams.update({'figure.autolayout': True})

all_fig = plt.figure(figsize=(11.93,15.98))

# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# plt.text()

# ax.legend()
snaver,elsevier,springer=[0]*10,[0]*10,[0]*10
subplot_no=0
total = float(len(all_sheets.sheet_names))
print all_sheets.sheet_names,total
print snaver
for sheet in all_sheets.sheet_names:
	df = all_sheets.parse(sheet)
	# print df.head()
	i=0
	for d in df.Snaver:
		snaver[i]=snaver[i]+d
		i+=1
		if(i==10):
			break
	i=0
	for d in df.Springer:
		springer[i]=springer[i]+d
		i+=1
		if(i==10):
			break
	i=0
	for d in df.Elsevier:
		elsevier[i]=elsevier[i]+d
		i+=1
		if(i==10):
			break
print snaver
print springer
print elsevier
snaver = [x/total for x in snaver]
springer = [x/total for x in springer]
elsevier = [x/total for x in elsevier]
print snaver
print springer
print elsevier

snaver = pd.Series(snaver)
springer = pd.Series(springer)
elsevier = pd.Series(elsevier)
print snaver
plt.style.use('seaborn-bright')
# ax = plt.gca()
ax = plt.subplot(2,1,1)

# ax.legend(loc=1)
l1=ax.plot(np.arange(1,11,1),snaver,alpha=0.7,color='blue',marker='s',markersize=6,label='Snaver')
l2=ax.plot(np.arange(1,11,1),springer,ls=(0,(5,5,)),alpha=0.7,color='green',marker='8',markersize=6,label='Springer')
ax.set_xticks(np.arange(0,11,1))
# plt.axis([0.99,20.01,0.59,1.01])
ax.legend()
ax.set_xlabel("Top K papers")
# ax.set_ylabel("nDCG@K")
ax.set_ylabel("Precision@K")
ax.set_title("Precision ",fontweight = "bold")

ax=plt.subplot(2,1,2)
l1=ax.plot(np.arange(1,11,1),snaver,alpha=0.7,color='blue',marker='s',markersize=6,label='Snaver')
l2=ax.plot(np.arange(1,11,1),elsevier,ls=(0,(5,5,)),alpha=0.7,color='green',marker='8',markersize=6,label='elsevier')
ax.set_xticks(np.arange(0,11,1))
ax.legend()
ax.set_xlabel("Top K papers")
ax.set_ylabel("Precision@K")


plt.draw()
# plt.show()
plt.savefig("precision.eps",dpi=300, bbox_inches = "tight")
plt.savefig("precision.png",dpi=300, bbox_inches = "tight")


# for sheet in all_sheets.sheet_names:
# 	print sheet
# 	if(sheet == 'P@i'):
# 		continue
# 	df = all_sheets.parse(sheet)
# 	print df.head()
# 	plt.style.use('seaborn-bright')
# 	# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# 	print subplot_no
# 	subplot_no+=1
# 	if(subplot_no<7):
# 		continue
# 	# if(subplot_no==7):
# 		# break
# 	ax = plt.subplot(4,3,subplot_no)

# 	# plt.text()
# 	l1=ax.plot(np.arange(1,21,1),df.Snaver,alpha=0.7,color='blue',marker='s',markersize=6)
# 	l2=ax.plot(np.arange(1,21,1),df.Springer,ls=(0,(5,5,)),alpha=0.7,color='green',marker='8',markersize=6)
# 	l3=ax.plot(np.arange(1,21,1),df.Elsevier,ls=(0, (3,1,5,1,5,5)),alpha=0.7,color='red',marker='+',markersize=6)

# 	ax.legend()
# 	ax.set_xticks(np.arange(0,21,2))
# 	# plt.axis([0.99,20.01,0.59,1.01])
# 	ax.set_xlabel("Top K papers")
# 	# ax.set_ylabel("nDCG@K")
# 	ax.set_ylabel("Avg Precision@K")
# 	name =""
# 	if(sheet == "IR"):
# 		name = "Information Retrieval"
# 	elif(sheet == "WSN"):
# 		name = "Wireless Networks"
# 	elif(sheet == "PDS"):
# 		name = "Parallel and distributed systems"
# 		# sheet = "PDS"
# 	elif(sheet == "AI"):
# 		name = "Artificial Intellignece"
# 		# sheet ="AI"
# 	elif(sheet == "CV"):
# 		name = "Computer Vision"
# 	elif(sheet == "mm"):
# 		name = "Multimedia"
# 	elif(sheet == "Security"):
# 		name = "Security"
# 	elif(sheet == "DM"):
# 		name = "Data Mining"
# 	elif(sheet == "NLP"):
# 		name = "Natural Language Processing"
# 	elif(sheet == "ML"):
# 		name = "Machine Learning"
# 	elif(sheet == "IP"):
# 		name = "Image Processing"
# 	else:
# 		name = "Software Engineering"
# 	ax.set_title(name,fontweight = "bold")
# 	# sns.despine()
# 	# plt.tight_layout()


# plt.savefig(file_name + "7.eps",dpi=300, bbox_inches = "tight")
# plt.savefig(file_name + "7.png",dpi=300, bbox_inches = "tight")