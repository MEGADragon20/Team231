from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math
import numpy as np

exampleCenters = 3
exampleNSamples = 75
x_y, c = make_blobs(cluster_std = 0.6, n_samples= exampleNSamples, centers= exampleCenters)
#print(x_y, c)

plt.scatter(x_y[:, 0], x_y[:, 1], c=c)

def biggest_growth_div(l: list[int]):
    last_value = None
    current_max_growth = -np.inf
    value = None
    for i in l:
        if last_value != None:
            if current_max_growth  <= i/last_value:
                current_max_growth = i/last_value
                value = i
        last_value = i
    return value

def biggest_growth_sub(l: list[int]):
    alle = []
    last_value = None
    current_max_growth = -np.inf
    value = None
    for i in l:
        if last_value!= None:
            if current_max_growth  <= i-last_value:
                current_max_growth = i-last_value
                alle.append(i-last_value)
                value = i
        last_value = i
    print(alle, "sss     ", value, "   s ss s s s",current_max_growth)
    return value

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
    fb = []
    current = array[0]
    a = 0
    while len(array) > len(fb):
        print(a)
        a += 1
        neighbor, distance = find_nearest_neighbor(current, array, fb)
        distances.append(distance)
        fb.append(current)
        current = neighbor

    distances.sort()
    print(distances)
    filtervalue = distances[-(exampleCenters-1)]


    current = array[0]
    segments = []
    forbidden = []
    for i in range(centers):
        segments.append([])
    current_segment = 0
    while len(array) > len(forbidden)/2:
        neighbor, distance = find_nearest_neighbor(current, array, forbidden)
        if distance <= filtervalue:
            segments[current_segment].append(neighbor)
        else:
            if current_segment +1 < len(segments):
                current_segment += 1
                segments[current_segment].append(neighbor)
            else:
                break

        forbidden.append(current)
        current = neighbor
    return segments
g = goth_rough_everything(x_y, centers= 3)

for i in g:
    if len(i) > 1: 
        k = list(zip(*i))
        plt.plot(k[0], k[1])


plt.show()




























