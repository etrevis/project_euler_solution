import csv
import time
import string
import sys
csv.field_size_limit(sys.maxsize)

start_time = time.time()

ranking = [
	1,	#High Card: Highest value card.
	2,	#One Pair: Two cards of the same value.
	3,	#Two Pairs: Two different pairs.
	4,	#Three of a Kind: Three cards of the same value.
	5,	#Straight: All cards are consecutive values.
	6,	#Flush: All cards of the same suit.
	7,	#Full House: Three of a kind and a pair.
	8,	#Four of a Kind: Four cards of the same value.
	9,	#Straight Flush: All cards are consecutive values of same suit.
	10	#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
]

def return_int(a):
	return int(a)


def split(hand):
	Numbers = []
	Suits = []
	for card in hand:
		if card[0] == 'A':
			Numbers.append(str(1))
		elif card[0] == 'K':
			Numbers.append(str(13))
		elif card[0] == 'Q':
			Numbers.append(str(12))
		elif card[0] == 'J':
			Numbers.append(str(11))
		elif card[0] == 'T':
			Numbers.append(str(10))
		else:			
			Numbers.append(card[0])
		Suits.append(card[1])
	return [Numbers,Suits]

def get_high_card(hand):
	abc = sorted(hand[0], key=return_int)
	if '1' in abc:
		return '14'
	else:
		return abc[4]

def get_pairs(hand):
	abc=[]
	for n in hand[0]:
		if hand[0].count(n)==2 and n not in abc:
			abc.append(n)
	if len(abc)>1:
		return '99'
	elif len(abc)==1:
		return abc[0]
	else:
		return 0
			
def is_three(hand):
	for n in hand[0]:
		if hand[0].count(n)==3:
			return n
	else:
		return 0

def is_poker(hand):
	for n in hand[0]:
		if hand[0].count(n)==4:
			return n
	else:
		return 0
		
def is_straight(hand):
	abc = sorted(hand[0], key=return_int)
	if '1' in abc and '13' in abc:
		abc.remove('1')
		abc.append('14')
	for n in range(4):
		if (int(abc[n])+1)==int(abc[n+1]):
			pass
		else:
			return 0
	else:
		return abc[4]

def is_flush(hand):
	a = hand[1][0]
	if hand[1].count(a) == 5:
		return get_high_card(hand)
	else:
		return 0
		
def is_full(hand):
	a = get_pairs(hand)
	if a=='99':
		b = int(is_three(hand))
		if b != 0:
			return str(b)
		else:
			return 0
	else:
		return 0

def is_str_flush(hand):
	a = int(is_flush(hand))
	b = int(is_straight(hand))
	if a != 0 and b != 0:
		return str(b)
	else:
		return 0

def get_best_hand(hand):
	if int(is_str_flush(hand)) !=0:
		if int(is_str_flush(hand)) ==14:
			return 10
		else:
			return 9
	elif int(is_poker(hand)) !=0:
		return 8
	elif int(is_full(hand)) !=0:
		return 7
	elif int(is_flush(hand)) !=0:
		return 6
	elif int(is_straight(hand))!=0:
		return 5
	elif int(is_three(hand))!=0:
		return 4
	elif get_pairs(hand)=='99':
		return 3
	elif int(get_pairs(hand))!=0:
		return 2
	else:
		return 1

hand_list={'1': [],
			}
answer = 0
with open("poker.csv","rb") as csvfile:
    reader= csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = 0
    for row in reader:
    	count+=1
        hand_list[str(count)] = row

for k,j in hand_list.items():
	hand_list[k]= [[ j[i] for i in range(0,5)],[j[i] for i in range(5,10)]]
	hand_list[k][0] = split(hand_list[k][0])
	hand_list[k][1] = split(hand_list[k][1])

for k in range(1,len(hand_list)+1):
	text = 'The hands in row ' +str(k)+' are: '
	temp = []
	for hand in hand_list[str(k)]:
		lalala = get_best_hand(hand)
		text += str(lalala) + ' '
		temp.append(lalala)	
	if temp[0]>temp[1]:
		text += '\t'+ 'Player 1 WIN!' 
		answer += 1
	elif temp[0]==temp[1]:
		if temp[0]==1:
			if int(get_high_card(hand_list[str(k)][0]))>int(get_high_card(hand_list[str(k)][1])):
				text += '\t'+ 'Player 1 WIN!'
				answer +=1
			else:
				continue
		elif temp[0]==2:
			if int(get_pairs(hand_list[str(k)][0]))>int(get_high_card(hand_list[str(k)][1])):
				text += '\t'+ 'Player 1 WIN!'
				answer +=1
			else:
				continue
		else:
			text += 'NON SO CHE FARE'
	print text
text = 'Answer: ' + str(answer) + '            ' + 'Time required: ' + str(((time.time() -start_time))) + ' s'
print text