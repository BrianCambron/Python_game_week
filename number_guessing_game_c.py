min = 0
max = 100
turns = 0
user_num = int(input('Enter a number between 1 - 100: '))
computer_guess = (min + max)// 2

while user_num != computer_guess:
    turns += 1
    computer_guess = (min + max)// 2
    print(computer_guess)

    if computer_guess > user_num:
        max = computer_guess

    elif computer_guess < user_num:
        min = computer_guess + 1

print('The computer guessed in', turns, 'tries.')
