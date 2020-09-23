from bottle import HTTPError

def year_validation(year):
	
	int_year=int(year)
	if int_year<999 or int_year>2020 or int_year == None:
		raise Exception("Значение для года принимается в диапазоне от 1000 до 2020")
	return True
