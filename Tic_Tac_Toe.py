import random
board=["-","-","-","-","-","-","-","-","-",]
currentPlayer="X"
gameRunning=True
winner=None
 
def printBoard(board):
    print(board[0]+" | "+board[1]," | "+board[2])
    print("------------")
    print(board[3]+" | "+board[4]," | "+board[5])
    print("------------")
    print(board[6]+" | "+board[7]," | "+board[8])
    
def playerInput(board):
    user_inp=int(input("enter a num 1-9: "))
    if user_inp >=1 and user_inp <=9  and board[user_inp-1]=="-":
        board[user_inp-1]=currentPlayer
    else:
        print("Oops already occupied")



def checkHorizontle(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True
    
    
    elif board[3]==board[1]==board[4] and board[5]!="-":
        winner=board[3]
        return True
    
    elif board[6]==board[7]==board[8] and board[8]!="-":
        winner=board[6]
        return True


def checkRow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    if board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True

def  checkDiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True  
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[0]
        return True  
    
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("its a tie")
        gameRunning=False
        
def computer(board):
    while currentPlayer=="O":
        spots=random.randint(0,8)
        if board[spots]=="-":
            board[spots]="O"
            switchPlayer()
        
        
def checkWin():
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        
        
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"
        
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)