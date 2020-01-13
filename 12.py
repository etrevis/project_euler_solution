import pickle

file = open("prime_numbers.txt","r")
prime_list = pickle.load(file)
i = 1
div_number = 1
while 500 > div_number: # the script will stop at 500
    prime_factor_dict = {x:0 for x in prime_list}
    div_number = 1
    sum = (i*(i+1))/2
    partial_cache = sum
    while partial_cache > 1:
        for prime in prime_list:
            if not prime == 1 and partial_cache % prime == 0:
                prime_factor_dict[prime] = prime_factor_dict[prime] + 1
                partial_cache = partial_cache / prime
    for exp in prime_factor_dict.values():
        if not exp == 0:
            div_number = div_number * (exp + 1)
    print 'Number of current divisor: ' + str(div_number) + '\n' + 'Triangle number: ' + str(sum) + '\nSum order: ' + str(i) + '\n'
    sum = 0
    i += 1
