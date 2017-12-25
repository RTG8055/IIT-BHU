from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer
import re
import gensim

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def remove_non_ascii_2(text):

    return re.sub(r'[^\x00-\x7F]',' ', text)

doc_set=[]
docid_paperid={}
file = open('output/sample3/paperids3_abstract.txt','r')
i=0
for line in file:
	i+=1
	line = line.strip('\n|\r').split('\t')
	line[1] = remove_non_ascii_2(line[1])
	doc_set.append(line[1])
	docid_paperid[i]=line[0]
# print doc_set
file.close()

journal_set={}
with open("output/sample3/paperids3_journals_conf_title.txt",'r') as f:
	i=0
	for line in f:
		i+=1
		line = line.strip("\n")
		line = line.split("\t")
		journal = line[1].split("<--")[0]
		# print repr(journal)
		journal_set[line[0]] = [journal,line[1].split("<--")[1]]

print len(journal_set),len(doc_set)

given_abs = raw_input("enter abstract:")
doc_set.append(remove_non_ascii_2(given_abs))

'''
sample1:
In the era of big scholarly data, citation recommendation is playing an increasingly significant role as it solves information overload issues by automatically suggesting relevant references that align with researchers interests. Many state-of-the-art models have been utilized for citation recommendation, among which graph-based models have garnered significant attention, due to their flexibility in integrating rich information that influences users preferences. Co-authorship is one of the key relations in citation recommendation, but it is usually regarded as a binary relation in current graph-based models. This binary modeling of co-authorship is likely to result in information loss, such as the loss of strong or weak relationships between specific research topics. To address this issue, we present a fine-grained method for co-authorship modeling that incorporates the co author network structure and the topics of their published articles. Then, we design a three layered graph based recommendation model that integrates fine grained co authorship as well as author paper, paper citation, and paper keyword relations. Our model effectively generates query oriented recommendations using a simple random walk algorithm. Extensive experiments conducted on a subset of the anthology network data set for performance evaluation demonstrate that our method outperforms other models in terms of both Recall and NDCG.

sample2:
The JPEG image compression standard is very sensitive to errors. Even though it contains error resilience features, it cannot easily cope with induced errors from computer soft faults prevalent in remote-sensing applications. Hence, new fault tolerance detection methods are developed to sense the soft errors in major parts of the system while also protecting data across the boundaries where data flow from one subsystem to the other. The design goal is to guarantee no compressed or decompressed data contain computer-induced errors without detection. Detection methods are expressed at the algorithm level so that a wide range of hardware and software implementation techniques can be covered by the fault tolerance procedures while still maintaining the JPEG output format. The major subsystems to be addressed are the discrete cosine transform, quantizer, entropy coding, and packet assembly. Each error detection method is determined by the data representations within the subsystem or across the boundaries. They vary from real number parities in the DCT to bit-level residue codes in the quantizer, cyclic redundancy check parities for entropy coding, and packet assembly. The simulation results verify detection performances even across boundaries while also examining roundoff noise effects in detecting computer-induced errors in processing steps.

sample3:
The performance of web search engines may often deteriorate due to the diversity and noisy information contained within web pages. User click-through data can be used to introduce more accurate description (metadata) for web pages, and to improve the search performance. However, noise and incompleteness, sparseness, and the volatility of web pages and queries are three major challenges for research work on user click-through log mining. In this paper, we propose a novel iterative reinforced algorithm to utilize the user click-through data to improve search performance. The algorithm fully explores the interrelations between queries and web pages, and effectively finds "virtual queries" for web pages and overcomes the challenges discussed above. Experiment results on a large set of MSN click-through log data show a significant improvement on search performance over the naive query log mining algorithm as well as the baseline search engine.

sample4:
Web query recommendation has long been considered a key feature of search engines. Building a good Web query recommendation system, however, is very difficult due to the fundamental challenge of predicting users' search intent, especially given the limited user context information. In this paper, we propose a novel "sequential query prediction" approach that tries to grasp a user's search intent based on his/her past query sequence and its resemblance to historical query sequence models mined from massive search engine logs. Different query sequence models were examined, including the naive variable length N-gram model, Variable Memory Markov (VMM) model, and our proposed Mixture Variable Memory Markov (MVMM) model. Extensive experiments were conducted to benchmark our sequence prediction algorithms against two conventional pairwise approaches on large-scale search logs extracted from a commercial search engine. Results show that the sequence-wise approaches significantly outperform the conventional pair-wise ones in terms of prediction accuracy. In particular, our MVMM approach, consistently leads the pack, making it an effective and practical approach towards Web query recommendation.

sample5:
Current Web search engines are built to serve all users, independent of the special needs of any individual user. Personalization of Web search is to carry out retrieval for each user incorporating his/her interests. We propose a novel technique to learn user profiles from users' search histories. The user profiles are then used to improve retrieval effectiveness in Web search. A user profile and a general profile are learned from the user's search history and a category hierarchy, respectively. These two profiles are combined to map a user query into a set of categories which represent the user's search intention and serve as a context to disambiguate the words in the user's query. Web search is conducted based on both the user query and the set of categories. Several profile learning and category mapping algorithms and a fusion algorithm are provided and evaluated. Experimental results indicate that our technique to personalize Web search is both effective and efficient.

sample6:
Fast and high-quality document clustering algorithms play an important role in providing intuitive navigation and browsing mechanisms by organizing large amounts of information into a small number of meaningful clusters. In particular, clustering algorithms that build meaningful hierarchies out of large document collections are ideal tools for their interactive visualization and exploration as they provide data-views that are consistent, predictable, and at different levels of granularity. This paper focuses on document clustering algorithms that build such hierarchical solutions and (i) presents a comprehensive study of partitional and agglomerative algorithms that use different criterion functions and merging schemes, and (ii) presents a new class of clustering algorithms called constrained agglomerative algorithms, which combine features from both partitional and agglomerative approaches that allows them to reduce the early-stage errors made by agglomerative methods and hence improve the quality of clustering solutions. The experimental evaluation shows that, contrary to the common belief, partitional algorithms always lead to better solutions than agglomerative algorithms; making them ideal for clustering large document collections due to not only their relatively low computational requirements, but also higher clustering quality. Furthermore, the constrained agglomerative methods consistently lead to better solutions than agglomerative methods alone and for many cases they outperform partitional methods, as well.

sample7:
As a global feature of fingerprints, the orientation field is very important for automatic fingerprint recognition. Many algorithms have been proposed for orientation field estimation, but their results are unsatisfactory, especially for poor quality fingerprint images. In this paper, a model-based method for the computation of orientation field is proposed. First a combination model is established for the representation of the orientation field by considering its smoothness except for several singular points, in which a polynomial model is used to describe the orientation field globally and a point-charge model is taken to improve the accuracy locally at each singular point. When the coarse field is computed by using the gradient-based algorithm, a further result can be gained by using the model for a weighted approximation. Due to the global approximation, this model-based orientation field estimation algorithm has a robust performance on different fingerprint images. A further experiment shows that the performance of a whole fingerprint recognition system can be improved by applying this algorithm instead of previous orientation estimation methods. 

sample8:
This letter proposes an energy-efficient clock synchronization scheme for Wireless Sensor Networks (WSNs)based on a novel time synchronization approach. Within the proposed synchronization approach, a subset of sensor nodes are synchronized by overhearing the timing message exchanges of a pair of sensor nodes. Therefore, a group of sensor nodes can be synchronized without sending any extra messages. This paper brings two main contributions: 1. Development of a novel synchronization approach which can be partially or fully applied for implementation of new synchronization protocols and for improving the performance of existing time synchronization  protocols. 2. Design of a time synchronization scheme which significantly reduces the overall network-wide energy consumption without incurring any loss of synchronization accuracy compared to other well-known schemes.

sample9:
We develop new multiscale amplitude-modulation frequency-modulation (AM-FM) demodulation methods for image processing. The approach is based on three basic ideas: (i) AM-FM demodulation using a new multiscale filterbank, (ii) new, accurate methods for instantaneous frequency (IF) estimation, and (iii) multiscale least squares AM-FM reconstructions. In particular, we introduce a variable-spacing local linear phase (VS-LLP) method for improved instantaneous frequency (IF) estimation and compare it to an extended quasilocal method and the quasi-eigen function approximation (QEA). It turns out that the new VS-LLP method is a generalization of the QEA method where we choose the best integer spacing between the samples to adapt as a function of frequency. We also introduce a new quasi-local method (QLM) for IF and IA estimation and discuss some of its advantages and limitations. The new IF estimation methods lead to significantly improved estimates. We present different multiscale decompositions to show that the proposed methods can be used to reconstruct and analyze general images.

sample12:
This paper describes a novel high-capacity steganography algorithm for embedding data in the inactive frames of low bit rate audio streams encoded by G.723.1 source codec, which is used extensively in Voice over Internet Protocol (VoIP). This study reveals that, contrary to existing thought, the inactive frames of VoIP streams are more suitable for data embedding than the active frames of the streams; that is, steganography in the inactive audio frames attains a larger data embedding capacity than that in the active audio frames under the same imperceptibility. By analyzing the concealment of steganography in the inactive frames of low bit rate audio streams encoded by G.723.1 codec with 6.3 kb/s, the authors propose a new algorithm for steganography in different speech parameters of the inactive frames. Performance evaluation shows embedding data in various speech parameters led to different levels of concealment. An improved voice activity detection algorithm is suggested for detecting inactive audio frames taking into packet loss account. Experimental results show our proposed steganography algorithm not only achieved perfect imperceptibility but also gained a high data embedding rate up to 101 bits/frame, indicating that the data embedding capacity of the proposed algorithm is very much larger than those of previously suggested algorithms.

sample16:
This paper studies the problem of achieving watermark semifragility in watermark-based authentication systems through a composite hypothesis testing approach. Embedding a semifragile watermark serves to distinguish legitimate distortions caused by signal-processing manipulations from illegitimate ones caused by malicious tampering. This leads us to consider authentication verification as a composite hypothesis testing problem with the watermark as side information. Based on the hypothesis testing model, we investigate effective embedding strategies to assist the watermark verifier to make correct decisions. Our results demonstrate that quantization-based watermarking is more appropriate than spread-spectrum-based methods to achieve the semifragility tradeoff between two error probabilities. This observation is confirmed by a case study of an additive Gaussian white noise channel with a Gaussian source using two figures of merit: 1) relative entropy of the two hypothesis distributions and 2) the receiver operating characteristic. Finally, we focus on common signal-processing distortions, such as JPEG compression and image filtering, and investigate the discrimination statistic and optimal decision regions to distinguish legitimate and illegitimate distortions. The results of this paper show that our approach provides insights for authentication watermarking and allows for better control of semifragility in specific applications.

sample21:
In this study, an attempt has been made to develop a decision tree classification (DTC) algorithm for classification of remotely sensed satellite data (Landsat TM) using open source support. The decision tree is constructed by recursively partitioning the spectral distribution of the training dataset using WEKA, open source data mining software. The classified image is compared with the image classified using classical ISODATA clustering and Maximum Likelihood Classifier (MLC) algorithms. Classification result based on DTC method provided better visual depiction than results produced by ISODATA clustering or by MLC algorithms. The overall accuracy was found to be 90% (kappa = 0.88) using the DTC, 76.67% (kappa = 0.72) using the Maximum Likelihood and 57.5% (kappa = 0.49) using ISODATA clustering method. Based on the overall accuracy and kappa statistics, DTC was found to be more preferred classification approach than others

sample22:
Classification decision tree algorithms are used extensively for data mining in many domains such as retail target marketing, fraud detection, etc. Highly parallel algorithms for constructing classification decision trees are desirable for dealing with large data sets in reasonable amount of time. Algorithms for building classification decision trees have a natural concurrency, but are difficult to parallelize due to the inherent dynamic nature of the computation. In this paper, we present parallel formulations of classification decision tree learning algorithm based on induction. We describe two basic parallel formulations. One is based on Synchronous Tree Construction Approach and the other is based on Partitioned Tree Construction Approach. We discuss the advantages and disadvantages of using these methods and propose a hybrid method that employs the good features of these methods. We also provide the analysis of the cost of computation and communication of the proposed hybrid method. Moreover, experimental results on an IBM SP-2 demonstrate excellent speedups and scalability.

sample23:
Semi-naive Bayesian techniques seek to improve the accuracy of naive Bayes (NB) by relaxing the attribute independence assumption. We present a new type of semi-naive Bayesian operation, Subsumption Resolution (SR), which efficiently identifies occurrences of the specialization-generalization relationship and eliminates generalizations at classification time. We extend SR to Near-Subsumption Resolution (NSR) to delete near–generalizations in addition to generalizations. We develop two versions of SR: one that performs SR during training, called eager SR (ESR), and another that performs SR during testing, called lazy SR (LSR). We investigate the effect of ESR, LSR, NSR and conventional attribute elimination (BSE) on NB and Averaged One-Dependence Estimators (AODE), a powerful alternative to NB. BSE imposes very high training time overheads on NB and AODE accompanied by varying decreases in classification time overheads. ESR, LSR and NSR impose high training time and test time overheads on NB. However, LSR imposes no extra training time overheads and only modest test time overheads on AODE, while ESR and NSR impose modest training and test time overheads on AODE. Our extensive experimental comparison on sixty UCI data sets shows that applying BSE, LSR or NSR to NB significantly improves both zero-one loss and RMSE, while applying BSE, ESR or NSR to AODE significantly improves zero-one loss and RMSE and applying LSR to AODE significantly improves zero-one loss. The Friedman test and Nemenyi test show that AODE with ESR or NSR have a significant zero-one loss and RMSE advantage over Logistic Regression and a zero-one loss advantage over Weka’s LibSVM implementation with a grid parameter search on categorical data. AODE with LSR has a zero-one loss advantage over Logistic Regression and comparable zero-one loss with LibSVM. Finally, we examine the circumstances under which the elimination of near-generalizations proves beneficial.

sample25:
The global smoothness and the local label fitting are two key issues for estimating the function on the graph in graph based semi-supervised learning (GSSL). The unsupervised normalized cut method can provide a more reasonable criterion for learning the global smoothness of the data than classic GSSL methods. However, the semi-supervised norm of the normalized cut, which is a NP-hard problem, has not been studied well. In this paper, a new GSSL framework is proposed by extending normalized cut to its semi-supervised norm. The NP-hard semi-supervised normalized cut problem is innovatively solved by effective algorithms. In addition, we can design more reasonable local label fitting terms than conventional GSSL methods. Other graph cut methods are also investigated to extend the proposed semi-supervised learning algorithms. Furthermore, we incorporate the nonnegative matrix factorization with the proposed learning algorithms to solve the out-of-sample problem in semi-supervised learning. Solutions obtained by the proposed algorithms are sparse, nonnegative and congruent with unit matrix. Experiment results on several real benchmark datasets indicate that the proposed algorithms achieve good results compared with state-of-art methods.

sample26:
In information retrieval, queries can fail to find documents due to mismatch in terminology. Query expansion is a well-known technique addressing this problem, where additional query terms are automatically chosen from highly ranked documents, and it has been shown to be effective at improving query performance. However, current techniques for query expansion use fixed values for key parameters, determined by tuning on test collections. In this paper we show that these parameters may not be generally applicable, and more significantly that the assumption that the same parameter settings can be used for all queries is invalid. Using detailed experiments with two test collections, we demonstrate that new methods for choosing parameters must be found. However, our experiments also demonstrate that there is considerable further scope for improvement to effectiveness through better query expansion.

sample27:
Object-oriented (OO) metrics are used mainly to predict software engineering activities/efforts such as maintenance effort, error proneness, and error rate. There have been discussions about the effectiveness of metrics in different contexts. In this paper, we present an empirical study of OO metrics in two iterative processes: the short-cycled agile process and the long-cycled framework evolution process. We find that OO metrics are effective in predicting design efforts and source lines of code added, changed, and deleted in the short-cycled agile process and ineffective in predicting the same aspects in the long-cycled framework process. This leads us to believe that OO metrics' predictive capability is limited to the design and implementation changes during the development iterations, not the long-term evolution of an established system in different releases.

sample28:
Over the past several decades, numerous software technologies have been developed for overcoming the software crisis. Among these technologies, reuse has been recognized as one of the most important software technologies. Recently, it has gained substantial attention as a possible solution to the software crisis in Ada and other software communities. The purpose of this empirical study is to examine how organizations actually exploit reuse technologies and evaluates how reuse factors affect the rate of reuse in an organization. This study is an attempt to enhance the measurement of the rate of reuse and the effectiveness of reuse by establishing conceptual foundations in the literature for reuse and conducting an empirical investigation of organizations using Ada technology. This study differentiated software reuse into six criteria: domain, human, tool, organization, software metrics, and environment. The results of this study show that the rate of reuse significantly depends upon reuse capability, software development effort, object-oriented design capability, repository development effort, Ada technology capability, and domain capability.

sample29:
The Unified Modeling Language (UML) is becoming the de facto standard for software analysis and design modeling. However, there is still significant resistance to model-driven development in many software organizations because it is perceived to be expensive and not necessarily cost-effective. Hence, it is important to investigate the benefits obtained from modeling. As a first step in this direction, this paper reports on controlled experiments, spanning two locations, that investigate the impact of UML documentation on software maintenance. Results show that, for complex tasks and past a certain learning curve, the availability of UML documentation may result in significant improvements in the functional correctness of changes as well as the quality of their design. However, there does not seem to be any saving of time. For simpler tasks, the time needed to update the UML documentation may be substantial compared with the potential benefits, thus motivating the need for UML tools with better support for software maintenance

sample30:
In this paper, we present a compiler testing technique that closes the gap between existing compiler implementations and correct compilers. Using formal specifications of procedure-calling conventions, we have built a target-sensitive test suite generator that builds test cases for a specific aspect of compiler code generators: the procedure-calling sequence generator. By exercising compilers with these specification-derived target-specific test suites, our automated testing tool has exposed bugs in every compiler tested on the MIPS and one compiler on the SPARC. These compilers include some that have been in heavy use for many years. Once a fault has been detected, the system can often suggest the nature of the problem. The testing system is an invaluable tool for detecting, isolating, and correcting faults in today's compilers.

sample36:
Software reuse enables developers to leverage past accomplishments and facilitates significant improvements in software productivity and quality. Software reuse catalyzes improvements in productivity by avoiding redevelopment and improvements in quality by incorporating components whose reliability has already been established. This study addresses a pivotal research issue that underlies software reuse - what factors characterize successful software reuse in large-scale systems. The research approach is to investigate, analyze, and evaluate software reuse empirically by mining software repositories from a NASA software development environment that actively reuses software. This software environment successfully follows principles of reuse-based software development in order to achieve an average reuse of 32 percent per project, which is the average amount of software either reused or modified from previous systems. We examine the repositories for 25 software systems ranging from 3,000 to 112,000 source lines from this software environment. We analyze four classes of software modules: modules reused without revision, modules reused with slight revision (<25 percent revision), modules reused with major revision (/spl ges/25 percent revision), and newly developed modules. We apply nonparametric statistical models to compare numerous development variables across the 2,954 software modules in the systems. We identify two categories of factors that characterize successful reuse-based software development of large-scale systems: module design factors and module implementation factors. We also evaluate the fault rates of the reused, modified, and newly developed modules. The module design factors that characterize module reuse without revision were (after normalization by size in source lines): few calls to other system modules, many calls to utility functions, few input-output parameters, few reads and writes, and many comments. The module implementation factors that characterize module reuse without revision were small size in source lines and (after normalization by size in source lines): low development effort and many assignment statements. The modules reused without revision had the fewest faults, fewest faults per source line, and lowest fault correction effort. The modules reused with major revision had the highest fault correction effort and highest fault isolation effort as wed as the most changes, most changes per source line, and highest change correction effort. In conclusion, we outline future research directions that build on these software reuse ideas and strategies.

sample37:
We introduce a middleware infrastructure that provides software services for developing and deploying high-performance parallel programming models and distributed applications on clusters and networked heterogeneous systems. This middleware infrastructure utilizes distributed agents residing on the participating machines and communicating with one another to perform the required functions. An intensive study of the parallel programming models in Java has helped identify the common requirements for a runtime support environment, which we used to define the middleware functionality. A Java-based prototype, based on this architecture, has been developed along with a Java object-passing interface (JOPI) class library. Since this system is written completely in Java, it is portable and allows executing programs in parallel across multiple heterogeneous platforms. With the middleware infrastructure, users need not deal with the mechanisms of deploying and loading user classes on the heterogeneous system. Moreover, details of scheduling, controlling, monitoring, and executing user jobs are hidden, while the management of system resources is made transparent to the user. Such uniform services are essential for facilitating the development and deployment of scalable high-performance Java applications on clusters and heterogeneous systems. An initial deployment of a parallel Java programming model over a heterogeneous, distributed system shows good performance results. In addition, a framework for the agents' startup mechanism and organization is introduced to provide scalable deployment and communication among the agents.

sample38:
In this paper, we investigate the scalability of three communication architectures for advanced metering infrastructure (AMI) in smart grid. AMI in smart grid is a typical cyber-physical system (CPS) example, in which large amount of data from hundreds of thousands of smart meters are collected and processed through an AMI communication infrastructure. Scalability is one of the most important issues for the AMI deployment in smart grid. In this study, we introduce a new performance metric, accumulated bandwidthdistance product (ABDP), to represent the total communication resource usages. For each distributed communication architecture, we formulate an optimization problem and obtain the solutions for minimizing the total cost of the system that considers both the ABDP and the deployment cost of the meter data management system (MDMS). The simulation results indicate the significant benefits of the distributed communication architectures over the traditional centralized one. More importantly, we analyze the scalability of the total cost of the communication system (including MDMS) with regard to the traffic load on the smart meters for both the centralized and the distributed communication architectures. Through the closed form expressions obtained in our analysis, we demonstrate that the total cost for the centralized architecture scales linearly as O(λN), with N being the number of smart meters, and λ being the average traffic rate on a smart meter. In contrast, the total cost for the fully distributed communication architecture is O(λ2/3 N2/3), which is significantly lower.

sample39:
Scheduling precedence constrained task graphs, with or without duplication, is one of the most challenging NP-complete problems in parallel and distributed computing systems. Duplication heuristics are more effective, in general, for fine grain task graphs and for networks with high communication latencies. However, most of the available duplication algorithms are designed under the assumption of unbounded availability of fully connected processors, and lie in a high complexity range. Low complexity optimal duplication algorithms work under restricted cost and/or shape parameters for the task graphs. Further, the required number of processors grows in proportion to the task-graph size significantly. An improved duplication strategy is proposed that works for arbitrary task graphs, with a limited number of interconnection-constrained processors. Unlike most other algorithms that replicate all possible parents/ancestors of a given task, the proposed algorithm tends to avoid redundant duplications and duplicates the nodes selectively, only if it helps in improving the performance. This results in lower duplications and also lower time and space complexity. Simulation results are presented for clique and an interconnection-constrained network topology with random and regular benchmark task graph suites, representing a variety of parallel numerical applications. Performance, in terms of normalized schedule length and efficiency, is compared with some of the well-known and recently proposed algorithms. The suggested algorithm turns out to be most efficient, as it generates better or comparable schedules with remarkably less processor consumption.

sample40:
Different distributed real-time systems (DRS) must handle aperiodic and periodic events under diverse sets of requirements. While existing middleware such as Real-Time CORBA has shown promise as a platform for distributed systems with time constraints, it lacks flexible configuration mechanisms needed to manage end-to-end timing easily for a wide range of different DRS with both aperiodic and periodic events. The primary contribution of this work is the design, implementation, and performance evaluation of the first configurable component middleware services for admission control and load balancing of aperiodic and periodic event handling in DRS. Empirical results demonstrate the need for, and the effectiveness of, our configurable component middleware approach in supporting different applications with aperiodic and periodic events, and providing a flexible software platform for DRS with end-to-end timing constraints

sample41:
The Internet and related technologies have made multidomain collaborations a reality. Collaboration enables domains to effectively share resources; however it introduces several security and privacy challenges. Managing security in the absence of a central mediator is even more challenging. In this paper, we propose a distributed secure interoperability framework for mediator-free collaboration environments. We introduce the idea of secure access paths which enables domains to make localized access control decisions without having global view of the collaboration. We also present a path authentication technique for proving path authenticity. Furthermore, we present an on-demand path discovery algorithms that enable domains to securely discover paths in the collaboration environment. We implemented a simulation of our proposed framework and ran experiments to investigate the effect of several design parameters on our proposed access path discovery algorithm.

sample52:
Audio-visual speech recognition (AVSR) using acoustic and visual signals of speech has received attention because of its robustness in noisy environments. In this paper, we present a late integration scheme-based AVSR system whose robustness under various noise conditions is improved by enhancing the performance of the three parts composing the system. First, we improve the performance of the visual subsystem by using the stochastic optimization method for the hidden Markov models as the speech recognizer. Second, we propose a new method of considering dynamic characteristics of speech for improved robustness of the acoustic subsystem. Third, the acoustic and the visual subsystems are effectively integrated to produce final robust recognition results by using neural networks. We demonstrate the performance of the proposed methods via speaker-independent isolated word recognition experiments. The results show that the proposed system improves robustness over the conventional system under various noise conditions without a priori knowledge about the noise contained in the speech.

sample53:
In this paper, we propose a graph-based approach for detecting and tracking multiple players in broadcast soccer videos. In the first stage, the position of the players in each frame is determined by removing the non player regions. The remaining pixels are then grouped using a region growing algorithm to identify probable player candidates. A directed weighted graph is constructed, where probable player candidates correspond to the nodes of the graph while each edge links candidates in a frame with the candidates in next two consecutive frames. Finally, dynamic programming is applied to find the trajectory of each player. Experiments with several sequences from broadcasted videos of international soccer matches indicate that the proposed approach is able to track the players reasonably well even under varied illumination and ground conditions.

sample54:
In this paper, we propose a novel unsupervised algorithm for the segmentation of salient regions in color images. There are three phases in this algorithm. In the first phase, we use nonparametric density estimation to extract candidates of dominant colors in an image, which are then used for the quantization of the image. The label map of the quantized image forms initial regions of segmentation. In the second phase, we define salient region with two properties; i.e., conspicuous; compact and complete. According to the definition, two new parameters are proposed. One is called ldquoImportance indexrdquo, which is used to measure the importance of a region, and the other is called ldquoMerging likelihoodrdquo, which is utilized to measure the suitability of region merging. Initial regions are merged based on the two new parameters. In the third phase, a similarity check is performed to further merge the surviving regions. Experimental results show that the proposed method achieves excellent segmentation performance for most of our test images. In addition, the computation is very efficient.

sample55:
Media streaming over wireless links is a challenging problem due to both the unreliable, time-varying nature of the wireless channel and the stringent delivery requirements of media traffic. In this paper, we use joint control of packet scheduling at the transmitter and content-aware playout at the receiver, so as to maximize the quality of media streaming over a wireless link. Our contributions are twofold. First, we formulate and study the problem of joint scheduling and playout control in the framework of Markov decision processes. Second, we propose a novel content-aware adaptive playout control, that takes into account the content of a video sequence, and in particular the motion characteristics of different scenes. We find that the joint scheduling and playout control can significantly improve the quality of the received video, at the expense of only a small amount of playout slowdown. Furthermore, the content-aware adaptive playout places the slowdown preferentially in the low-motion scenes, where its perceived effect is lower.

sample56:
In this paper, a new fast encoding algorithm based on an efficient motion estimation (ME) process is proposed to accelerate the encoding speed of the scalable video coding standard. Through analysis of the ME process performed in the enhancement layer, we discovered that there are redundant MEs and some MEs can simply be unified at the fully overlapped search range (FOSR). In order to make the unified ME more efficient, we theoretically derive a skip criterion to determine whether the computation of rate-distortion cost can be omitted. In the proposed algorithm, the unnecessary MEs are removed and a unified ME with the skip criterion is applied in the FOSR. Simulation results show that the proposed algorithm achieves computational savings of approximately 46% without coding performance degradation when compared with the original SVC encoder.

sample57:
This paper studies cross-lingual acoustic modeling in the context of subspace Gaussian mixture models (SGMMs). SGMMs factorize the acoustic model parameters into a set that is globally shared between all the states of a hidden Markov model (HMM) and another that is specific to the HMM states. We demonstrate that the SGMM global parameters are transferable between languages, particularly when the parameters are trained multilingually. As a result, acoustic models may be trained using limited amounts of transcribed audio by borrowing the SGMM global parameters from one or more source languages, and only training the state-specific parameters on the target language audio. Model regularization using ℓ1-norm penalty is shown to be particularly effective at avoiding overtraining and leading to lower word error rates. We investigate maximum a posteriori (MAP) adaptation of subspace parameters in order to reduce the mismatch between the SGMM global parameters of the source and target languages. In addition, monolingual and cross-lingual speaker adaptive training is used to reduce the model variance introduced by speakers. We have systematically evaluated these techniques by experiments on the GlobalPhone corpus.

sample58:
Room reverberation poses various deleterious effects on performance of automatic speech systems. Speaker identification (SID) performance, in particular, degrades rapidly as reverberation time increases. Reverberation causes two forms of spectro-temporal distortions on speech signals: i) self-masking which is due to early reflections and ii) overlap-masking which is due to late reverberation. Overlap-masking effect of reverberation has been shown to have a greater adverse impact on performance of speech systems. Motivated by this fact, this study proposes a blind spectral weighting (BSW) technique for suppressing the reverberation overlap-masking effect on SID systems. The technique is blind in the sense that prior knowledge of neither the anechoic signal nor the room impulse response is required. Performance of the proposed technique is evaluated on speaker verification tasks under simulated and actual reverberant mismatched conditions. Evaluations are conducted in the context of the conventional GMM-UBM as well as the state-of-the-art i-vector based systems. The GMM-UBM experiments are performed using speech material from a new data corpus well suited for speaker verification experiments under actual reverberant mismatched conditions, entitled MultiRoom8. The i-vector experiments are carried out with microphone (interview and phonecall) data from the NIST SRE 2010 extended evaluation set which are digitally convolved with three different measured room impulse responses extracted from the Aachen impulse response (AIR) database. Experimental results prove that incorporating the proposed blind technique into the standard MFCC feature extraction framework yields significant improvement in SID performance under reverberation mismatch.

sample59:
Finite difference solutions to the wave equation are simple and flexible modeling tools for approximating physical systems in audio and room acoustics. Each model is characterized by a matrix operator and the time-stepping solution by a sequence of powers of the matrix. Spectral decomposition of representative matrices provide some practical insight into solution behavior and in some cases stability. In addition to computed eigenvalue spectra, pseudospectra provide a description of numerical amplification due to rounding errors in floating point arithmetic. The matrix analysis also shows that certain boundary implementations in non-cuboid geometries can be unstable despite satisfying conditions derived from von Neumann and normal mode analyses.

sample60:
For music transcription or musical source separation, apart from knowing the multi-F0 contours, it is also important to know which F0 has been played by which instrument. This paper focuses on this aspect, i.e. given the polyphonic audio along with its multiple F0 contours, the proposed system clusters them so as to decide `which instrument played when.' For the task of identifying the instrument or singers in the polyphonic audio, there are many supervised methods available. But many times individual source audio is not available for training. To address this problem, this paper proposes novel schemes using semi-supervised as well as unsupervised approach to source clustering. The proposed theoretical framework is based on auditory perception theory and is implemented using various tools like probabilistic latent component analysis and graph clustering, while taking into account various perceptual cues for characterizing a source. Experiments have been carried out over a wide variety of datasets - ranging from vocal to instrumental as well as from synthetic to real world music. The proposed scheme significantly outperforms a state of the art unsupervised scheme, which does not make use of the given F0 contours. The proposed semi-supervised approach also performs better than another semi-supervised scheme, which makes use of the given F0 information, in terms of computations as well as accuracy.

sample61:
The task of query-by-example spoken term detection (QbE-STD) is to find a spoken query within spoken audio data. Current state-of-the-art techniques assume zero prior knowledge about the language of the audio data, and thus explore dynamic time warping (DTW) based techniques for the QbE-STD task. In this paper, we use a variant of DTW based algorithm referred to as non-segmental DTW (NS-DTW), with a computational upper bound of O (mn) and analyze the performance of QbE-STD with Gaussian posteriorgrams obtained from spectral and temporal features of the speech signal. The results show that frequency domain linear prediction cepstral coefficients, which capture the temporal dynamics of the speech signal, can be used as an alternative to traditional spectral parameters such as linear prediction cepstral coefficients, perceptual linear prediction cepstral coefficients and Mel-frequency cepstral coefficients. We also introduce another variant of NS-DTW called fast NS-DTW (FNS-DTW) which uses reduced feature vectors for search. With a reduction factor of α ∈ ℕ, we show that the computational upper bound for FNS-DTW is O(mn/(α2)) which is faster than NS-DTW.

'''

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

# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=len(doc_set)/10, id2word = dictionary, passes=20)




# lda_corpus = ldamodel[corpus]
# i=0
# final_topic =0

# focus_doc = lda_corpus[len(doc_set)-1]
# tmax=0;topic_id=0
# for d in focus_doc:
# 	if(d[1]>tmax):
# 		tmax=d[1]
# 		topic_id=d[0]
# print topic_id

# final_list={}
# for doc in lda_corpus:
# 	i+=1
# 	if(i==len(doc_set)):
# 		continue
# 	# print doc
# 	for d in doc:
# 		if(d[0] == topic_id):
# 			final_list[i] = d[1]
# 	print doc,i

# final_list = sorted(final_list,key=final_list.__getitem__,reverse=True)
# new = open("output/sample1/gensim_lda1.txt",'w')
# for d in final_list:
# 	pid = docid_paperid.get(d)
# 	print d,pid
# 	new.write(pid + "\n")
# print final_list
# new.close()


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

nmf_scores={}
i=0
for d_id,doc in enumerate(nmf):
	i+=1
	for t_d,d in enumerate(doc):
		if(t_d == topic_id):
			nmf_scores[i] = d
	# print doc,i
# print nmf_scores,type(nmf_scores)
nmf_order = sorted(nmf_scores,key=nmf_scores.__getitem__,reverse=True)
# print type(nmf_order),nmf_order_dict2

