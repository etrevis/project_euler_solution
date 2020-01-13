import time
import csv

alphabet = {
	'A':	1,
	'B':	2,
	'C':	3,
	'D':	4,
	'E':	5,
	'F':	6,
	'G':	7,
	'H':	8,
	'I':	9,
	'J':	10,
	'K':	11,
	'L':	12,
	'M':	13,
	'N':	14,
	'O':	15,
	'P':	16,
	'Q':	17,
	'R':	18,
	'S':	19,
	'T':	20,
	'U':	21,
	'V':	22,
	'W':	23,
	'X':	24,
	'Y':	25,
	'Z':	26,
}

start_time = time.time()
words=[]
with open("p042_words.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        n_list = [str(x).strip('"') for x in row]
        words.extend(n_list)

triangle_numbers = []
for n in range(1,10000):
	triangle_numbers.append(n*(n+1)/2)
	
answer=0
for word in words:
	total = 0
	for char in word:
		total += alphabet[char]
	if total in triangle_numbers:
		answer +=1

text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text