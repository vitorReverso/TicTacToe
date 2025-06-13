import numpy as np

# FUNCTIONS
def victory_system(tabuleiro):
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
            values = [tabuleiro[pos[0]][pos[1]] for pos in line]

            if values[0] == values[1] == values[2] != 0:
                winner = values[0]
                print(f"Player: {'1' if winner == 1 else '2'} wins")
                return True
                
        return False # if dont have victory

# CREATE THE GAME BOARD
tabuleiro = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

loop = 1

# PALY TIME SYSTEM
turno = None

while loop <= 10:
    # PLAYER 1: CODE
    # PLAYER 1: CODE
    row = int(input("line: "))
    column = int(input("column: "))

    if 0 <= row < 3 and 0 <= column < 3:
        if tabuleiro[row][column] == 0:
            turno = True
            loop += 1
            tabuleiro[row][column] = 1
            print(tabuleiro)
            print(loop)
            turno = False
        else:
            print("invalid position")
            print(tabuleiro)
            turno = True
            continue
    else:
        print("the position passed the limit")
        turno = True

    # VICTORY SYSTEM
    if victory_system(tabuleiro):
        break                   

    if loop >= 10:
        print("the both loses") # FOR AVOID THE PLAYER 2 TO PLAY AFTER AT END GAME
        break

    # PLAYER 2: CODE
    if turno == False:
        row2 = int(input("line2: "))
        column2 = int(input("column2: "))

        if 0 <= row2 < 3 and 0 <= column2 < 3:
            if tabuleiro[row2][column2] == 0:
                tabuleiro[row2][column2] = -1
                print(tabuleiro)            
                loop += 1    
            else:
                print("invalid position")
                print(tabuleiro)

            if victory_system(tabuleiro):
                break
        else:
            print("the position passed the limits")