import random
user_win = 0
bot_win = 0
options = ['r' , 'p' , 's']
while True:
    user_input = input('enter R\P\S   or  enter Q for quit: ').lower()
    if user_input == "q" :
        break
    
    if user_input not in options:
        print('it not an option')
        continue
    r = random.randint(0 , 2)
    bot_pick = options[r]
     
    print('computer picked', bot_pick)
    if user_input == bot_pick:
        print('draw')
        continue
     
    if user_input == "r" and bot_pick == "s" :
        print('you won! ')
        user_win += 1
    elif user_input == "p" and bot_pick == "r" :
        print('you won! ')
        user_win += 1
    elif user_input == "s" and bot_pick == "p" :
        print('you won! ')
        user_win += 1    
    else: 
        print('computer won!')
        bot_win += 1 
print('you won' , user_win , "times.")    
print('computer won' , bot_win , " times.")       
print('bye')
    