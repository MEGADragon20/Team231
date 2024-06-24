def check_for_victory(gitter):
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
    return False
def check_if_full(gitter):
    for i in range(3):
        for j in range(3):
            if gitter[i][j] == None:
                return False
    return True

def filter(gitter):
    return False if check_for_victory(gitter) or check_if_full(gitter) else True

def trans(lis: list):
    return [[lis[0],lis[1],lis[2]],[lis[3],lis[4],lis[5]],[lis[6],lis[7],lis[8]]]
pseudo = [[None, None, None],[None, None, None],[None, None, None]]
ps = [None, None, None, None, None, None, None, None, None]

from tqdm import tqdm

All = []

x = 0
#!1.
for h in tqdm(range(9), leave=False):
    ps[h] = "x"
    if ps not in All:
        a = []
        for b in ps:
            a.append(b)
        All.append(a)
#!2.
    for i in tqdm(range(9), leave=False):
        if ps[i] == None:
            ps[i]= "o"
            if ps not in All:
                a = []
                for b in ps:
                    a.append(b)
                All.append(a)
#!3.
            for j in tqdm(range(9), leave=False):
                if ps[j] == None:
                    ps[j]= "x"
                    if ps not in All:
                        a = []
                        for b in ps:
                            a.append(b)
                        All.append(a)
#!4.
                for k in range(9):
                    if ps[k] == None:
                        ps[k]= "o"
                        if ps not in All:
                            a = []
                            for b in ps:
                                a.append(b)
                            All.append(a)
#!5.
                    for l in range(9):
                        if ps[l] == None:
                            ps[l]= "x"
                            if ps not in All:
                                a = []
                                for b in ps:
                                    a.append(b)
                                All.append(a)
                        if filter(trans(ps)) == False:
                            break
                        else:
#!6.                        
                            for m in range(9):
                                if ps[m] == None:
                                    ps[m]= "o"
                                    if ps not in All:
                                        a = []
                                        for b in ps:
                                            a.append(b)
                                        All.append(a)
                                if filter(trans(ps)) == False:
                                    break
                                else:
#!7.
                                    for n in range(9):
                                        if ps[n] == None:
                                            ps[n]= "x"
                                            if ps not in All:
                                                a = []
                                                for b in ps:
                                                    a.append(b)
                                                All.append(a)
                                        if filter(trans(ps)) == False:
                                            break
                                        else:
#!8.
                                            for o in range(9):
                                                if ps[o] == None:
                                                    ps[o]= "o"
                                                    if ps not in All:
                                                        a = []
                                                        for b in ps:
                                                            a.append(b)
                                                        All.append(a)
                                                if filter(trans(ps)) == False:
                                                    break
                                                else:
#!9.
                                                    for p in range(9):
                                                        if ps[p] == None:
                                                            ps[p]= "x"
                                                            if ps not in All:
                                                                a = []
                                                                for b in ps:
                                                                    a.append(b)
                                                                All.append(a)
                                                        if filter(trans(ps)) == False:
                                                            if ps[p] is not None:
                                                                ps[p] = None
                                                            break
                                                        if ps[p] is not None:
                                                            ps[p] = None
                                                if ps[o] is not None:
                                                    ps[o] = None
                                        if ps[n] is not None:
                                            ps[n] = None
                                if ps[m] is not None:
                                    ps[m] = None
                        if ps[l] is not None:
                            ps[l] = None
                    if ps[k] is not None:
                        ps[k] = None
                if ps[j] is not None:
                    ps[j] = None
        if ps[i] is not None:
            ps[i] = None

    ps[h] = None
    
    
print(len(All))


