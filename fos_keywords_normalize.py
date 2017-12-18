import zipfile
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

stop =set(stopwords.words('english'))
fos_keywords={}
lan=LancasterStemmer()
# wordnet = WordNetLemmatizer()
with zipfile.ZipFile("zips/fos_papers_keywords_server.zip") as z2:
	with z2.open("fos_papers_keywords_server.txt") as f2:
		i=0
		for  line in f2:
			i+=1
			# print repr(line)
			fosid,papers,keywords = line.split('\t')
			keywords = keywords.strip('\n')
			c=set()
			for k in keywords.split(','):
				k2=[]
				tokens = word_tokenize(k.lower())
				tokens = [w for w in tokens if not w in stop]
				print i,tokens,k
				for x in tokens:
					k2.append(lan.stem(x))
					# k2.append(wordnet.lemmatize(x))
				print ' '.join(k2),"<--", k
				c.add(' '.join(k2))
			keywords = list(c)

			# print repr(fosid),repr(papers),repr(keywords)
			fos_keywords[fosid] = keywords
			if(i==100):
				break
print i
new = open('fos_keywords_normalized2.txt','w')
i=0
for k,v in fos_keywords.items():
	i+=1
	# print k,v
	new.write(str(k) + "\t" + ','.join(v)+ "\n")
print i
# while True:
	# x = raw_input("enter fos:")
	# print fos_keywords.get(x)