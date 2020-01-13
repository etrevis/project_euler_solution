import time
start_time = time.time()
import csv
import math

prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)

def quad_num(a,b,n):
	return (n*n+a*n+b)

def is_prime(n,prime_list):
	if n in prime_list:
		return 1
	else:
		return 0
		
upper_limit = 100
beg_time = time.time()
best_pair = [0,0,1]
for a in range(-1000,1000):
	for b in range(-1001,1001):
		if b> -best_pair[2]*(best_pair[2]+a): #conditions to have a positive number, this speeds up things
			if (time.time()-beg_time)>10:
				print 'The best pair now is:'
				print best_pair
				text = 'Current couple is : a='+str(a)+' and b='+str(b) + '\n'
				print text
				beg_time = time.time()
			counter = 0
			for i in range(0,upper_limit): #maybe it can be stoped at 80 but who knows
				if is_prime(quad_num(a,b,i),prime_list):
					counter +=1
				else:
					break
			if counter > best_pair[2]:
				best_pair[2] = counter
				best_pair[1] = b
				best_pair[0] = a

text = 'Answer: ' + str(best_pair[0]*best_pair[1])+ '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text