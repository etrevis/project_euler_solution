import time
start_time = time.time()

upper_limit = 1000
answer = ''
total= 0
for i in range(1,upper_limit+1):
	total += i**i
char_list = []
for char in str(total):
	char_list.append(char)
for i in range(len(char_list)-10,len(char_list)):
	answer += char_list[i]
text = 'Answer: ' + answer + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text