import time
start_time = time.time()
upper_limit=1001

total = 1
number = 1
for i in range(3,(upper_limit+1),2):
	for a in range(0,4):
		number = (number+(i-1))
		total += number
	text = 'Square side lenght: ' + str(i)
	print text

text = 'Answer: ' + str(total) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text