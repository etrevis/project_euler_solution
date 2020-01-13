import time
start_time = time.time()

lower_limit = 1
upper_limit = 1000
pentagon_numbers = []
listed = []
answer = 0
begin_time = time.time()
while answer==0:
	for n in range(lower_limit,upper_limit):
		pentagon_numbers.append(n*(3*n-1)/2)
	for a in sorted(pentagon_numbers, reverse=1):
		if a> (lower_limit*(3*lower_limit-1)/2):
			for b in pentagon_numbers:
				if (time.time()-begin_time)>5:
					begin_time = time.time()
					text = 'Working on numbers: ' + str(a) + ', ' + str(b)
					print text
				if b<a:
					c = (a-b)
					if c in pentagon_numbers:
						listed.append([a,b,c])
	for pair in sorted(listed, key=lambda couple: couple[2]):
		if (pair[0]+pair[1]) in pentagon_numbers:
			answer = pair[2]
			break
	lower_limit=upper_limit
	upper_limit=upper_limit*2

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text