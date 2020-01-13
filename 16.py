i = 1000
number = 2
while i != 1:
	number = number * 2
	i -= 1
string = str(number)
sum = 0
for digit in string:
	sum = sum + int(digit)
print sum