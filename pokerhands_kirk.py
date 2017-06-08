from collections import Counter
import itertools
def pokervalue(cards):
	l_v=[]
	l_s=[]
	s_v=[]
	max_s=''
	for x in range(len(cards)):
		l_v.append(cards[x]['value'])
		l_s.append(cards[x]['suit'])
		s_v.append([(cards[x]['suit']),(cards[x]['value'])])
	c_v=Counter(l_v) 
	c_s=Counter(l_s)
	lv_s=list(set(sorted(l_v)))
	s_v.sort()
	st_count=0
	stf_count=0
	if 5 in c_s.values() or 6 in c_s.values() or 7 in c_s.values():
		max_s = max(c_s, key=c_s.get)
		for x in range(len(s_v)-1):
			if s_v[x][0]==max_s and s_v[x][1]+1==s_v[x+1][1]:
				stf_count+=1
		if [max_s,1] in s_v and [max_s,13] in s_v and [max_s,2] not in s_v:
				stf_count+=1
	else:
		for x in range(len(lv_s)-1):
			if lv_s[x]+1==lv_s[x+1]:
				st_count+=1
			if lv_s[0]==1 and lv_s[-1]==13 and lv_s[1]!=2:
				st_count+=1
	if stf_count>=4:
		return('straight flush')
	elif 4 in c_v.values():
		return('four of a kind')
	elif 3 in c_v.values() and 2 in c_v.values():
		return('full house')
	elif max_s != '':
		return('flush')
	elif st_count>=4:
		return('straight')
	elif 3 in c_v.values():
		return('three of a kind')
	elif (2,2) in ([(k, len(list(v))) for k, v in itertools.groupby(sorted(c_v.values()))]):
		return('two pair')
	elif 2 in c_v.values():
		return('one pair')
	else:
		return('high card')
