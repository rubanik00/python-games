import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6]) 
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'Х' or letter == '0'):
        print('Вы выбираете Х или О?')
        letter = input().upper()
    
    if letter == 'Х':
        return ['Х','0']
    else:
        return ['0', 'Х']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board,letter,move):
    board[move] = letter

def isWiner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    boardCopy = []

    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход (1-9)')
        move = input()

    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMove = []

    for i in moveList:
        if isSpaceFree(board, i):
            possibleMove.append(i)
        
    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = '0'
    else:
        playerLetter = 'X'
    
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWiner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWiner(boardCopy, playerLetter):
                return i
    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Игра "Крестики-нолики"')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWiner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWiner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'

    
    print('Сыграем еще раз? (да или нет)') 
    if not input().lower().startswith('д'):
        break