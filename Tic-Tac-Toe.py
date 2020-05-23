from random import randrange

def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def boardposition(board,move):
    global b1, b2
    for i, x in enumerate(board):
        if move in x:
            b1 = i
            b2 = x.index(move)
def EnterMove():
    global free
    move = "start"
    move = input("Enter your move(1-9): ")
    while move not in free:
        move = input("Invalid move, please enter your move(1-9): ")
    #get index
    place = free.index(move)
    del free[place]
    boardposition(board,move)
    board[b1][b2]="O"
    DisplayBoard(board)
    
def Cmove():
    global free
    cmove = str(randrange(10))
    while cmove not in free:
        cmove = str(randrange(10))
    place = free.index(cmove)
    del free[place]
    print("Computer's move:",cmove)
    boardposition(board,cmove)
    board[b1][b2]="X"
    DisplayBoard(board)

        
board = [['1','2','3'],['4',"X",'6'],['7','8','9']]
free = ['1','2','3','4','6','7','8','9']  
DisplayBoard(board)
EnterMove()
Cmove()
while True:
    EnterMove()
    if board[0] == ['O','O','O'] or\
       board[1] == ['O','O','O'] or\
       board[2] == ['O','O','O'] or \
       (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or\
       (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or\
       (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or\
       (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or\
       (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        print("You WIN!")
        break
    if free == []:
        print("Game Tied!")
        break
    Cmove()
    if board[0] == ['X','X','X'] or\
       board[1] == ['X','X','X'] or\
       board[2] == ['X','X','X'] or \
       (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or\
       (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or\
       (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or\
       (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or\
       (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') :
        print("You LOSE!")
        break
    if free == []:
        print("Game Tied!")
        break
print("GameEnd")

k=input("press enter to exit") 
