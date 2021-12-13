try:
	fileFIRST=open('brown.txt')
except:
	print('File Cannot Be Opened!', fileFIRST)
	exit()
lines=fileFIRST.readlines()
fileFIRST.close()
dict={}
fileSECOND=open('output.txt','w')
for line in lines:
	words=line.split()
	length=len(words)
	for i in range(length-5):
		key=words[i]+' '+words[i+1]+' '+words[i+2]+' '+words[i+3]+' '+words[i+4]
		if key not in dict:
			dict[key]=1
		else:
			dict[key]+=1
max=None
for key in dict:
	result=key,dict[key]
	fileSECOND.write(str(result))
	fileSECOND.write('\n')
	if max is None or dict[key]>max:
			max=dict[key]
print('Максимальное количество: ',max)

