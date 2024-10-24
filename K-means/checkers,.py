from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math
import numpy as np

exampleCenters = 1
exampleNSamples = 25
x_y, c = make_blobs(cluster_std = 1, n_samples= exampleNSamples, centers= exampleCenters)
#print(x_y, c)

plt.scatter(x_y[:, 0], x_y[:, 1], c=c)

def max_distance_in_segment(seg):
    if len(seg) < 5:
        return 0
    current_max = 0
    for i in seg:
        for j in seg:
            if abstand_berechnen([i, j]) > current_max:
                current_max = abstand_berechnen([i, j])
    return current_max

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
def x_is_not_in_y(x,y) -> bool:
    for i in y:
        if i[0] == x[0] and i[1] == x[1]:
            return False
    return True


def generate_chain(array):
    chains = []
    print(len(array))
    for i in range(25):
        current = array[i]
        chain = []
        boo = True
        while boo:
            a = find_nearest_neighbor(current, array, [current])[0]
            if x_is_not_in_y(a,chain):
                chain.append(a)
            else:
                boo = False
            current = a
        print("d",chain)
        chains.append(chain)
    return chains

def goth_rough_everything(array, centers):
    return [generate_chain()]
        

                

g = generate_chain(x_y)
print(g)
for i in g:
    if len(i) >= 1: 
        k = list(zip(*i))
        plt.plot(k[0], k[1])


plt.show()

