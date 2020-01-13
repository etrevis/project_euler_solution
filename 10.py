import csv
import math

prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)
if len(prime_list) > 0:
    i = prime_list[len(prime_list) - 1]
else:
    prime_list = [2,3,5]
    i = 7
div_count = 0
writing = 0
while i <= 2000000:
    for prime in prime_list:
        if div_count == 0:
            partial = float(i) / prime
            if partial == int(partial):
                div_count += 1
            if partial < prime:
            	break
    if div_count == 0:
        prime_list.append(i)
        print 'prime number found!'
    if (i-writing) > 20000:
        with open("prime_numbers.csv","wb") as csvfile:
            csv.writer(csvfile, delimiter=',', quotechar=';').writerow(prime_list)
        writing = i
    div_count = 0        
    print i
    i += 2
with open("prime_numbers.csv","wb") as csvfile:
    csv.writer(csvfile, delimiter=',', quotechar=';').writerow(prime_list)
for prime in prime_list:
    if prime < 1415:
        i =prime*prime
        if i in prime_list:
            prime_list.remove(i)
            print i
            print 'false prime removed'
seen = set()
uniq = []
for x in prime_list:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
with open("prime_numbers.csv","wb") as csvfile:
    csv.writer(csvfile, delimiter=',', quotechar=';').writerow(prime_list)
fin_sum = sum(prime_list)+1
strng = 'The sum is: '+ str(fin_sum)
print strng