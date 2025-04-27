import random

board = [" " for _ in range(9)]
nodes_visited = 0  # Global counter

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + "|" + board[i*3+1] + "|" + board[i*3+2])
        if i < 2:
            print("-+-+-")
    print()

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_full():
    return " " not in board

# Standard Minimax
def minimax(is_maximizing):
    global nodes_visited
    nodes_visited += 1

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# Minimax with Alpha-Beta Pruning
def minimax_ab(is_maximizing, alpha, beta):
    global nodes_visited
    nodes_visited += 1

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax_ab(False, alpha, beta)
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cut-off
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax_ab(True, alpha, beta)
                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha cut-off
        return best_score

# RANDOMIZE the board
def randomize_board():
    global board
    choices = ["X", "O", " "]
    filled = random.randint(0, 6)  # Number of random filled spots (0 to 6)
    positions = random.sample(range(9), filled)

    # Reset the board
    board = [" " for _ in range(9)]

    # Randomly fill the selected positions
    for pos in positions:
        board[pos] = random.choice(["X", "O"])

# Testing
def test_minimax():
    global nodes_visited
    print("\nTesting Standard Minimax:")
    nodes_visited = 0
    minimax(True)
    print(f"Nodes visited: {nodes_visited}")

def test_minimax_ab():
    global nodes_visited
    print("\nTesting Minimax with Alpha-Beta Pruning:")
    nodes_visited = 0
    minimax_ab(True, -float('inf'), float('inf'))
    print(f"Nodes visited: {nodes_visited}")

# Main program
randomize_board()
print_board()
test_minimax()
test_minimax_ab()
