def capitalizing_this(input_string):
	st=str(input_string)
	lst = [word[0].upper() + word[1:].lower() for word in st.split()]
	s = " ".join(lst)
#	print(s)
	return s

#capitalizing_this("HellO WOrld")