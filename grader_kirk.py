def evaluator(students, grades):
	if len(students)>30 or len(grades)>30 or len(students)!=len(grades) or len(students)==0 or len(grades)==0: 
		return None
	else:
		count=0
		summ=0
		summ_stud=0
		student_av={} #dictionary student average grade
		for i in range(len(grades)):
			if len(grades[i])<4 or len(grades[i])>50:
				return None
			else:
				for j in range(len(grades[i])):
					if grades[i][j]<0 or grades[i][j]>20:
						return None
					else:
						count+=1 #number of grades, total
						summ+=grades[i][j] #sum of grades, total
						summ_stud+=grades[i][j] #sum of grades per student
					student_av[students[i]]=round(summ_stud/len(grades[i]),2)
				summ_stud=0
			avg=round(summ/count,2)
		tup=(avg, student_av)	
		#print (tup)
		return tup

#students=["Mari","Aleksander","Eva"]
#grades=[[3,4,5],[10,11,20],[20,20,20]]
#evaluator(students, grades)