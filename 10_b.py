import math
import time 
import csv

start_time = time.time()
max_prime =  2000000
prime_list = range(2,max_prime)
i = 0
while i < math.sqrt(max_prime):
	if i in prime_list:
		a_max = int(max_prime / i) -i +1
		a=0
		while a < a_max:
			j = i*i + a*i
			if j in prime_list:
				prime_list.remove(j)
			a+=1
	i+=1
	print i
runtime = time.time() - start_time
str1 = 'time required: (seconds) '+ str(runtime)
with open("primes.csv","wb") as csvfile:
    csv.writer(csvfile, delimiter=',', quotechar=';').writerow(prime_list)
print str1