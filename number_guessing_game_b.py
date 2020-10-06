import random
random_number = random.randint(1,10)
computer_guess = random.randint(1,10)
turns = 0

while random_number != computer_guess:
    turns += 1
    print(computer_guess)
    computer_guess = random.randint(1,10)
    if random_number == computer_guess:
        print('It took', turns, 'turns')
        break
