from collections import Counter
import re
def coolest_word(words):
	words=list(words) 
	maxNr=0 # max different chars in 1 word
	counts=0 # temporal variable to diff chars in word
	coolest=''
	regex = re.compile('[^a-zA-Z]')
	for x in range(len(words)):
		#charmax = max(words[x], key=words[x].count)
		words[x]=regex.sub('',words[x])	
		letterCountList = Counter(words[x]).most_common(len(words[x]))
		counts=len(letterCountList)
			
		if counts>maxNr:
			maxNr=counts
			coolest=words[x]

	if len(words)==0 or coolest=='':
		return None
	else:
		#print(coolest)
		return coolest

#coolest_word(['expectation', 'discomfort', 'half', 'decomposi tion', 'decomposition'])