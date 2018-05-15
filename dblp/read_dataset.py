import zipfile,os,json

path = 'datasets/dblp/dblp_v10.zip/dblp-ref/'
with zipfile.ZipFile("../datasets/dblp/dblp_v10.zip") as z:
	with z.open("dblp-ref/dblp-ref-0.json") as f:
		i=0
		data = json.load(f)
		