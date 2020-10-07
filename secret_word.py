import random

with open ('/usr/share/dict/words') as infile:
    infile = infile.read().split()
    word = random.choice(infile).lower()
# print(word)

guessed_letters = []
wrong_guesses = []
attempts = 10

while attempts > 0:
    full_word = ''
    for letter in word:
        if letter in guessed_letters:
            full_word = full_word + letter
        else:
            full_word = full_word + '_ '
    if full_word == word:
        print('You guessed the word!', word)
        break
    guess = input('Let\'s play some HangMan! \n Enter a letter: ').lower()

    print(full_word)

    if guess in guessed_letters or guess in wrong_guesses: #checks to see if the letter has already been guessed
        print('You already guessed that letter: ', guess)

    if guess in word:
        guessed_letters.append(guess)
    elif not guess in word:
        wrong_guesses.append(guess)
        attempts -= 1
    if attempts == 0:
        print('You ran out of attempts! The word was:', word)
        break
    if len(guess) > 1: #checks to see if user is only inputting 1 letter
        print('Enter only 1 letter')
    elif not guess.isalpha(): #makes sure the user is not inputting anything other than a letter
        print('Enter a letter only')
