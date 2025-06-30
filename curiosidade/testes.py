import numpy as np

class TicTacToe:
    def __init__(self, row, column, gameboard): 
        self.gameboard = gameboard
        self.row = row
        self.column = column
        pass

def victorySet(gameboard):
    lines = [
        # ROW
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        # COLUMNS
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        # DIAGONAL
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for line in lines:
        values = [gameboard[r][c] for r, c in line]
        if values[0] == values[1] == values[2] != 0:
            if values[0] == 1:
                print("WINNER PLAYER 1")
            else:
                print("WINNER PLAYER 2")

def game():
    game = TicTacToe
    game.gameboard = np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
    return game.gameboard
board = game()

# TURN SYSTEM
turno = False

# WHILE LOOP
loop = 1

def player1(loop):
    game.row = int(input("ROW: "))
    game.column = int(input("COLUMN: "))

    if 0 <= game.row < 3 and 0 <= game.column < 3:
        if board[game.row][game.column] == 0:
            turno = True
            loop += 1

            board[game.row][game.column] = 1

            print(board)
            turno = False
        else:
            print("Invalid position -- player 1")
            True
    else:
        print("The limit was passed -- player 1")
        turno = True

    return board
player1_v = player1(loop)

def player2(loop):
    game.row = int(input("ROW2: "))
    game.column = int(input("COLUMN: "))

    if 0 <= game.row < 3 and 0 <= game.column < 3:
        if board[game.row][game.column] == 0:
            board[game.row][game.column] = -1
            
            print(board)
            loop += 1
        else:
            print("The limit was passed -- player 2")
            print(board)
    else:
        print("The limit was passed -- player 2")

    return board
player2_v = player2(loop)

# GAME
while loop <= 10:
    player1(loop)
    if victorySet(player1_v):
        break

    if turno == False:
        player2(loop)
    if victorySet(player2_v):
        break

print("FINAL GAMEBOARD")
print(board)