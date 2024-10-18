# Initialize the board
board = ['' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(cell if cell != '' else ' ' for cell in row))
        print('-'*5)

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif '' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')  
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

# AI move using Minimax algorithm
def ai_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    if move is not None:       
        board[move] = 'X'

# Function to play the game
def play_game():
    while True:
        print_board(board)
        if check_win(board, 'X'):
            print("X wins!")
            break
        elif check_win(board, 'O'):
            print("O wins!")
            break
        elif '' not in board:
            print("It's a tie!")
            break

        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == '':
                board[move] = 'O'
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # AI move
        ai_move(board)

# Start the game
play_game()
