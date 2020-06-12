import random

HANGMAN_PICS = [''' 
    +---+
        |
        |
        |
       ===''','''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
    |   |
        |
       ===''',''' 
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''',''' 
    +---+
    O   |
   /|\  |
   /    |
       ===''',''' 
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
    
words = 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split()

def getRandomWorld(words):
    numWord = random.randint(0, len(words))
    return words [numWord]

def displayGame(correctLetter, missLetter, secretWord):
    print(HANGMAN_PICS[len(missLetter)])
    print()

    print('Ошибочные буквы', end=' ')
    for letter in missLetter:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetter:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuess):
    print('Введите букву.')
    
    while True:
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuess:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def playAgin():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')

correctLetter = ''
missLetter = ''
secretWord = getRandomWorld(words)
gameIsDone = False

while True:
    displayGame(correctLetter, missLetter, secretWord)
    guess = getGuess(correctLetter + missLetter)

    if guess in secretWord:
        correctLetter = correctLetter + guess
        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetter:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - ' + secretWord + "! Вы угадали")
            gameIsDone = True
    else:
        missLetter = missLetter + guess

        if len(missLetter) == len(HANGMAN_PICS) - 1:
            displayGame(correctLetter, missLetter, secretWord)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(missLetter))+'и угадано букв:'+str(len(correctLetter))+'.Было загадано слово"'+secretWord+'".')
            gameIsDone = True
    
    if gameIsDone:
        if playAgin():
            correctLetter = ''
            missLetter = ''
            secretWord = getRandomWorld(words)
            gameIsDone = False
        else:
            break   

    

        

    
