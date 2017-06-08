import time
from datetime import date
def get_age(birth_date, current_date=None):
	if current_date:
		return current_date.year-birth_date.year-((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
	else: 
		today = date.today()
		return today.year-birth_date.year-((today.month, today.day) < (birth_date.month, birth_date.day))
	
#print(get_age(date(1989,1,27), date(2016, 1, 26)))
