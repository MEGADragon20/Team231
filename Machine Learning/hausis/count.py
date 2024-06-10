a = 9
def check_for_victory(gitter):
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
    return False
def check_if_full(gitter):
    for i in range(3):
        for j in range(3):
            if gitter[i][j].owner == None:
                return False
    return True

pseudo = [[None, None, None],[None, None, None],[None, None, None]]

while True:
    x = 0
    y = 0

     