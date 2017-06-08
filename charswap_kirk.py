def charswap(s):
	s = str(s)
	l=list(s)
	if len(l) < 2:
		return "".join(l)
	else:
		first = l[0]
		last = l[-1]
		l[0]=last
		l[-1]=first
		return "".join(l)

print(charswap(34))
