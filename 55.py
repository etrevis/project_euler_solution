import time
start_time = time.time()

upper_limit = 10000
max_cycles = 50 
count = 0
Lychrell_numbers = {}
begin_time = time.time()

def is_palindrome(number):
	str_number = str(number)
	len_str = len(str_number)
	first_half = str_number[:int(len_str/2)]
	if len_str%2:
		second_half = str_number[int(len_str/2 + 1):]
	else:
		second_half = str_number[int(len_str/2):]
	second_half = second_half[::-1]
	if first_half == second_half:
		return 1
	else:
		return 0

def next_palindrome_attemp(current_in):
	str_pal = str(current_in)
	nmb = int(str_pal[::-1])
	return (current_in+nmb)


for number in range(1,(upper_limit+1)):
	i = 0
	nmr_in = next_palindrome_attemp(number)
	if not nmr_in in Lychrell_numbers:
		while i < max_cycles:
			if is_palindrome(nmr_in):
				Lychrell_numbers['number'] = i
				break
			else:
				nmr_in = next_palindrome_attemp(nmr_in)
			i = i+1
			if i==50:
				count = count +1


text = 'Answer: ' + str(count) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print (text)