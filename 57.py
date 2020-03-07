import time

start_time = time.time()

count = 0

def plus_two(numerator,denominator):
	return ((2*denominator+numerator),denominator)


for i in range(1000):
	fraction = (2,1)
	for l in range(i):
		fraction = plus_two(fraction[1],fraction[0])
	fraction = ((fraction[1]+fraction[0]),fraction[0])
	if len(str(fraction[0]))>len(str(fraction[1])):
		count+=1

print ('Answer: ' +str(count) + '\t\t\t' +str(time.time()-start_time) +'s')

