import random

with open ('/usr/share/dict/words') as infile:
    infile = infile.read().split()
    word = random.choice(infile).lower()
# print(word)

full_word = '_ ' * len(word)
guessed_letters = []
attempts = 10
print('Guess the word!')
print(full_word, '\n')

while attempts > 0:

    guess = input('Enter a letter: ').lower()
    # guessed_letters.append(guess)
    # print(guessed_letters)
    if len(guess) > 1: #checks to see if user is only inputting 1 letter
        print('Enter only 1 letter')
    elif not guess.isalpha(): #makes sure the user is not inputting anything other than a letter
        print('Enter a letter only')
    elif guess in guessed_letters: #makes sure the same letter is not used twice
        print('Letter has already been used')
    for letter in word:
