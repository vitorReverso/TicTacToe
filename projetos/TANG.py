import numpy as np

class TicTacToe:
    def __init__(self, gameboard, row, collumn):
        self.gameboard = gameboard
        self.row = row
        self.collumn = collumn

        pass

def HE_init(fan_IN, fan_OUT):    # RELU weight
    std = np.sqrt(2.0 / fan_IN)
    return np.random.randn(fan_IN, fan_OUT) * std

def GLOROT_init(fan_IN, fan_OUT):    # SOFTMAX WEIGHT
    std = np.sqrt(2.0 / (fan_IN + fan_OUT))
    return np.random.randn(fan_IN, fan_OUT) * std

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / np.sum(e_x)

def ReLU(x):
    return np.maximum(0, x)

def derivative_Relu(x):
    return np.where(x > 0, 1, 0)

def trainingData_set():
    lines = np.array([
        # ROW
        [1, 1, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 0, 0, 0, 0, 0, 0], 
        
        # ROW 2
        [0, 0, 0, 1, 1, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 1, 1, 0, 0, 0], 
        
        # ROW 3
        [0, 0, 0, 0, 0, 0, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1], 
        
        # COLUMN 1
        [1, 0, 0, 1, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 1, 0, 0, 1, 0, 0], 
        
        # COLUMN 2
        [0, 1, 0, 0, 1, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 1, 0], 
        [0, 0, 0, 0, 1, 0, 0, 1, 0], 
        
        # COLUMN 3
        [0, 0, 1, 0, 0, 1, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 1, 0, 0, 1], 
        
        # DIAGONAL 
        [1, 0, 0, 0, 1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 1, 0, 0, 0, 1], 
        
        # DIAGONAL 2
        [0, 0, 1, 0, 1, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 1, 0, 1, 0, 0], 
    ])   

    return lines
dataSet = trainingData_set()

def targets():
    target = np.array([
        # ROW
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        
        # ROW 2
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        
        # ROW 3
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        
        # COLUNAS
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],

        # COLUMN 2
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],

        # COLUMN 3
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        
        # DIAGONAL
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        
        # DIAGONAL 2
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
    ])
    return target
targets_y = targets()

def victory_Set(board):
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
    for i in lines:
        values = [board[r][c] for r, c in i]
        if values[0] == values[1] == values[2]:
            if values[0] == 1:
                print("player 1 win")
            else:
                print("player 2 win ")

def game():
    game = TicTacToe
    game.gameboard = np.array([[1, 0, 0],
                                [1, 0, 0],
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

            board[game.row][game.column] = 2

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

def NEURAL_NETWORK(board):
    original_input = board.flatten()
    
    # WEIGHT
    HE_weight = HE_init(9, 9)
    GLOROT_weight = GLOROT_init(len(original_input), 9)
    learning_rate = 0.01

    # HIDDEN LAYER
    turno = True
    for epoch in range(10000):
        total_loss = 0
        for i in range(len(targets_y)):
            simple_inputs = dataSet[i]
            target = targets_y[i]

            output_Relu = ReLU(np.dot(simple_inputs, HE_weight))
            softmax_output = softmax(np.dot(output_Relu, GLOROT_weight))
            
            # CROSS ENTROPY
            eps = 1e-15
            y_pred = np.clip(softmax_output, eps, 1 - eps)
            entropy = -np.sum(target * np.log(y_pred))
            total_loss += entropy

            # ERROR 
            error = softmax_output - target

            # BACKPROPAGATION
            grad_glorot = np.outer(output_Relu, error)
            hidden_grad = np.dot(error, GLOROT_weight.T) * derivative_Relu(np.dot(simple_inputs, HE_weight))
            grad_He = np.outer(simple_inputs, hidden_grad)

            # ADJUSTMENT
            HE_weight -= learning_rate * grad_He
            GLOROT_weight -= learning_rate * grad_glorot
    
        if epoch % 500 == 0:
            print(f"epoch {epoch}, Loss: {total_loss:.4f}")

    hidden_real = ReLU(np.dot(original_input, HE_weight))
    output_real = softmax(np.dot(hidden_real, GLOROT_weight))

    # VECTOR ONE-HOT
    turno = False

    vector = [0] * 9
    vector[np.argmax(output_real)] = -1
    vector = np.array(vector)

    board = board + (vector.reshape(3, 3))
    print(board)

    return board
neural = NEURAL_NETWORK(board)

while loop < 10:
    player1(loop)
    if victory_Set(player1_v):
        break

    if loop >= 10:
        print("The both loses")

    if turno == False:
        NEURAL_NETWORK(board)
        print(board)

        if victory_Set(neural):
            break

print(board)