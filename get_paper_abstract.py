import urllib2
import requests

import zipfile



relavant_urls = []
with zipfile.ZipFile("zips/upload_cs_papers_urls.zip") as z:
	with z.open("upload_cs_papers_urls.txt",'r') as f:
		i=0
		for line in f:
			i+=1
			# print line
			pid,urls = line.split('\t')
			urls = urls.strip('\n|\r')
			# print repr(pid),repr(urls)
			urls = urls.split(' ')
			print repr(urls)
			for url in urls:
				
			if(i==10):
				break
print urls