new = open("output/sample3/scikit_nmf3.txt",'w')
# for d in nmf_order:
# 	pid = docid_paperid.get(d)
# 	print d,pid
# 	if(pid != None):
# 		new.write(pid + "\n")
# print nmf_order
# new.close()
i=0
written_journal=set()
for d in nmf_order:
	# i+=1
	if(d==len(doc_set)):
		continue
	pid = docid_paperid.get(d)
	journal = journal_set.get(pid)[0]
	# print d,pid,journal,i
	if(journal == "Information not present"):
		journal = raw_input("enter journal for:-" + journal_set.get(pid)[1] + ":")
	if(journal not in written_journal and journal != "s"):
		i+=1
		c = journal_set[pid]
		# print c
		c[0] = journal
		# print c
		journal_set[pid]=c
		new.write(str(i) + "." +journal + "\n")
		written_journal.add(journal)
	# if(i==25):
		# break
print nmf_order
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

lda_scores={}
i=0
for d_id,doc in enumerate(lda):
	i+=1
	# if(i==len(doc_set)):
		# continue
	# print doc
	for t_d,d in enumerate(doc):
		if(t_d == topic_id):
			lda_scores[i] = d
	# print doc,i

lda_order = sorted(lda_scores,key=lda_scores.__getitem__,reverse=True)
new = open("output/sample3/scikit_lda3.txt",'w')
# for d in lda_order:
# 	pid = docid_paperid.get(d)
# 	print d,pid
# 	if(pid != None):
# 		new.write(pid + "\n")
# print lda_order
# new.close()
i=0
written_journal=set()
for d in lda_order:
	# i+=1
	if(d==len(doc_set)):
		continue
	pid = docid_paperid.get(d)
	journal = journal_set.get(pid)[0]
	# print d,pid,journal,i
	if(journal == "Information not present"):
		journal = raw_input("enter journal for:-" + journal_set.get(pid)[1] + ":")
	if(journal not in written_journal and journal != "s"):
		i+=1
		c = journal_set[pid]
		# print c
		c[0] = journal
		# print c
		journal_set[pid]=c
		new.write(str(i) + "." +journal + "\n")
		written_journal.add(journal)
	# if(i==25):
		# break
