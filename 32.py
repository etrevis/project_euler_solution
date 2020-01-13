import time
start_time = time.time()
upper_limit=10000

combinations = []
products = []
begin_time = time.time()
for a in range(1,(upper_limit/2)):
	for b in range(1,upper_limit):
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Working on numbers: ' + str(a)+', '+str(b)
			print text
		prod = a*b
		string = str(a)+str(b)+str(prod)
		lenght = len(string)
		if lenght==9:
			list_char = range(1, (lenght+1))
			for char in string:
				if int(char) in list_char:
					list_char.remove(int(char))
				else:
					break
			if len(list_char)==0 and not prod in products:
				combinations.append([a,b,prod])
				products.append(prod)				
answer = 0
for abc in combinations:
	print abc
	answer += abc[2]

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text