upper_limit = 10000

def divisors(num):
	i = num -1
	div = [1]
	while i > 1:
		if num%i==0:
			div.append(i)
		i -=1
	return div

numbers = 	{'1': [[1], 1],
			'2': [[1], 1],
}		

sum_amicable = 0
for i in range(1,upper_limit):
	print i
	a = divisors(i)
	numbers[str(i)]= [a, sum(a)]

for i in range(1,upper_limit):
	sum_a = numbers[str(i)][1]
	if sum_a < upper_limit:
		if numbers[str(sum_a)][1] == i and i !=sum_a:
			text = 'The couple ' + str(i) + '/' + str(sum_a) + ' are amicable numbers'
			print text
			sum_amicable += i
print sum_amicable