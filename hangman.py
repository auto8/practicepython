word = 'hello' 
l = []
for i in word:
	l.append(i)

class player:
	def __init__(self):
		self.guess_bank = 6
		self.word = []

def get_guess():
	guess = str(input('guess a char '))
	return guess 


def hmm(guess_char, word, player):
	if guess_char in l:
		for i in l:
			if guess_char == i:
				player.word.append(i)
		return True
	else:
		player.guess_bank -= 1 	

def display(wordbank, word):
	output = str()
	space = ' '
	for i in word:
		if i in wordbank:
			output += i 
		else:
			output += space
	return output 

def hangman(number):
	dictionary = {5: '  o', 4: '  o\n  |', 3: '  o\n -|', 2: '  o\n -|-', 1: '  o\n -|-\n /', 0: '  o\n -|-\n / \\'}
	return dictionary[number]

new = player()
while True:
	guess_char = get_guess()
	if hmm(guess_char, l, new) == True:
		print('\t\t\t' + display(new.word, word))
	else:
		print(hangman(new.guess_bank))
		print('\t\t\t' + display(new.word, word))
	
	if display(new.word, word) == word:
		print('u win')
		break
	elif new.guess_bank == 0:
		print('u lose')
		break
		
	
	

