import csv
import time
import math
start_time = time.time()

upper_limit= 1000000
prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)
answer = 0 
begin_time = time.time()
for i in range(9,upper_limit,2):
	if not i in prime_list:
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Working on number: ' + str(i)
			print text
		status =1
		for prime in prime_list:
			if i > prime and status:
				partial = math.sqrt((i-prime)/2)
				if partial == int(partial):
					status=0
					break
		if status:
			answer = i
			break
		

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text