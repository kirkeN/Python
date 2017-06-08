def commonest_bigram(text):
	l=text.split()
	bi=[] #bigram in list
	matrix=[] #list of bigrams
	count=0 #counting bigram
	maxCount=0 #winner bigram, most counts
	maxBigram=[]

	for x in range(len(l)-1):
		bi.append(l[x])
		bi.append(l[x+1])
		matrix.append(bi)
		bi=[]

	for y in range(len(matrix)):
		for z in range(len(matrix)):
			if matrix[y]==matrix[z]:
				count=count+1
		if count>maxCount:
			maxCount=count
			maxBigram=matrix[y]
		count=0

	#print ("max bigram: {}".format(maxBigram))
	#print(tuple(maxBigram))
	return tuple(maxBigram)

#commonest_bigram("to be or to be or to not or to do something")

