import time
import itertools

start_time = time.time()

answer = 0

dict_candidates = {	'3': [],
					'4': [],
					'5': [],
					'6': [],
					'7': [],
					'8': []}

cyclic_cand = []

the_list = [i for i in range(1,7)]

def gen_f(n, nth):
	if nth==3:
		return int((n*(n+1))/2)
	if nth ==4:
		return int(n*n)
	if nth ==5:
		return int((n*(3*n-1))/2)
	if nth ==6:
		return int(n*(2*n-1))
	if nth ==7:
		return int((n*(5*n-3))/2)
	if nth ==8:
		return int(n*(3*n-2))

def check_cyc(n_1, n_2):
	n2_start =  str(n_2)[:2]
	n1_end = str(n_1)[2:]
	if n1_end == n2_start:
		return 1
	else:
		return 0

def get_list(grade, dict):
	return (dict_candidates[str((grade+2))])

def look_for_cyc(order_list):
	for numb in get_list(order_list[0], dict_candidates):
		for numb2 in get_list(order_list[1], dict_candidates):
			if check_cyc(numb, numb2):
				for numb3 in get_list(order_list[2], dict_candidates):
					if check_cyc(numb2, numb3):
						for numb4 in get_list(order_list[3], dict_candidates):
							if check_cyc(numb3,numb4):
								for numb5 in get_list(order_list[4], dict_candidates):
									if check_cyc(numb4, numb5):
										for numb6 in get_list(order_list[5], dict_candidates):
											if check_cyc(numb5, numb6) and check_cyc(numb6,numb):
												print (str( numb) + '-'+str(numb2)+ '-' + str(numb3)+'-' + str(numb4)+'-' + str(numb5)+'-' + str(numb6))
												cyclic_cand.append([numb,numb2,numb3,numb4,numb5,numb6])
												return 1

for a in range(3,9):
	i = 0
	x_numb = 0
	while x_numb <10000:
		x_numb = gen_f(i,a)
		i += 1
		if x_numb > 999:
			dict_candidates[str(a)].append(x_numb)

for new_list in itertools.permutations(the_list):
	if look_for_cyc(new_list):
		for i in cyclic_cand[0]:
			answer += int(i)
		break

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print (text)















