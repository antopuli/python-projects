
# IMPORT RANDRANGE FUNCTION FOR COMPUTER MOVEMENTS
from random import randrange


# CREATE THE STARTING BOARD
board = []
n = 1
for row in range(3):
    column = [n, n+1, n+2]
    n += 3
    board.append(column)
board[1][1] = 'X'

# FUNCTIONS
def displayBoard():

    # DISPLAY THE CURRENT STATUS OF THE BOARD
    
    print(
            f"""
            +-------+-------+-------+
            |       |       |       |
            |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
            |       |       |       |
            +-------+-------+-------+
            """
        )
          
def enterMove():
    
    # ASKS THE USER ABOUT THEIR MOVE, CHECKS THE INPUT AND UPDATES THE BOARD
    
    isFree = False
    
    try:
        move = int(input("Enter your move: "))
        
        if move < 1 or move > 9: 
            print("ERROR! You can't enter a value less than 1 or greater than 9.")
            enterMove()
        else:
            
            for r, c in makeAListOfFreeFields():
                if board[r][c] == move: 
                    isFree = True
                    move = (r, c)
            if isFree:
                board[move[0]][move[1]] = 'O'
            else:
                print("Invalid move.")
                enterMove()
         
    except:
        print("Invalid input!")
        enterMove()
          
def makeAListOfFreeFields():
    
    # BUILDS A LIST OF ALL THE FREE SQUARES, CONSISTING OF A TUPLE LIST
    
    freeFields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'X' or board[r][c] == 'O': continue
            freeFields.append((r, c))
    return freeFields


def victoryFor(sign):
    
    # THE FUNCTION VERIFY IF SOMEONE HAS WON THE GAME
    
    global gameStatus
    global winner
    
    gameStatus = True
    winner = ''
    
    if \
    (board[2][0] == board[1][1] and board[1][1] == board[0][2]) or \
    (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
    (board[0][0] == board[1][0] and board[1][0] == board[2][0]) or \
    (board[0][1] == board[1][1] and board[1][1] == board[2][1]) or \
    (board[0][2] == board[1][2] and board[1][2] == board[2][2]) or \
    (board[0][0] == board[0][1] and board[0][1] == board[0][2]) or \
    (board[1][0] == board[1][1] and board[1][1] == board[1][2]) or \
    (board[2][0] == board[2][1] and board[2][1] == board[2][2]):
        gameStatus = False
        winner = sign
    elif len(makeAListOfFreeFields()) == 0:
        gameStatus = False
        winner = 'none'
        
 

def drawMove():
    
    # The function draws the computer's move and updates the board.
    
    cpuMove = randrange(1, 10)
    isFree = False
    
    for r, c in makeAListOfFreeFields():
        if board[r][c] == cpuMove: 
            isFree = True
            cpuMove = (r, c)
            
    if isFree:
        board[cpuMove[0]][cpuMove[1]] = 'X'
    else:
        drawMove()




# EXE

displayBoard()

while True:
    
    enterMove()
    displayBoard()
    victoryFor('O')
    if not gameStatus: break
    
    drawMove()
    displayBoard()
    victoryFor('X')
    if not gameStatus: break
    

if winner == 'O': print("You won!")
elif winner == 'X': print("You lost!")
elif winner == 'none' : print("Tie.")