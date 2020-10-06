import random

with open ('/usr/share/dict/words') as infile:
    infile = infile.read().split()
    word = random.choice(infile).lower()
# print(word)


full_word = '_ ' * len(word)
guessed_letters = []
attempts = 10
print('Guess the word!')
print(full_word)
print('\n')

while attempts > 0:
    guess = input('Enter a letter: ')
    if len(guess) > 1:
        print('Enter only 1 letter')
        continue
    elif not guess.isalpha():
        print('Enter a letter only')
        continue
    elif guess in guessed_letters:
        print('Letter has already been used')
        continue
    
