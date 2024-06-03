def minimax(board, depth, maxen):
    if gameOver(board):
        return evaluateBoard(board)

    if maxen == True:
        bScore = -9999999999999999999999
        for i in availableMoves(board):
            make_move(board, "x" , i)
            score = minimax(board, depth+1, False)
            undoMove(board, i)
            best_score = max(score, bScore)
        return best_score
    else:
        bScore = 9999999999999999999999
        for i in availableMoves(board):
            make_move(board, "o" , i)
            score = minimax(board, depth+1, True)
            undoMove(board, i)
            best_score = min(score, bScore)
        return best_score

def availableMoves(field):
        dahfgjhsdfg = []
        for i in range(3):
            for j in range(3):
                if field[i][j] == None:
                    dahfgjhsdfg.append((i,j))
        return dahfgjhsdfg

def findBestMove(field):
    bestMove = None
    bestScore = -100
    for i in range(3):
        for j in range(3):
            move = (i,j)
            make_move(field, "x", move)
            moveScore = minimax(field, 0, False)
            undoMove(field, move)
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = move
    return bestMove 
def evaluateBoard(field):
    winner = None
    for i in field:
        if i[0] == i[1] and i[1] == i[2] and i[2] != None:
            winner = i[0]
    for i in range(3):
        if field[0][i] == field[1][i] and field[1][i] == field[2][i] and field[2][i] != None:
            winner = field[0][i]
    if field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[2][2] != None:
        winner = field[0][0]
    if field[0][2] == field[1][1] and field[1][1] == field[2][0] and field[2][0] != None:
        winner = field[0][2] 
    if winner == None:
        return 0
    elif winner == "x":
        return -10
    elif winner == "o":
        return 10
    
def make_move(field, owner, move):
    field[move[0]][move[1]] = owner

def undoMove(field, move: tuple):
    field[move[0]][move[1]] = None

def gameOver(gitter):
    for i in gitter:
        if i[0] == i[1] and i[1] == i[2] and i[2] != None:
            return True
    for i in range(3):
        if gitter[0][i] == gitter[1][i] and gitter[1][i] == gitter[2][i] and gitter[2][i] != None:
                return True
    if gitter[0][0] == gitter[1][1] and gitter[1][1] == gitter[2][2] and gitter[2][2] != None:
        return True
    if gitter[0][2] == gitter[1][1] and gitter[1][1] == gitter[2][0] and gitter[2][0] != None:
        return True
    for i in range(3):
        for j in range(3):
            if gitter[i][j] == None:
                return False
    return True


field = [[None, None, "o"],["o", "x", None],["o", None, "x"]]
print(findBestMove(field))