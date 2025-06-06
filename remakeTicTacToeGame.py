import numpy as np

# PARTE DO JOGO
tabuleiro = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

loop = 1

# TURN SYSTEM
turno = None

while loop <= 9:
    # PLAYER 1
    row = int(input("line: "))
    column = int(input("column: "))

    # PLAYER 1 SYSTEM
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
        print("The position passed the limit")
        continue

    if loop >= 9:
        break

    # PLAYER 2 SYSTEM
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
        else:
            print("The position passed the limit")
            continue
    else:
        print("PLAYER 2 TRUE")
        continue
    
# SISTEMA DE VERIFAÇÃO DE VITORIA
if tabuleiro[0][0] & tabuleiro[0][1] & tabuleiro[0][2] == 1 or -1:
    print("")