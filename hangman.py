import random
import sys

def get_word():
	with open('words.txt', 'r') as f:
		value = f.readlines()
	word = random.choice(value)
	return word.lower().strip()

class player:
	def __init__(self):
		self.guess_bank = 6
		self.word = []

def get_guess():
	guess = str(input('guess a char '))
	return guess 


def hmm(guess_char, word, player):
	if guess_char in word:
		for i in word:
			if guess_char == i:
				player.word.append(i)
		return True
	else:
		player.guess_bank -= 1 	

def display(wordbank, word):
	output = str()
	space = '_'
	for i in word:
		if i in wordbank:
			output += i 
		else:
			output += space
	return output 

def hangman(number):
	dictionary = {5: '  o', 4: '  o\n  |', 3: '  o\n -|', 2: '  o\n -|-', 1: '  o\n -|-\n /', 0: '  o\n -|-\n / \\'}
	return dictionary[number]

def play_or_quit():
	ask = int(input('enter 1 to play again 0 to abort '))
	if ask == 1:
		main()
		new = player()
	else:
		sys.exit()

def main():
	new = player()
	word = get_word()
	while True:
		guess_char = get_guess()
		
		if hmm(guess_char, word, new) == True:
			print(hangman(new.guess_bank))
			print('\t\t\t' + display(new.word, word))
		else:
			print(hangman(new.guess_bank))
			print('\t\t\t' + display(new.word, word))
	
		if display(new.word, word) == word:
			print('u win')
			play_or_quit()

		elif new.guess_bank == 0:
			print('u lose')
			play_or_quit()

main()
