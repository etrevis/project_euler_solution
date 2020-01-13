today = {
	'day': 1,
	'month': 1,
	'year': 1900,
	'day_name': 2,
	'count': 0,
}

months = {
	'1': 31,
	'2': 28,
	'3': 31,
	'4': 30,
	'5': 31,
	'6': 30,
	'7': 31,
	'8': 31,
	'9': 30,
	'10': 31,
	'11': 30,
	'12': 31,
}

def isleap(today):
	if today['year'] % 4 == 0 and today['year'] % 100 != 0:
		return 1
	elif today['year'] % 400 == 0:
		return 1
	else:
		return 0

def weekday(num):
	if num < 7:
		num +=1
	else:
		num = 1
	return num

def nextday(today):
	if today['day'] < months[str(today['month'])]:
		if today['day']==1 and today['day_name']==1:
			today['count'] +=1
		today['day'] += 1
		today['day_name'] = weekday(today['day_name'])
	else:
		today['day'] = 1
		today['day_name'] = weekday(today['day_name'])
		if isleap(today) and today['month']==2:
			leap_day = '29/2/'+ str(today['year'])+' happy leap year!'
			print leap_day
			today['day_name'] = weekday(today['day_name'])
		if today['month'] <12:
			today['month'] += 1
		else:
			today['month'] = 1
			today['year'] +=1
	return today

def end_date(today):
	if today['day'] == 1 and today['month'] == 1 and today['year'] == 2001:
		return 0
	else:
		return 1	

while end_date(today):
	today = nextday(today)
print (today['count'])
		
			
	
