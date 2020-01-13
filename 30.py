import time
start_time = time.time()
upper_limit=1000000

numbers = []
begin_time = time.time()
for i in range(2,(upper_limit+1)):
	if (time.time()-begin_time)>5:
		begin_time = time.time()
		text = 'Working on number: ' + str(i)
		print text
	total = 0
	for char in str(i):
		total += int(char)**5
	if total == i:
		numbers.append(i)

text = 'Answer: ' + str(sum(numbers)) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text