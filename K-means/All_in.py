from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math
import numpy as np

exampleCenters = 3
exampleNSamples = 100
x_y, c = make_blobs(cluster_std = 0.6, n_samples= exampleNSamples, centers= exampleCenters)
#print(x_y, c)

plt.scatter(x_y[:, 0], x_y[:, 1], c=c)


def abstand_berechnen(punkte):
        return math.sqrt((punkte[0][0]-punkte[1][0])**2+(punkte[0][1]-punkte[1][1])**2)
def not_in_ABERAUFCRACK(l, e):
    for i in l:
        if i[0] == e[0] and i[1] == e[1]:
            return False
    return True
def find_nearest_neighbor(p, array, f):
    current_nearest = None
    current_distance = math.inf
    for i in array:
        if not_in_ABERAUFCRACK(f, i):
            if abstand_berechnen([i, p]) < current_distance:
                current_nearest = i
                current_distance = abstand_berechnen([i, p])
    return current_nearest, current_distance

def avg(l) -> float:
    sum = 0
    for i in l:
        sum += i
    return sum/len(l) if len(l) != 0 else None
          
def goth_rough_everything(array, centers):
    distances = []
    for p in range(len(array)):
        pointA = array[p-1]
        for pointB in array:
            if pointA[0] != pointB[0] and pointA[1] != pointB[1]:
                distances.append(abstand_berechnen([pointA, pointB]))

    distances.sort()
    sg = distances[:round(len(distances)/centers)]
    sg_avg = avg(sg)
    sg_max = sg[-1]
    sg_30_avg = avg(sg[-30:])
    print(sg_30_avg, sg_max)


    current = array[0]
    segments = []
    castouts = []
    forbidden = []
    for i in range(centers):
        segments.append([])
    print(len(array))
    while len(array) > len(forbidden):
        neighbor, distance = find_nearest_neighbor(current, array, forbidden)
        if distance <= sg_30_avg:
            segments[0].append(neighbor)
        elif sg_max > distance > sg_30_avg:
            castouts.append(neighbor)
        else:
            a = segments[0]
            segments.pop(0)
            segments.append(a)
            segments[0].append(neighbor)

        forbidden.append(current)
        current = neighbor

    return segments

g = goth_rough_everything(x_y, centers= 3)
print(g)
for i in g:
    if len(i) > 0:
        k = list(zip(*i))
        print(k)

        plt.plot(k[0], k[1])
plt.show()
































