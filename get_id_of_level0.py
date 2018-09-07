import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

with open("FOS_groups_level_conf_sorted.txt") as f:
	i=0
	for line in f:
		i+=1
		l0 = line.split("\t")[0]
		l1 = line.split("\t")[1]
		
		if(l1[1] == '0'):
			continue
		else:
			print l0
		# print "line ",i
# 00F03FC7 -- Psycology
# 010EC23D -- Political Science
# 0205A1DB -- Mathematics
# 0259B070 -- Environmetnal Science
# 0271BC14 -- Computer science
# 04497984 -- Medicine
# 052C8328 -- Biology
# 05B091C0
# 073B64E4
# 0796A60A
# 07982D63
# 08473A1E
# 087C4600
# 0895A350
# 08974DB8
# 09ACE10E
# 0B0FEB68
# 0B7A44E7
# 0C41F50C