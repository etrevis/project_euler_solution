import csv
import time

start_time = time.time()

is_prime = True

prime_list=[]

def save_file_time(time1):
	if (time.time()-time1)>60:
		return True
	else:
		return False

def save_file():
	with open("prime_numbers.csv","w") as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar=';')
		writer.writerow(prime_list)

def read_file():
	with open("prime_numbers.csv","r") as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar=';')
		for row in reader:
			n_list = [int(x) for x in row]
			prime_list.extend(n_list)


read_file()
current_number = prime_list[(len(prime_list)-1)]

prev_list_lenght = len(prime_list)

print ('Starting from: {}'.format(current_number))

while True:
	current_number +=2
	is_prime = True
	for prime in prime_list:
		if current_number%prime == 0:
			is_prime = False
			break
	if is_prime == True:
		prime_list.append(current_number)
		if save_file_time(start_time):
			start_time = time.time()
			save_file()
			print('File updated with {} new primes. Last saved one: {}'.format((len(prime_list) -prev_list_lenght ),prime_list[(len(prime_list)-1)]))
			prev_list_lenght = len(prime_list)

