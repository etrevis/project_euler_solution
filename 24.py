import time
import itertools

start_time= time.time()


abc= []
permutations = itertools.permutations(range(10))
for i in permutations:
	abc.append(i)
text = 'Answer: ' + str(abc[999999]) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text