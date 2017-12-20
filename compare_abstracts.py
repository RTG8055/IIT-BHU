from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer
import gensim

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

doc_set=[]
docid_paperid={}
file = open('output/sample3/paperid_abstract3.txt','r')
i=0
for line in file:
	i+=1
	line = line.strip('\n|\r').split('\t')
	doc_set.append(line[1])
	docid_paperid[i]=line[0]
# print doc_set

given_abs = raw_input("enter abstract:")
doc_set.append(given_abs)


'''
In the era of big scholarly data, citation recommendation is playing an increasingly significant role as it solves information overload issues by automatically suggesting relevant references that align with researchers interests. Many state-of-the-art models have been utilized for citation recommendation, among which graph-based models have garnered significant attention, due to their flexibility in integrating rich information that influences users preferences. Co-authorship is one of the key relations in citation recommendation, but it is usually regarded as a binary relation in current graph-based models. This binary modeling of co-authorship is likely to result in information loss, such as the loss of strong or weak relationships between specific research topics. To address this issue, we present a fine-grained method for co-authorship modeling that incorporates the co author network structure and the topics of their published articles. Then, we design a three layered graph based recommendation model that integrates fine grained co authorship as well as author paper, paper citation, and paper keyword relations. Our model effectively generates query oriented recommendations using a simple random walk algorithm. Extensive experiments conducted on a subset of the anthology network data set for performance evaluation demonstrate that our method outperforms other models in terms of both Recall and NDCG.

The JPEG image compression standard is very sensitive to errors. Even though it contains error resilience features, it cannot easily cope with induced errors from computer soft faults prevalent in remote-sensing applications. Hence, new fault tolerance detection methods are developed to sense the soft errors in major parts of the system while also protecting data across the boundaries where data flow from one subsystem to the other. The design goal is to guarantee no compressed or decompressed data contain computer-induced errors without detection. Detection methods are expressed at the algorithm level so that a wide range of hardware and software implementation techniques can be covered by the fault tolerance procedures while still maintaining the JPEG output format. The major subsystems to be addressed are the discrete cosine transform, quantizer, entropy coding, and packet assembly. Each error detection method is determined by the data representations within the subsystem or across the boundaries. They vary from real number parities in the DCT to bit-level residue codes in the quantizer, cyclic redundancy check parities for entropy coding, and packet assembly. The simulation results verify detection performances even across boundaries while also examining roundoff noise effects in detecting computer-induced errors in processing steps.

The performance of web search engines may often deteriorate due to the diversity and noisy information contained within web pages. User click-through data can be used to introduce more accurate description (metadata) for web pages, and to improve the search performance. However, noise and incompleteness, sparseness, and the volatility of web pages and queries are three major challenges for research work on user click-through log mining. In this paper, we propose a novel iterative reinforced algorithm to utilize the user click-through data to improve search performance. The algorithm fully explores the interrelations between queries and web pages, and effectively finds "virtual queries" for web pages and overcomes the challenges discussed above. Experiment results on a large set of MSN click-through log data show a significant improvement on search performance over the naive query log mining algorithm as well as the baseline search engine.

'''

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
    
    # print repr(stopped_tokens)
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
new = open("output/sample3/gensim_lda3.txt",'w')
for d in final_list:
	pid = docid_paperid.get(d)
	print d,pid
	new.write(pid + "\n")
print final_list
new.close()


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

no_topics = len(doc_set)/10 + 1

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
new = open("output/sample3/scikit_nmf3.txt",'w')
for d in final_list:
	pid = docid_paperid.get(d)
	print d,pid
	if(pid != None):
		new.write(pid + "\n")
print final_list
new.close()



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
new = open("output/sample3/scikit_nmf3.txt",'w')
for d in final_list:
	pid = docid_paperid.get(d)
	print d,pid
	if(pid != None):
		new.write(pid + "\n")
print final_list
new.close()


# for k,d in enumerate(lda):
# 	print d,k+1

