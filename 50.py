import csv
import time
start_time = time.time()

upper_limit = 1000000
prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)

answer=0
begin_time = time.time()
lenght = 0
the_list = [1,2]
top_number = [41,6,0]
while answer==0 and len(prime_list)>lenght and top_number[0]<upper_limit:
	lenght +=1
	the_list.append(prime_list[lenght])
	reversed_list = sorted(the_list, reverse=1)
	for i in range(0,len(the_list)):
		if (time.time()-begin_time)>5:
			begin_time = time.time()
			text = 'Top number: ' + str(top_number[0])
			print text
		reversed_list.pop()
		total = sum(reversed_list)
		if total in prime_list and (len(reversed_list) - i)>top_number[1]:
			top_number[2] = top_number[0]
			top_number[1] = len(the_list) - i
			top_number[0] = total
		elif total < top_number[0]:
			break
answer = top_number[2]

        
text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text