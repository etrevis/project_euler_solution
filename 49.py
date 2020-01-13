import csv
import time
import itertools
start_time = time.time()

prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)

answer = []
begin_time = time.time()
while len(answer) == 0:
	for prime in prime_list:
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Working on prime: ' + str(prime)
			print (text)
		permutations = []
		if len(str(prime))==4 and prime not in [1487,4817,8147]:
			permutations = [prime]
			for perm in itertools.permutations(str(prime)):
				num  = ''
				for char in perm:
					num+=char
				num = int(num)
				if len(str(num))==4 and num!=prime and num in prime_list and not num in permutations:
					permutations.append(int(num))
		if len(permutations)>=3:
			permutations.sort()
			for a in permutations:
				c = a- prime
				if (a+c) in permutations and (a+c)!=prime:
					answer = [prime,a,(a+c)]
					break
		if len(answer)!=0:
			break
						
magic = str(answer[0])+str(answer[1])+str(answer[2])
text = 'Answer: ' + str(magic) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print (text)