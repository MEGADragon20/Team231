def availableMoves(field):
        dahfgjhsdfg = []
        for i in range(3):
            for j in range(3):
                if field[i][j] == None:
                    dahfgjhsdfg.append((i,j))
        return dahfgjhsdfg


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
    