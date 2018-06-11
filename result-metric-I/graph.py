import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "Final2"
# file_name = "Precision2"

all_sheets = pd.ExcelFile(file_name+".xlsx")

# plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams.update({'figure.autolayout': True})

all_fig = plt.figure(figsize=(11.93,15.98))

# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# plt.text()

# ax.legend()
subplot_no=0
print all_sheets.sheet_names
for sheet in all_sheets.sheet_names:
	print sheet
	if(sheet == 'P@i'):
		continue
	df = all_sheets.parse(sheet)
	print df.head()
	plt.style.use('seaborn-bright')
	# ax = fig.add_axes([0.1,0.1,0.8,0.8])
	print subplot_no
	subplot_no+=1
	# if(subplot_no<7):
		# continue
	if(subplot_no==7):
		break
	ax = plt.subplot(4,3,subplot_no)

	# plt.text()
	l1=ax.plot(np.arange(1,16,1),df.Snaver2,alpha=0.7,color='aqua',marker='s',markersize=6,label='DISCOVER(Springer)')
	l1=ax.plot(np.arange(1,16,1),df.Snaver1,alpha=0.7,color='blue',marker='s',markersize=6,label='DISCOVER(Elsevier)')
	l2=ax.plot(np.arange(1,16,1),df.Springer,ls=(0,(5,5,)),alpha=0.7,color='green',marker='8',markersize=6)
	l3=ax.plot(np.arange(1,16,1),df.Elsevier,ls=(0, (3,1,5,1,5,5)),alpha=0.7,color='red',marker='+',markersize=6)

	ax.legend()
	ax.set_xticks(np.arange(0,16,3))
	# plt.axis([0.99,20.01,0.59,1.01])
	ax.set_xlabel("Top K papers")
	ax.set_ylabel("nDCG@K")
	# ax.set_ylabel("Precision@K")
	name =""
	if(sheet == "IR"):
		name = "Information Retrieval"
	elif(sheet == "WSN"):
		name = "Wireless Networks"
	elif(sheet == "PDS"):
		name = "Parallel and distributed systems"
		# sheet = "PDS"
	elif(sheet == "AI"):
		name = "Artificial Intellignece"
		# sheet ="AI"
	elif(sheet == "CV"):
		name = "Computer Vision"
	elif(sheet == "mm"):
		name = "Multimedia"
	elif(sheet == "Security"):
		name = "Security"
	elif(sheet == "DM"):
		name = "Data Mining"
	elif(sheet == "NLP"):
		name = "Natural Language Processing"
	elif(sheet == "ML"):
		name = "Machine Learning"
	elif(sheet == "IP"):
		name = "Image Processing"
	else:
		name = "Software Engineering"
	ax.set_title(name,fontweight = "bold")
	# sns.despine()
	# plt.tight_layout()


plt.savefig(file_name + "2.eps",dpi=300, bbox_inches = "tight")
plt.savefig(file_name + "2.png",dpi=300, bbox_inches = "tight")