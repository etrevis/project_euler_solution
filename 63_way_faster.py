import time
import itertools
start_time = time.time()

upper_limit = 50
count = 0


for a in range(1,15):
	for b in range(upper_limit):
		c = a**b
		if len(str(c)) == b:
				print ('base ' +str(a))
				print ('power '+ str(b))
				print ('number ' + str(c)+ '\n')
				count +=1


text = 'Answer: ' + str(count) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print (text)















