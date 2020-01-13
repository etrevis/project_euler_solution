import time
import itertools
start_time = time.time()

upper_limit = 100

def return_strings(a):
	abc = []
	for i in range(1,a+1):
		abc.append(str(i))
	return abc
			

def return_N_comb(n,r):
	counter = 0
	for comb in itertools.permutations(n,r):
		counter += 1
	return counter
	
begin_time = time.time()
asked_comb = []
for a in range(1,upper_limit+1):
	n = return_strings(a)
	for b in range(1,a+1):
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Working on numbers: ' + str(a) + ', '+str(b) + '\n'
			print text
		combinations = return_N_comb(n,b)
		if combinations>1000000:
			asked_comb.append([a,b,combinations])

answer = len(asked_comb)		

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text