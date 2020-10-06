import random
user_num = int(input('Enter a number between 1 - 10: '))
computer_guess = random.randint(1,10)
turns = 0

while user_num != computer_guess:
    turns += 1
    print(computer_guess)
    computer_guess = random.randint(1,10)
    if user_num == computer_guess:
        print('It took', turns, 'turns')
        break
