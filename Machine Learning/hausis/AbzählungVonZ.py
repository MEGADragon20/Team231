def abzählungVonGanzenZahlen(menge: set):
    N = set()
    for i in menge:
        if i == 0:
            N.add(i)
        elif i > 0:
            N.add(i*2)
        elif i < 0:
            N.add((i*-2) - 1)
    return N

def umkehrFunktion(menge: set):
    Z = set()
    for i in menge:
        if i == 0:
            Z.add(i)
        elif i%2 == 0:
            Z.add(i/2)
        elif i%2 == 1:
            Z.add((i + 1)/ - 2)
    return Z
l = set()
for i in range(200):
    l.add(i)

print(l)
print(umkehrFunktion(l))