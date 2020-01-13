import csv
import time
start_time = time.time()

upper_limit= 1000000
prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)

def cyclic_permutation(num):
	char_list = []
	for cha in str(num):
		char_list.append(cha)
	a = char_list[0]
	for i in range(0,len(char_list)-1):
		char_list[i] = char_list[i+1]
	char_list[len(char_list)-1]=a
	text = ''
	for char in char_list:
		text = text + char
	return int(text)

begin_time = time.time()
circular_prime_list = []
for i in prime_list:
	if (time.time()-begin_time)>5:
		begin_time = time.time()
		text = 'Working on number: ' + str(i) + '\n' + 'Number of circular primes found: ' + str(len(circular_prime_list))
		print text
	perm_list = [i]
	for a in range(0,len(str(i))-1):
		perm_list.append(cyclic_permutation(perm_list[a]))
	status1 = 1
	for num in perm_list:
		if not (num in prime_list) and status1 or len(str(i))!=len(str(num)):
			status1 = 0
			break
	if status1:
		status = 1
		for permutations in circular_prime_list:
			if not (i in permutations) and status:
				continue
			else:
				status = 0
				break
		if status:
			circular_prime_list.append(perm_list)
	if i>upper_limit:
		break

final_list = []
for lists in circular_prime_list:
	for num in lists:
		if not num in final_list:
			final_list.append(num)
print final_list

text = 'Answer: ' + str(len(final_list)) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text