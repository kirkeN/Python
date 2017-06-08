import re
def transposition(text):
	regex = re.compile('[^0-9a-zA-Z]')
	l=text.split() #list of string
	row=[]
	matrix=[]
	for s in range(len(l)):
		l[s]=regex.sub('',l[s])
	
	while '' in l:
		l.remove('')
	while ' ' in l:
		l.remove(' ')
	
	max_word=max(l, key=len)

	for x in range(len(max_word)):   
		for y in range(len(l)):
			if len(l[y])>x: #and l[y][x].isalnum(): #have still alphanumeric chars?
				row.append(l[y][x])
			else:
				row.append(' ')

		matrix.append(" ".join(row))
		row=[]
	
	matrix = "\n".join(x for x in matrix)
	matrix+= "\n"
#	print(matrix)
	return matrix
	
	
#transposition("Hello, World !")