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
sample1:
Co authorship, graph model, topic clustering, random walk, citation recommendation.

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
Fingerprint recognition, Image matching, Approximation algorithms, Robustness, Polynomials, Biometrics, Databases, Large-scale systems, Bifurcation, Automation 

sample8:
Time synchronization, wireless sensor networks, clock synchronization

sample11:
local Gabor XOR patterns, LGXP, Face representation, Fishers linear discriminant, FLD, fusion, histogram

sample12:
Audio streams, inactive frames, steganography, Voice over Internet Protocol, VoIP

sample16:
Digital watermarking, hypothesis testing, multimedia authentication, semifragile

sample21:
Remote sensing, image classification, decision tree classifier, DTC, maximum likelihood classifier, MLC, ISODATA

sample22:
Data mining, parallel processing, classification, scalability, decision trees

sample23:
Classification, Naive Bayes, Semi naive Bayes, Feature selection, AODE

sample24:


sampel25:
Graph based, semi-supervised learning, Global smoothness, Label fitting, Graph cut, Basis matrix, Congruency approximation

sample 26:
Information Retrieval, query expansion,search engine, effectiveness

sample27:
Predictive models,  Size measurement, Software maintenance, Object oriented modeling, Software measurement, Software systems, Testing, Software engineering,Error analysis, Lead  

sample28:
multiple regression analysis, software reuse, Ada, software crisis, organizations, measurement, literature, domain capability, human factors, software tool, software metrics, software environment, software development effort, object-oriented design, repository development

sample29:
Unified modeling language, Documentation, Software maintenance, Object oriented modeling, Programming, Software standards, Software design, Software systems, Costs, Design engineerin

sample30:
Target-sensitive test suite generation, automatic fault isolation, procedure-calling convention, code generation, compiler testing and debugging

sample36:
Programming, Large-scale systems,Software quality,  Productivity, Computer architecture, Software reusability, NASA, Software systems, Software measurement, Software metrics

sample37:
Distributed systems middleware, parallel programming models, parallel and distributed Java, cluster, heterogeneous systems, distributed agents

sample38:
Scalability, smart grid, advanced metering infrastructure (AMI), meter data management system, MDMS, facility location problem

sample39:
Algorithm, distributed computing, interconnection network, multiprocessor scheduling.
Multiprocessing systems, Processor scheduling, Scheduling algorithm, NP-complete problem, Distributed computing, Delay, Algorithm design and analysis, Availability, Cost function, Shape  

sample40:
Component middleware, dynamic real-time task allocation, load balancing and admission control


sample41:
Distributed access control, access paths, role mapping, role discovery, role-based access control
Middleware, Real time systems, Load management, Application software, Admission control, Time factors, Timing, Quality of service, Control systems, Telecommunication control

sample52:
Audio-visual speech recognition, late integration, robustness, hidden Markov model, interframe correlation, neural network, stochastic optimization.

sample53:
trajectory, Dynamic programming, player detection, soccer analysis, tracking , Target tracking, Cameras, Layout, TV broadcasting, Video recording, Gunshot detection systems, Face detection, Dynamic programming, Multimedia communication, Lighting

sample54:
salient region, Dominant color, importance index, merging likelihood, nonparametric density estimation
Image segmentation, Merging, Image retrieval, Information retrieval, Color, Videos, Content based retrieval, Histograms, Phase estimation, Quantization 

sample55:
video-aware adaptation and communication, Adaptive media playout, cross-layer optimization, multimedia delivery over wireless networks, network control, packet scheduling.
Scheduling algorithm, Streaming media, Transmitters, Wireless LAN, Layout, Rate-distortion, Programmable control, Adaptive control, Motion control, Video sequences 

sample56:
skip criterion, Fast encoding, inter-layer prediction, motion estimation, scalable video coding

sample57:
adaptation, Acoustic modelling, subspace Gaussian mixture model, cross-lingual speech ,recognition, regularization

sample58:
Mismatch conditions, NIST SRE, overlap-masking effect, reverberation, speaker verification, Reverberation, Speech, Microphones, Licenses, Estimation, Speech enhancement

sample59:
room acoustics, Eigen values and eigen functions, finite difference, operator spectra, pseudo spectra
Boundary conditions,room Acoustics, Eigenvalues and eigenfunctions, Matrix decomposition, Stability analysis 

sample60:
polyphonic instrument identification, Acoustic scene analysis, music information retrieval, Instruments, Speech, Speech processing, Feature extraction, Harmonic analysis, Indexes,

sample61:
query-by-example spoken term detection, Dynamic time warping, fast search, frequency domain linear prediction, Speech, Mel frequency cepstral coefficient, Vectors, Speech processing, Frequency-domain analysis, Computational modeling




'''


given_fos = raw_input("choose 1\n{\n1:cs,\n2:Biology,\n3:chemistry...}:")
if(given_fos == '1'):
	given_fos = "0271BC14"
elif(given_fos == '2'):
	given_fos = "052C8328"
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
try:
	papers = get_relavent_papers(normalized_given_keywords,given_fos)
	new = open('biology_output/test_paperIDs.txt','w')
	for p in papers:
		new.write(str(p) + '\n')
	new.close()
	print "got papers"
except Exception as e:
	print "Keywords not searched. Error:", e