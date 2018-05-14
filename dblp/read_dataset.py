import zipfile,os,json

path = 'datasets/dblp/dblp_v10.zip/dblp-ref/'
with zipfile.ZipFile("../datasets/dblp/dblp_v10.zip") as z:
	z.extract('dblp-ref/')
	z.r
		
