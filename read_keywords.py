import zipfile
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize

from search_graph import get_relavent_papers

given_keywords = raw_input("enter comma separated keywords:")
given_fos = raw_input("choose 1\n{\n1:cs,\n2:physics,\n3:chemistry...}:")
if(given_fos == '1'):
	given_fos = "0271BC14"
else:
	print "retry not yet supported"



stop =set(stopwords.words('english'))
lan=LancasterStemmer()
given_keywords = given_keywords.replace('-',' ')
given_keywords = given_keywords.split(',')
i=0

normalized_given_keywords = set()
for word in given_keywords:
	i+=1
	word2=[]
	tokens = word_tokenize(word.lower())
	tokens = [w for w in tokens if not w in stop]
	print i,tokens,word
	for x in tokens:
		word2.append(lan.stem(x))
	normalized_given_keywords.add(' '.join(word2))
normalized_given_keywords = ','.join(list(normalized_given_keywords))
print normalized_given_keywords
papers = get_relavent_papers(normalized_given_keywords,given_fos)

new = open('output/papers2.txt','w')
for p in papers:
	new.write(str(p) + '\n')
new.close()
print "got papers"