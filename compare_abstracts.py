from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer
import gensim

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
# doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
# doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
# doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
# doc_e = "Health professionals say that brocolli is good for your health."

doc_set=[]
docid_paperid={}
file = open('Rugved/Paperid_Abstracts.txt','r')
i=0
for line in file:
	i+=1
	line = line.strip('\n|\r').split('\t')
	doc_set.append(line[1])
	docid_paperid[i]=line[0]
# print doc_set

given_abs = raw_input("enter abstract:")
doc_set.append(given_abs)


# doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]	


stop =set(stopwords.words('english'))
texts=[]
tokenizer = RegexpTokenizer(r'\w+')


p_stemmer = PorterStemmer()
# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in stop]
    
    # print stopped_tokens
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id < > term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=len(doc_set)/10, id2word = dictionary, passes=20)

for top in ldamodel.print_topics():
	print top



lda_corpus = ldamodel[corpus]
i=0
final_topic =0

focus_doc = lda_corpus[len(doc_set)-1]
tmax=0;topic_id=0
for d in focus_doc:
	if(d[1]>tmax):
		tmax=d[1]
		topic_id=d[0]
print topic_id

final_list={}
for doc in lda_corpus:
	i+=1
	if(i==len(doc_set)):
		continue
	# print doc
	for d in doc:
		if(d[0] == topic_id):
			final_list[i] = d[1]
	print doc,i

final_list = sorted(final_list,key=final_list.__getitem__,reverse=True)
for d in final_list:
	print d,docid_paperid.get(d)
print final_list


'''
In the era of big scholarly data, citation recommendation is playing an increasingly significant role as it solves information overload issues by automatically suggesting relevant references that align with researchers interests. Many state-of-the-art models have been utilized for citation recommendation, among which graph-based models have garnered significant attention, due to their flexibility in integrating rich information that influences users preferences. Co-authorship is one of the key relations in citation recommendation, but it is usually regarded as a binary relation in current graph-based models. This binary modeling of co-authorship is likely to result in information loss, such as the loss of strong or weak relationships between specific research topics. To address this issue, we present a fine-grained method for co-authorship modeling that incorporates the co author network structure and the topics of their published articles. Then, we design a three layered graph based recommendation model that integrates fine grained co authorship as well as author paper, paper citation, and paper keyword relations. Our model effectively generates query oriented recommendations using a simple random walk algorithm. Extensive experiments conducted on a subset of the anthology network data set for performance evaluation demonstrate that our method outperforms other models in terms of both Recall and NDCG.
'''


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

no_features = 250

# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(doc_set)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(doc_set)
tf_feature_names = tf_vectorizer.get_feature_names()


from sklearn.decomposition import NMF, LatentDirichletAllocation

no_topics = len(doc_set)/10

# Run NMF
final_mat=[]
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit_transform(tfidf)

focus_doc = nmf[len(doc_set)-1]
tmax=0;topic_id=0
for t_d,d in enumerate(focus_doc):
	if(d>tmax):
		tmax=d
		topic_id=t_d
print topic_id

final_list={}
i=0
for d_id,doc in enumerate(nmf):
	i+=1
	# if(i==len(doc_set)):
		# continue
	# print doc
	for t_d,d in enumerate(doc):
		if(t_d == topic_id):
			final_list[i] = d
	print doc,i

final_list = sorted(final_list,key=final_list.__getitem__,reverse=True)
for d in final_list:
	print d,docid_paperid.get(d)
print final_list




# for k,d in enumerate(nmf):
# 	print d,k+1

# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit_transform(tf)


focus_doc = lda[len(doc_set)-1]
tmax=0;topic_id=0
for t_d,d in enumerate(focus_doc):
	if(d>tmax):
		tmax=d
		topic_id=t_d
print topic_id

final_list={}
i=0
for d_id,doc in enumerate(lda):
	i+=1
	# if(i==len(doc_set)):
		# continue
	# print doc
	for t_d,d in enumerate(doc):
		if(t_d == topic_id):
			final_list[i] = d
	print doc,i

final_list = sorted(final_list,key=final_list.__getitem__,reverse=True)
for d in final_list:
	print d,docid_paperid.get(d)
print final_list


# for k,d in enumerate(lda):
# 	print d,k+1

