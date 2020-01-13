import time
start_time = time.time()
upper_limit=50

Lychrell_numbers = {}
begin_time = time.time()
for s in range(1,int(upper_perimeter_limits+1)):
	text = 'Working on number: ' + str(s)
	print (text)
	numbers['s']=[]
	for a in range(1,int(s/2)):
		for b in range(a,s):
			c = (s-a-b)
			if (a*a+b*b)==c*c:
				numbers['s'].append((a,b,c))
			else:
				pass
	if len(numbers['s'])>best_candidate[1]:
		best_candidate = [s,len(numbers['s'])]
		text = 'New candidate! Triads: ' + str(best_candidate[1]) + '\t' +str(numbers['s'])
		print(text)

text = 'Answer: ' + str(best_candidate[0]) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print (text)