import time
import itertools
start_time = time.time()

upper_limit = 100000000
count = 0

def is_power(number, power):
	if number > 500000:
		for i in range(8,10):
			if abs(i**power - number)==0:
				print ('base ' +str(i))
				print('power '+ str(power))
				return 1
	else:
		for i in range(10):
			if abs(i**power - number)==0:
				print ('base ' +str(i))
				print('power '+ str(power))
				return 1

for i in range(upper_limit+1):
	if is_power(i, len(str(i))):
		print (str(i)+'\n')
		count +=1




text = 'Answer: ' + str(count) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print (text)















