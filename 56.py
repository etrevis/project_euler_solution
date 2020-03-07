import time

start_time = time.time()
biggest = 1

for a in range(100):
	for b in range(100):
		num = str(a**b)
		n_sum = 0
		for i in num:
			n_sum+=int(i)
		if n_sum > biggest:
			biggest = n_sum


print ('Answer: ' +str(biggest) + '\t\t\t' +str(time.time()-start_time) +'s')

