import time
import math 
start_time = time.time()

upper_limit = 100

begin_time = time.time()
asked_comb = []
for a in range(1,upper_limit+1):
	for b in range(1,a+1):
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Working on numbers: ' + str(a) + ', '+str(b) + '\n'
			print text
		combinations = (math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))
		if combinations>1000000:
			asked_comb.append([a,b,combinations])

answer = len(asked_comb)		

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text