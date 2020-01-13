import time
start_time = time.time()
upper_limit=1000000

numbers = []
begin_time = time.time()
for i in range(3,(upper_limit+1)):
	if (time.time()-begin_time)>5:
		begin_time = time.time()
		text = 'Working on number: ' + str(i)
		print text
	total = 0
	for char in str(i):
		partial = 1
		for a in range(2,(int(char)+1)):
			partial = a*partial
		total += partial
	if total == i:
		numbers.append(i)

text = 'Answer: ' + str(sum(numbers)) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text