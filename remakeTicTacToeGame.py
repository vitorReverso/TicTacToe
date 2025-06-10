import numpy as np

# CREATE THE GAME BOARD
tabuleiro = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

loop = 1

# PALY TIME SYSTEM
turno = None

while loop <= 10:
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

        # TESTS VERIFICATION
        # ROWS
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != 0:
            if tabuleiro[0][0] == 1:
                print("player 1 won")
                break

        if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != 0:
            if tabuleiro[1][0] == 1:
                print("player 1 win")
                break

        if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != 0:
            if tabuleiro[2][0] == 1:
                print("player 1 win")
                break                
        
        # COLUMNS
        if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != 0:
            if tabuleiro[0][0] == 1:
                print("player 1 win")
                break

        if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != 0:
            if tabuleiro[0][1] == 1:
                print("player 1 win")
                break

        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != 0:
            if tabuleiro[0][2] == 1:
                print("player 1 win")
                break  

        # DIAGONAL
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
            if tabuleiro[0][0] == 1:
                print("player 1 win")
                break

        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
            if tabuleiro[0][2] == 1:
                print("player 1 win")
                break                   
    else:
        print("The position passed the limit")
        turno = True
        continue

    if loop >= 10: # FOR AVOID THE PLAYER 2 TO PLAY AFTER AT END GAME
        break

    # PLAYER 2: CODE
    if turno == False:
        row2 = int(input("line2: "))
        column2 = int(input("column2: "))

        if 0 <= row2 < 3 and 0 <= column2 < 3:
            if tabuleiro[row2][column2] == 0:
                loop += 1

                tabuleiro[row2][column2] = -1
                print(tabuleiro)
            else:
                print("invalid position")
                print(tabuleiro)
                continue

            if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != 0:
                if tabuleiro[0][0] == -1:
                    print("player 2 won")
                    break

            if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != 0:
                if tabuleiro[1][0] == -1:
                    print("player 2 win")
                    break

            if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != 0:
                if tabuleiro[2][0] == -1:
                    print("player 2 win")
                    break                
            
            # COLUMNS
            if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != 0:
                if tabuleiro[0][0] == -1:
                    print("player 2 win")
                    break

            if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != 0:
                if tabuleiro[0][1] == -1:
                    print("player 2 win")
                    break

            if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != 0:
                if tabuleiro[0][2] == -1:
                    print("player 2 win")
                    break  

            # DIAGONAL
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
                if tabuleiro[0][0] == -1:
                    print("player 2 win")
                    break

            if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
                if tabuleiro[0][2] == -1:
                    print("player 2 win")
                    break                
        else:
            print("The position passed the limit")
            continue
    else:
        print("PLAYER 2 TRUE")
        continue
    