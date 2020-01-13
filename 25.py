import time
start_time = time.time()

fib_numbers = [1,1]
status = 1
while status:
	num = fib_numbers[len(fib_numbers)-1] + fib_numbers[len(fib_numbers)-2]
	fib_numbers.append(num)
	if len(str(num))==1000:
		status = 0

text = 'Answer: ' + str(len(fib_numbers)) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text