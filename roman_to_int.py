def roman_to_int(string):
	roman_int = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	nr = 0
	for x in range(len(string)):
		if x == len(string)-1:
			nr += roman_int[string[x]]
		else:
			if roman_int[string[x]]>=roman_int[string[x+1]]:
				nr += roman_int[string[x]]
			else:
				nr -= roman_int[string[x]]
	return nr


#roman_to_int("MMMCDXCIX")	
