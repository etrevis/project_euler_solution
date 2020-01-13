import time
import itertools
start_time = time.time()

def return_tuple(a):
	
	return abc

begin_time = time.time()
answer = 0
i = 0
while answer ==0:
	count=0
	i +=1
	multiple_list = []
	if (time.time()-begin_time)>5:
		begin_time = time.time()
		text = 'Working on number: ' + str(i) + '\n'
		print text
	for a in range(6,0,-1):
		if len(str(i*a)) == len(str(i)):
			multiple_list.append(tuple( x for x in str(i*a)))
		else:
			break
	if len(multiple_list) == 6:
		for multiple in multiple_list:
			if multiple in itertools.permutations(str(i)):
				count+=1
			else:
				break
	if count>=6:
		answer = i

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text