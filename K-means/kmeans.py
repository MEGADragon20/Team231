from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math
import copy

exampleCenters = 3
exampleNSamples = 100
x_y, c = make_blobs(cluster_std = 0.8, n_samples= exampleNSamples, centers= exampleCenters)
print(x_y, c)

plt.scatter(x_y[:, 0], x_y[:, 1], c=c)



def abstand_berechnen(pair1, pair2):
    x1, y1 = pair1[0], pair1[1]
    x2, y2 = pair2[0], pair2[1]

    return(math.sqrt((y1 - y2)**2 + (x1 - x2)**2))

def highest(samples, centers, y_werte: list):
    number = round(samples/centers)
    number = number + 1
    groups = []
    while len(y_werte) > number:
        a = []
        for i in range(number):
            a.append(y_werte[0])
            y_werte.pop(0)
        groups.append(a)
    groups.append(y_werte)
    return groups
        
def y_sorted(coords):
    y_werte = []
    for i in coords:
        y_werte.append(i[1])

    y_werte.sort()
    return y_werte

def x_sorted(coords):
    x_werte = []
    for i in coords:
        x_werte.append(i[0])

    x_werte.sort()
    return x_werte

def findymedian(groups):
    mids=[]
    for a in groups:
        mids.append(a[round(len(a)/2)])
    return mids

def findlines(mids):
    lines=[]
    for a in range(len(mids)-1):
        lines.append((mids[a]+mids[a+1])/2)
    return lines

def squares_anzahl_ber(squares_koord):
    anzahl=[]
    for i in squares_koord:
        anzahl.append(len(i))
    return anzahl

def squares_numbern(squares,samples):
    anzahl=[[],[],[],[],[],[],[],[],[]]
    counter = 0
    for i in squares:
        for j in samples:
            if j[0] > i[0][0] and j[0] < i[1][0] and j[1] > i[0][1] and j[1] < i[1][1]:
                anzahl[counter].append(j)
        counter += 1
    return anzahl

def square_zuordnen(liny, linx,coords):
    squares=squaresmake(liny,linx)
    squares_koords=squares_numbern(squares, coords)
    squares_anzahl=squares_anzahl_ber(squares_koords)
    
    squares_anzahl_sorted=copy.deepcopy(squares_anzahl)
    squares_anzahl_sorted.sort()
    squares_anzahl_sorted.reverse()
    print(squares_anzahl)
    print(squares_anzahl_sorted)
    c=-3
    for i in squares_anzahl_sorted[:3]:
        squares_anzahl[squares_anzahl.index(i)]=c
        c+=1
    counter=0
    for i in squares_anzahl:
        if i > 0:
            x_sum = 0
            y_sum = 0
            for j in squares_koords[counter]:
                x_sum += j[0]
                y_sum += j[1]
            x_avr=x_sum/i
            y_avr=y_sum/i
            distances=[]
            distances.append((x_avr-min(linx))**2)
            distances.append((x_avr-max(linx))**2)
            distances.append((y_avr-liny[0])**2)
            distances.append((y_avr-liny[1])**2)
            min_din=distances.index(min(distances))
            if min_din==0:
                if x_avr < min(linx):
                    squares_anzahl[counter]=squares_anzahl[counter+3]
                else:
                    squares_anzahl[counter]=squares_anzahl[counter-3]
            if min_din==1:
                if x_avr < max(linx):
                    squares_anzahl[counter]=squares_anzahl[counter+3]
                else:
                    squares_anzahl[counter]=squares_anzahl[counter-3]
            if min_din==2:
                if y_avr < min(liny):
                    squares_anzahl[counter]=squares_anzahl[counter+1]
                else:
                    squares_anzahl[counter]=squares_anzahl[counter-1]
            if min_din==3:
                if y_avr < max(liny):
                    squares_anzahl[counter]=squares_anzahl[counter+1]
                else:
                    squares_anzahl[counter]=squares_anzahl[counter-1]
        counter+=1

    for i in range(len(squares_anzahl)):
        squares_anzahl[i]+=3

    return squares_anzahl



def squaresmake(liny, linx):
    squares = []
    squares.append([[-100,-100],[min(linx), min(liny)]])
    squares.append([[-100,min(liny)],[min(linx), max(liny)]]) 
    squares.append([[-100,max(liny)],[min(linx), 100]])
    squares.append([[min(linx),-100],[max(linx), min(liny)]])     
    squares.append([[min(linx),min(liny)],[max(linx), max(liny)]])     
    squares.append([[min(linx),max(liny)],[max(linx), 100]])   
    squares.append([[max(linx),-100],[100, min(liny)]])     
    squares.append([[max(linx),min(liny)],[100, max(liny)]])     
    squares.append([[max(linx),max(liny)],[100, 100]])
    return squares 

def main(coords, solution, centers, samples):
    y_h = highest(samples, centers, y_sorted(coords))
    midsy = findymedian(y_h)
    print("'################################")
    print(midsy)
    liny = findlines(midsy)
    print(liny)
    print("################################")
    x_h = highest(samples, centers, x_sorted(coords))
    midsx = findymedian(x_h)
    linx = findlines(midsx)
    print(square_zuordnen(liny,linx,coords))
    return (liny, linx)



g = main(x_y, c, exampleCenters, exampleNSamples)
print("")
print("")
print("#",g,"#")

plt.axline((0, g[0][0]), slope = 0)
plt.axline((0, g[0][1]), slope= 0)

plt.axline((g[1][0],0), slope = math.inf)
plt.axline((g[1][1],0), slope= math.inf)

plt.show()