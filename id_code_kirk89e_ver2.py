import calendar
def is_person_code_valid(string):
	if len(string) != 11:
		#print("Length should be 11 digits")
		return False
	#elif " " in string: #check whitespaces
		#return False
	elif not string.isdigit(): #check digit
		#print("not digits")
		return False
	else:
	#string.replace(" ", "")
		if int(string[0]) in [1,2]:
			century = "18"
		elif int(string[0]) in [3,4]:
			century = "19"
		else:
			century = "20"

		yy = century + string[1:3]
		mm = string[3:5] # month substring
		dd = string[5:7] # day substring
		c_string = int(string[-1]) #last nr in id code
		c_calc = (int(string[0])*1+int(string[1])*2+int(string[2])*3+int(string[3])*4+int(string[4])*5+int(string[5])*6+int(string[6])*7+int(string[7])*8+int(string[8])*9+int(string[9])*1)%11 
		if c_calc == 10: #second grade calc
			c_calc = (int(string[0])*3+int(string[1])*4+int(string[2])*5+int(string[3])*6+int(string[4])*7+int(string[5])*8+int(string[6])*9+int(string[7])*1+int(string[8])*2+int(string[9])*3)%11 
			if c_calc == 10:
				c_calc = 0

	#now it's sure that string is 11 digits!

	if int(string[0]) not in [1,2,3,4,5,6]: #check 1st nr
		#print("1st number is not correct.")
		return False
	elif int(mm)>12 or int(mm)<1: #check month
		#print("Month is not correct!")
		return False
	elif calendar.monthrange(int(yy),int(mm))[1] < int(dd) or int(dd) < 1: #check day
		#print("Day is not correct!")
		return False
	elif c_calc != c_string: #checksum
		#print("Id code's last number is not correct.")
		return False
	else:
		#print("Yout id code seems to be correct!")
		return True
