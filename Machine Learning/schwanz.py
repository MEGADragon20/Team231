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
        if i[0].owner == i[1].owner and i[1].owner == i[2].owner and i[2].owner != None:
            winner = i[0].owner
    for i in range(3):
        if field[0][i].owner == field[1][i].owner and field[1][i].owner == field[2][i].owner and field[2][i].owner != None:
            winner = field[0][i].owner
    if field[0][0].owner == field[1][1].owner and field[1][1].owner == field[2][2].owner and field[2][2].owner != None:
        winner = field[0][0].owner
    if field[0][2].owner == field[1][1].owner and field[1][1].owner == field[2][0].owner and field[2][0].owner != None:
        winner = field[0][2].owner 
    if winner == None:
        return 0
    elif winner == "x":
        return -10
    elif winner == "o":
        return 10
    
def make_move(field, owner, move):
    field[move[0]][move[1]].owner = owner

def undoMove(field, move: tuple):
    field[move[0]][move[1]].owner = None

def gameOver(gitter):
    for i in gitter:
        if i[0].owner == i[1].owner and i[1].owner == i[2].owner and i[2].owner != None:
            return True
    for i in range(3):
        if gitter[0][i].owner == gitter[1][i].owner and gitter[1][i].owner == gitter[2][i].owner and gitter[2][i].owner != None:
                return True
    if gitter[0][0].owner == gitter[1][1].owner and gitter[1][1].owner == gitter[2][2].owner and gitter[2][2].owner != None:
        return True
    if gitter[0][2].owner == gitter[1][1].owner and gitter[1][1].owner == gitter[2][0].owner and gitter[2][0].owner != None:
        return True
    for i in range(3):
        for j in range(3):
            if gitter[i][j].owner == None:
                return False
    return True
