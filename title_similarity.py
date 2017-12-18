
from compare_titles import sentence_similarity
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

given_title = raw_input("enter title:")


titles = {}
f = open("Rugved/toppapertitles_1692.txt",'r')
for line in f:
    paperID,ptitle = line.split('\t')
    ptitle = ptitle.strip('\n')
    titles[paperID] = ptitle
f.close()

# print titles
maxS=0
maxP=''
maxT=''
i=0
for paperID,title in titles.items():
    i+=1
    sim1 = sentence_similarity(given_title,title)
    sim2 = sentence_similarity(title,given_title)
    if(sim1>maxS):
        maxS=sim1
        maxP=paperID
        maxT=title
    titles[paperID] = [title,sim1,sim2]
    # if(i==2):
        # break

print maxS,maxP,maxT

i=0
new=open("Rugved/toppaper_with_title_similarity_1692.csv",'w')
new.write("Paper ID,Title,Sim1,Sim2\n")
for k,v in titles.items():
    # print v
    new.write(str(k) + ',"' + v[0] + '",' + str(v[1]) +',' + str(v[2])+ "\n")
    i+=1
    # if(i==2):
        # break
print i