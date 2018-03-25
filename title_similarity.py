
from compare_titles import sentence_similarity
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

given_title = raw_input("enter title:")
'''
Exploiting Fine Grained Co Authorship for Personalized Citation Recommendation

Detecting Computer Induced Errors in Remote Sensing JPEG Compression Algorithms

Optimizing web search using web click through data

Web Query Recommendation via Sequential Query Prediction

Personalized Web search for improving retrieval effectiveness

Hierarchical Clustering Algorithms for Document Datasets

A Model Based Method for the Computation of Fingerprints Orientation Field

A New Approach for Time Synchronization in Wireless Sensor Networks: Pairwise Broadcast Synchronization

sample12:
Steganography in Inactive Frames of VoIP Streams Encoded by Source Codec

sample16:
A Hypothesis Testing Approach to Semifragile Watermark Based Authentication

sample21:
Decision tree approach for classification of remotely sensed satellite data using open source support

sample22:
Parallel Formulations of Decision Tree Classification Algorithms

sample23:
Subsumption resolution: an efficient and effective technique for semi naive Bayesian learning

sample24:
An improved artificial bee colony algorithm for solving constrained optimization problems

sample25:
Graph based semi supervised learning via label fitting

sample26:
Qustioning query expansion: an examination of behaviour and parameters

sample27:
An empirical validation of object-oriented metrics in two different iterative software processes

sample28:
An empirical study of software reuse with special attention to Ada

sample29:
The impact of UML documentation on software maintenance: an experimental evaluation

sample30:
Automatic detection and diagnosis of faults in generated code for procedure calls

sample36:
Enabling reuse-based software development of large-scale systems

sample37:
Middleware Infrastructure for Parallel and Distributed Programming Models in Heterogeneous Systems 

sample38:
Scalable Distributed Communication Architectures to Support Advanced Metering Infrastructure in Smart Grid

sample39:
On improved duplication strategy for scheduling precedence constrained graphs in multiprocessor systems

sample40:
Configurable Middleware for Distributed Real-Time Systems with Aperiodic and Periodic Tasks

sample41:
Secure Collaboration in a Mediator-Free Distributed Environment

sample52:
Robust Audio-Visual Speech Recognition Based on Late Integration

sample53:
Graph-Based Multiplayer Detection and Tracking in Broadcast Soccer Videos

sample54:
Color-Based Image Salient Region Segmentation Using Novel Region Merging Strategy

sample55:
Content-Aware Playout and Packet Scheduling for Video Streaming Over Wireless Links

sample56:
A New Fast Encoding Algorithm Based on an Efficient Motion Estimation Process for the Scalable Video Coding Standard

sample57:
Cross-Lingual Subspace Gaussian Mixture Models for Low-Resource Speech Recognition

sample58:
Blind Spectral Weighting for Robust Speaker Identification under Reverberation Mismatch

sample59:
Spectral and Pseudospectral Properties of Finite Difference Models Used in Audio and Room Acoustics

sample60:
Musical Source Clustering and Identification in Polyphonic Audio

sample61:
Query-by-Example Spoken Term Detection using Frequency Domain Linear Prediction and Non-Segmental Dynamic Time Warping

'''

filtered_titles = {}
f = open("output/sample61/filtered_papers61_with_titles61.txt",'r')
for line in f:
    paperID,ptitle = line.split('\t')
    ptitle = ptitle.strip('\n')
    filtered_titles[paperID] = ptitle
f.close()

non_ref_titles = {}
f = open("output/sample61/papers_without_ref61_with_titles61.txt",'r')
for line in f:
    paperID,ptitle = line.split('\t')
    ptitle = ptitle.strip('\n')
    non_ref_titles[paperID] = ptitle
f.close()


# print filtered_titles
maxS=0
maxP=''
maxT=''
i=0
for paperID,title in filtered_titles.items():
    i+=1
    sim1 = sentence_similarity(given_title,title)
    sim2 = sentence_similarity(title,given_title)
    if(sim1>maxS):
        maxS=sim1
        maxP=paperID
        maxT=title
    filtered_titles[paperID] = [title,sim1,sim2]
    # if(i==2):
        # break

print maxS,maxP,maxT

maxS=0
maxP=''
maxT=''
i=0
for paperID,title in non_ref_titles.items():
    i+=1
    sim1 = sentence_similarity(given_title,title)
    sim2 = sentence_similarity(title,given_title)
    if(sim1>maxS):
        maxS=sim1
        maxP=paperID
        maxT=title
    non_ref_titles[paperID] = [title,sim1,sim2]
    # if(i==2):
        # break

print maxS,maxP,maxT

i=0
new=open("output/sample61/papers_without_refernces_titSim.csv",'w')
new.write("Paper ID,Title,Sim1,Sim2\n")
for k,v in non_ref_titles.items():
    # print v
    new.write(str(k) + ',"' + v[0] + '",' + str(v[1]) +',' + str(v[2])+ "\n")
    i+=1
    # if(i==2):
        # break
print i


i=0
new=open("output/sample61/filtered_papers_titSim.csv",'w')
new.write("Paper ID,Title,Sim1,Sim2\n")
for k,v in filtered_titles.items():
    # print v
    new.write(str(k) + ',"' + v[0] + '",' + str(v[1]) +',' + str(v[2])+ "\n")
    i+=1
    # if(i==2):
        # break
print i