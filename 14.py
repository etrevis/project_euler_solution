answer = 0
i = 13
longest_chain = 0
status = True

def do_step(number):
    if number % 2 == 0:
        return number / 2
    else:
        return (3 * number) + 1

while 1000000 > i:
    chain_length = 0
    new_number = do_step(i)
    while new_number != 1:
        new_number = do_step(new_number)
        chain_length += 1
    if longest_chain < chain_length:
        longest_chain = chain_length
        answer = i
    print i
    i += 1

print ('The answer to problem 14 is: ' + str(answer))
