import random

gToken = 0

print('Hi, what is your name? ')

number = random.randint(1,20)

myName = input()

for gToken in range(6):
    print(myName + ' let\'s try to guess number')
    myNum = input()
    myNum = int(myNum)

    if myNum < number:
        print('Your number is so small')

    if myNum > number:
        print('Your number is so big')
    
    if myNum == number:
        gToken = str(gToken + 1)
        print('Super, ' + myName + '! You are win! Your try is ' + gToken )
        break

if myNum != number:
    number = str(number)
    print('Oh you are lose, The right number is ' + number)


