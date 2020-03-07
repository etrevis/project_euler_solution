import time
import csv

start_time = time.time()

prime_list=[]
with open("prime_numbers.csv","r") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)

side_n = 2
corner = 1
ratio = 1
prime_in = []
corner_count = 1

while ratio > 0.15:
	for i in range(4):
		corner = corner +side_n
		corner_count += 1
		if corner in prime_list:
			prime_in.append(corner)
	ratio = len(prime_in)/corner_count
	if side_n % 27 == 0:
		print('Current ratio: {0:.4f} \t Side lenght: {1} \t Corner value: {2}'.format(ratio, (side_n+1), corner))
	side_n += 2

print ('Answer: {0} \t\t\t {1:.5f}s'.format((side_n -1),(time.time()-start_time)))

