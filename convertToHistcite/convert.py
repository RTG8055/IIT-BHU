import re

new = open("download_1.txt",'w')
h = open("../datasets/HistCiteSample.txt",'r')
i=0
for line in h:
	print repr(line)
	i+=1
	if(i==15):
		break
	
with open("../datasets/web_of_science_data/savedrecs(3).txt",'r') as old:
	i=0
	while(True):
		line = old.readline()
		prev=old.tell()
	# for line in old:
		print repr(line),line[0:2]
		# line = old.readline()
		# print repr(line)
		print i
		if(i == 0):
			print True
			new.write("FN ISI Export Format\n")
		elif(i==1):
			new.write(line)
		else:
			# line = old.readline()
			# while(line != '\n'):
			if(line[0:2] == 'AF' or line[0:2] == 'ID' or line[0:2] == 'DE' or line[0:2] == 'AB' or line[0:2] == 'C1' or line[0:2] == 'RP' or line[0:2] == 'EM' or line[0:2] == 'Z9' or line[0:2] == 'U1' or line[0:2] == 'U2' or line[0:2] == 'EI' or line[0:2] == 'PD' or line[0:2] == 'DI' or line[0:2] == 'WC' or line[0:2] == 'FU' or line[0:2] == 'FX'):
				# line = old.readline()
				while(True):
					prev = old.tell()
					line = old.readline()
				# for line in old:
					print line
					if(line[0] == ' '):
						continue
					else:
						old.seek(prev)
						break
				# continue
			elif(line[0:2] == 'VL'):
				new.write(line)
				new.write("IS "+ str(i))# random is value
			else:
				print line
				new.write(line)
				print old.tell(),len(line),line

				# for line2 in old:
				while True:
					prev2=old.tell()
					line2 = old.readline()
					print old.tell(),len(line2),line2
					if(line2[0] == ' '):
						new.write(line2)
					else:
						old.seek(prev2)
						break
		i+=1
		# if(i==100):
			# break

