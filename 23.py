import time

upper_limit = 28123

def divisors(num):
	i = num -1
	div = [1]
	while i > 1:
		if num%i==0:
			div.append(i)
		i -=1
	return div

numbers = 	{'abb': [],
			'def': [],
			'perfect': [],
}		
start_time =  time.time()
begin = time.time()
print 'Looking for divisors and sorting numbers'
for i in range(1,upper_limit):
	if (time.time()-begin)> 8:
		begin = time.time()
		abc =[len(numbers['def']), len(numbers['perfect']), len(numbers['abb'])]
		text = 'Found '+ str(abc[0]) +' deficient numbers, ' + str(abc[1]) +' perfect numbers and ' + str(abc[2]) +' abbundat numbers'
		print text
	if i>sum(divisors(i)):
		numbers['def'].append(i)
	elif i==sum(divisors(i)):
		numbers['perfect'].append(i)
	elif i<sum(divisors(i)):
		numbers['abb'].append(i)

print 'Testing numbers'
num_list = []
check = 1
for i in range (1,upper_limit):
	check = 1
	for num in numbers['abb']:
		if check and num< i:
			partial = i - num
			if partial in numbers['abb']:
				text = 'the number ' + str(i) + ' can be written as ' +str(partial)+ ' + ' + str(num)
				check = 0
				print text	
	if check:
		num_list.append(i)

text = 'The final sum is ' + str(sum(num_list)) + '     ' + 'Time required: ' + str(((time.time() -start_time))) + ' s' 
print text