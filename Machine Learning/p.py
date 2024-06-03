def evaluate(board):
    # Überprüfen, ob jemand gewonnen hat
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '-':
            return 1 if board[row][0] == 'X' else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return 1 if board[0][col] == 'X' else -1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return 1 if board[0][0] == 'X' else -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return 1 if board[0][2] == 'X' else -1
    
    # Überprüfen, ob das Spiel unentschieden ist
    if '-' not in [cell for row in board for cell in row]:
        return 0
    
    # Das Spiel ist noch nicht zu Ende
    return None

def minimax(board, depth, is_maximizing):
    result = evaluate(board)
    
    # Wenn das Spiel zu Ende ist oder die maximale Tiefe erreicht wurde
    if result is not None or depth == 0:
        return result, None
    
    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score, _ = minimax(board, depth - 1, False)
                    board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score, _ = minimax(board, depth - 1, True)
                    board[i][j] = '-'
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move

def make_best_move(board):
    _, best_move = minimax(board, 9, True)
    return best_move

# Beispiel für die Verwendung:
board = [
    ['O', 'O', 'X'],
    ['X', 'X', 'O'],
    ['-', '-', '-']
]

best_move = make_best_move(board)
print("Best move:", best_move)