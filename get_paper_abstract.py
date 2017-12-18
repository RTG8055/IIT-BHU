import urllib2
import requests

import zipfile


urls = []
with zipfile.ZipFile("zips/PaperUrls.zip") as z:
	with z.open("PaperUrls.txt",'r') as f:
		i=0
		for line in f:
			i+=1
			print line
			pid,url = line.split('\t')
			url = url.strip("\n|\r")
			urls.append(url)
			if(i==10):
				break
print urls