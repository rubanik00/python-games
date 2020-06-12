import random 
import time

def discriptGame():
    print('''
    Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры.
    В одной из них — дружелюбный дракон,
    который готов поделиться с вами своими сокровищами.
    Во второй — жадный и голодный дракон, который мигом вас съест.  ''')

def chooseCave():
    guess = ''

    while guess != '1' and guess != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        guess = input()
    return guess

def getRandomCave(guess):
    randomCave = random.randint(1,2)

    print(''' 
    Вы приближаетесь к пещере...
    Ее темнота заставляет вас дрожать от страха...
    Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...''')
    time.sleep(2)

    if guess == str(randomCave):
        print('...дарит вам сладости')
    else:
        print('...моментально вас съедает!')
    
def playAgin():
    while True:
        print('Попытать удачу еще раз?')
        if input().lower().startswith('d'):
            startGame()
        else:
            break


def startGame():
    discriptGame()
    guess = chooseCave()
    getRandomCave(guess)
    playAgin()

startGame()
