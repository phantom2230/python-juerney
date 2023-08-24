print('welcom to my general knowledge game')
playing = input('do you wanna play? ')
if playing.lower() != "yes" :
    quit()
print('ok lets play :)')
score = 0
answer = input('what is CPU stands for? ')
if answer == 'cpu' :
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input('what is GPU stands for? ')
if answer == 'gpu' :
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input('what is PSU stands for? ')
if answer == 'psu' :
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input('what is RAM stands for? ')
if answer == 'ram' :
    print('correct!')
    score += 1
else:
    print('wrong!')

print('you got ' + str(score) + " questions correct!")
print('you got ' + str((score / 4) * 100) + "% right  !")
