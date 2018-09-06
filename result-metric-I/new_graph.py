import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# file_name = 'new_data'

file_name= 'Updated_Resultsnew'

all_sheets = pd.ExcelFile(file_name + '.xlsx')

plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams.update({'figure.autolayout' : True})

for sheet in all_sheets.sheet_names:
	if('Sheet' in  sheet):
		continue
	print sheet
	ylabel='default'
	tick_skip=3
	if('precision' in sheet or 'Precision' in sheet):
		ylabel = 'Precision@N'
	elif('nDCG' in sheet):
		ylabel = 'nDCG@N'
	else:
		tick_skip=2
		ylabel = 'H5-Index'

	df = all_sheets.parse(sheet)
	print df.head()

	fig = plt.figure(figsize=(6,4))
	plt.style.use('seaborn-bright')

	colors=['red','black','green','orange','aqua','magenta','brown','blue']
	markers=['^','p','8','P','*','D','o','s']
	print df.count()
	nrows = df.count()[0]
	cols = df.columns
	xlabel='Top N Recommendation'
	



	for i in range(0,len(cols)):
		plt.plot(np.arange(1,nrows+1,1),df[cols[i]],alpha=0.6,markersize=6,color=colors[i],marker=markers[i])
		
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.xticks(np.arange(0,nrows+1,tick_skip))
	plt.legend(bbox_to_anchor=(0.48,-0.67), loc="lower left", bbox_transform=fig.transFigure,ncol=len(cols), mode="expand",labelspacing = 0.,borderaxespad=17.3,frameon=False)
	# plt.show()
	plt.savefig(file_name + "_"+sheet + ".eps",dpi=300, bbox_inches = "tight")


