import random
random_number = random.randint(1,10)
# print(random_number)
win = False
turns = 0
while win == False:
    # print('Enter a number between 1 - 10')
    your_guess = input('Enter a number between 1 - 10: ')
    turns +=1
    if random_number == int(your_guess):
        print('You win')
        win == True
        break
    elif turns == 5:
        print('You ran out of turns, the number was', random_number)
        break
    else :
        if int(your_guess) < random_number:
            print('Your guess is too low try higher')
        else:
            print('Your guess is too high try lower')
