import random

top_of_range = input('Enter a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Enter a number larger than 0 next time')
        quit()
else:
    print('Please enter a number')
    quit()

random_number = random.randint(0, top_of_range)
#print(random_number)445

while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print('You guessed correctly!')
            break
        else:
            print('Incorrect, try again')
    else:
        print('Please enter a number')
