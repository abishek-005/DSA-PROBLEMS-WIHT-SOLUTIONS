# ---------- TIC TAC TOE WITH MINIMAX ----------

HUMAN = "X"
AI = "O"
EMPTY = " "

# Create empty board
def create_board():
    return [EMPTY] * 9

# Print board
def print_board(board):
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(board, player):
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8), # rows
        (0,3,6),(1,4,7),(2,5,8), # cols
        (0,4,8),(2,4,6)          # diagonals
    ]
    for a,b,c in win_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Check draw
def is_draw(board):
    return EMPTY not in board

# Evaluate board
def evaluate(board):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, HUMAN):
        return -1
    else:
        return 0

# Get possible moves
def possible_moves(board):
    return [i for i in range(9) if board[i] == EMPTY]

# Minimax algorithm
def minimax(board, is_maximizing):
    score = evaluate(board)

    if score != 0 or is_draw(board):
        return score

    if is_maximizing:
        best_score = -1000
        for move in possible_moves(board):
            board[move] = AI
            best_score = max(best_score, minimax(board, False))
            board[move] = EMPTY
        return best_score
    else:
        best_score = 1000
        for move in possible_moves(board):
            board[move] = HUMAN
            best_score = min(best_score, minimax(board, True))
            board[move] = EMPTY
        return best_score

# Best move for AI
def best_ai_move(board):
    best_score = -1000
    move = -1
    for i in possible_moves(board):
        board[i] = AI
        score = minimax(board, False)
        board[i] = EMPTY
        if score > best_score:
            best_score = score
            move = i
    return move

# Main game loop
def play_game():
    board = create_board()
    print("Tic Tac Toe (You = X, AI = O)")
    print_board(board)

    while True:
        # Human move
        pos = int(input("Enter position (0-8): "))
        if board[pos] != EMPTY:
            print("Invalid move da macha 😅")
            continue
        board[pos] = HUMAN
        print_board(board)

        if check_winner(board, HUMAN):
            print("🎉 Nee WIN da macha!")
            break
        if is_draw(board):
            print("😐 Draw!")
            break

        # AI move
        ai_pos = best_ai_move(board)
        board[ai_pos] = AI
        print("🤖 AI move:")
        print_board(board)

        if check_winner(board, AI):
            print("😈 AI WIN da!")
            break
        if is_draw(board):
            print("😐 Draw!")
            break

# Start game
play_game()
