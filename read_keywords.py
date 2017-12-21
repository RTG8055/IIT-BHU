import zipfile
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize

from search_graph import get_relavent_papers

given_keywords = raw_input("enter comma separated keywords:")
'''

sample2:
Cyclic redundancy check,parity calculations, discrete cosine transform , fault-tolerant source coding, Huffman coding, JPEG data compression, quantization protection, soft errors

sample3:
Click through, Data, Iterative Algorithm,  Log  Mining,  Search  Engine

sample4:
mixture variable memory, Markov model, Query recommendation, sequential query prediction

sample5:
Category Hierarchy, Information Filtering, Personalization, Retrieval Effectiveness, Search Engine

sample6:
hierarchical clustering, criterion function, constrained agglomerative clustering, data mining

sample7:
Automatic fingerprint recognition, combination model, global approximation, orientation field, singular point

sample8:
Time synchronization, wireless sensor networks, clock synchronization

Fingerprint recognition, Image matching, Approximation algorithms, Robustness, Polynomials, Biometrics, Databases, Large-scale systems, Bifurcation, Automation 

'''


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

new = open('output/sample8/papers8.txt','w')
for p in papers:
	new.write(str(p) + '\n')
new.close()
print "got papers"