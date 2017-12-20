
from compare_titles import sentence_similarity
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

given_title = raw_input("enter title:")
'''
Exploiting Fine-Grained Co-Authorship for Personalized Citation Recommendation

Detecting Computer-Induced Errors in Remote-Sensing JPEG Compression Algorithms

Optimizing web search using web click-through data

Web Query Recommendation via Sequential Query Prediction

Personalized Web search for improving retrieval effectiveness

Hierarchical Clustering Algorithms for Document Datasets
'''

filtered_titles = {}
f = open("output/sample6/filtered_papers6_with_titles6.txt",'r')
for line in f:
    paperID,ptitle = line.split('\t')
    ptitle = ptitle.strip('\n')
    filtered_titles[paperID] = ptitle
f.close()

non_ref_titles = {}
f = open("output/sample6/papers_without_ref6_with_titles6.txt",'r')
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
new=open("output/sample6/papers_without_refernces_titSim.csv",'w')
new.write("Paper ID,Title,Sim1,Sim2\n")
for k,v in non_ref_titles.items():
    # print v
    new.write(str(k) + ',"' + v[0] + '",' + str(v[1]) +',' + str(v[2])+ "\n")
    i+=1
    # if(i==2):
        # break
print i


i=0
new=open("output/sample6/filtered_papers_titSim.csv",'w')
new.write("Paper ID,Title,Sim1,Sim2\n")
for k,v in filtered_titles.items():
    # print v
    new.write(str(k) + ',"' + v[0] + '",' + str(v[1]) +',' + str(v[2])+ "\n")
    i+=1
    # if(i==2):
        # break
print i