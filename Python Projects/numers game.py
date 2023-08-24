import random

top_of_range = input('enter a number: ') 
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('enter a number larger than 0 next time')
        quit()
else: 
    print('pls enter a numer')
    quit()

r = random.randint(0 , top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess) 
        if user_guess == r: 
            print('you got it right')
            break
        else:
            print('you got it wrong')
    else:
        print('pls enter a number')
print('you got it in' , guesses , 'guesses' )