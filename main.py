import random

# Define the board with grid lines
def print_board(board):
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(f"{idx} {' '.join(row)}")
    print()

# Check if the current player has won
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Center column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal
        [board[2][0], board[1][1], board[0][2]]   # Diagonal
    ]
    return [player, player, player] in win_conditions

# Check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm to determine the best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Find the best move for the computer
def find_best_move(board):
    best_move = None
    best_score = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game")
    print("You are 'X', and the computer is 'O'.")
    print_board(board)
    
    while True:
        # Player move
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue
            board[row][col] = 'X'
        except (IndexError, ValueError):
            print("Invalid input. Enter row and column as two integers between 0 and 2.")
            continue
        
        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Computer move
        print("Computer's turn...")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        
        if check_winner(board, 'O'):
            print_board(board)
            print("Computer wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        print_board(board)

# Run the game
play_game()
