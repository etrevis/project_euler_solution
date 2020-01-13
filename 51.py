import csv
import time
import itertools
import string
start_time = time.time()

prime_list=[]
with open("prime_numbers.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [int(x) for x in row]
        prime_list.extend(n_list)

combinations = []
def generate_masks(prime_l):
	masks = []
	for lenght in range(1,prime_l+1):
		for ones in range(0,lenght-1):
			abc = ''
			for i in range(0,ones):
				abc += '1'
			for i in range(ones,lenght):
				abc+='0'
			for a in itertools.permutations(abc,lenght):
				num = []
				for b in a:
					num.append(b)
				if len(num) == lenght and not num in masks and '1' in num:
					masks.append(num)
	return masks

def append_list(a_list,b_dic):
	ind = str(len(a_list))
	try:
		b_dic[ind].append(a_list)
	except KeyError:
		b_dic[ind] = [a_list]


clever_dic = {'1':[],
				'2':[],
				}

for prime in prime_list:
	prime_list = [int(x) for x in str(prime)]
	append_list(prime_list,clever_dic)

def gen_next_num(prime_in,comb,a):
	partial = []
	for i in range(0,len(prime_in)):
		if int(comb[i])==1:
			partial.append(prime_in[i])
	if len(partial)!=partial.count(partial[0]):
		return prime
	partial = []
	for i in range(0,len(prime_in)):
		if int(comb[i])==1 and prime[i]<a and (a or not i):
			partial.append(a)
		else:
			partial.append(prime_in[i])
	return partial

answer = []
keep_it = []
begin_time = time.time()
for l in range(4,7):
	combinations = generate_masks(l)
	for prime in clever_dic[str(l)]:
		for comb in combinations:
			if (time.time()-begin_time)>5:
				begin_time = time.time()
				print 'Working on prime: '
				print prime
				print '\n'
			if len(comb) == len(prime):
				count = 1
				for it in range(0,10):
					test = gen_next_num(prime,comb,it)
					if test in clever_dic[str(l)] and test!=prime:
						count +=1
					if not count >= (-1+it):
						break
				if count>=8:
					keep_it = comb
					answer = prime
			if len(answer)>0:
				break
		if len(answer)>0:
			break
	if len(answer)>0:
		break
print keep_it
abc=''
for a in answer:
	abc += str(a)
answer = int(abc)

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text