print lda_order
new.close()



############
#Ranking lad and nmf wise
############
lda_ranks={}
nmf_ranks={}

i,j=0,0
prev1,prev2 = 0,0
for d1,d2 in zip(nmf_order,lda_order):
	if(not (i==0 and j==0)):
		if(prev1 != nmf_scores.get(d1)):
			i+=1
		if(prev2 != lda_scores.get(d2)):
			j+=1
	else:
		i+=1
		j+=1
	# print d1,i,d2,j,prev1,nmf_scores.get(d1),prev2,lda_scores.get(d2)
	nmf_ranks[d1] = i
	lda_ranks[d2] = j
	prev1,prev2= nmf_scores.get(d1),lda_scores.get(d2)



#######################
# Ranking algorithm:
#		for each document, rank=(rank in nmf list + rank in lda list) / 2
#######################

doc_rank = {}

for d1 in nmf_order:
	doc_rank[d1] = (nmf_ranks.get(d1) + lda_ranks.get(d1)) /2.0
	# print doc_rank[d1],nmf_ranks.get(d1),lda_ranks.get(d1),d1

doc_list = sorted(doc_rank,key=doc_rank.__getitem__)
# print doc_list

new = open("output/sample3/LN3.txt",'w')
i=0
written_journal=set()
for d in doc_list:
	# i+=1
	if(d==len(doc_set)):
		continue
	pid = docid_paperid.get(d)
	journal = journal_set.get(pid)[0]
	# print d,pid,journal,i
	if(journal == "Information not present"):
		journal = raw_input("enter journal for " + journal_set.get(pid)[1] + ":")
	if(journal not in written_journal and journal != "s"):
		i+=1
		c = journal_set[pid]
		# print c
		c[0] = journal
		# print c
		journal_set[pid]=c
		new.write(str(i) + "." +journal + "\n")
		written_journal.add(journal)
	# if(i==25):
		# break
print doc_list
new.close()
