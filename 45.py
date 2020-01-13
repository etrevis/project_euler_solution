import time
start_time = time.time()

lower_limit = 144
upper_limit = 300
answer = 0
pentagon_numbers = []
triangular_numbers = []
hexagonal_numbers = []
begin_time = time.time()
while answer==0:
	for n in range(lower_limit,upper_limit):
			pentagon_numbers.append(n*(3*n-1)/2)
	for n in range(lower_limit,upper_limit):
			triangular_numbers.append(n*(n+1)/2)
	for n in range(lower_limit,upper_limit):
			hexagonal_numbers.append(n*(2*n-1))
	for hexa in hexagonal_numbers:
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Working on numbers: ' + str(upper_limit) + ', ' + str(lower_limit)
			print text
		if hexa in pentagon_numbers and hexa in triangular_numbers:
			answer = hexa
			break
	lower_limit=upper_limit
	upper_limit=upper_limit*2

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text