import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

all_sheets = pd.ExcelFile("PDS and AI.xlsx")
print all_sheets.sheet_names
for sheet in all_sheets.sheet_names:
	print sheet
	if(sheet == 'P@i'):
		continue
	df = all_sheets.parse(sheet)
	print df.head()
	plt.style.use('seaborn-bright')
	fig = plt.figure(figsize=(10,10))
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	l1=ax.plot(np.arange(1,21,1),df.Snaver,alpha=0.7,color='blue',marker='s')
	l2=ax.plot(np.arange(1,21,1),df.Springer,ls=(0,(5,5,)),alpha=0.7,color='green',marker='8')
	l3=ax.plot(np.arange(1,21,1),df.Elsevier,ls=(0, (3,1,5,1,5,5)),alpha=0.7,color='red',marker='+')
	ax.legend()
	ax.set_xticks(np.arange(1,21,1))
	# plt.axis([0.99,20.01,0.59,1.01])
	ax.set_xlabel("Top K papers")
	ax.set_ylabel("nDCG@K")
	name =""
	if(sheet == "IR"):
		name = "Information Retrieval"
	elif(sheet == "WSN"):
		name = "Wireless Networks"
	elif(sheet == "PDS_Graph"):
		name = "Parallel and distributed systems"
		sheet = "PDS"
	elif(sheet == "AI_Graph"):
		name = "Artificial Intellignece"
		sheet ="AI"
	else:
		name = "Software Engineering"
	
	ax.set_title(name)
	# sns.despine()
	plt.savefig(sheet + "8.png",dpi=300)