from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math

exampleCenters = 3
exampleNSamples = 100
x_y, c = make_blobs(cluster_std = 0.6, n_samples= exampleNSamples, centers= exampleCenters)
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
    return (liny, linx)



g = main(x_y, c, exampleCenters, exampleNSamples)
print("")
print("")
print(g)
for i in g:
    plt.axline((0, i[0]), slope = 0)
    plt.axline(( i[1], 0), slope= math.inf)

plt.show()