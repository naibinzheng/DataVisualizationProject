__author__ = 'Naibin Zheng'
from random import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd
from scipy.spatial import distance as ed
import math
from operator import sub
from operator import add

def main():
    w = []
    for i in range(20):
        row = []
        for j in range(20):
            v = []
            for k in range(12):
                v.append(random())
            row.append(v)
        w.append(row)

    print (w)


    chord = pd.read_csv("../../../data/chords.csv")
    matrix = chord.as_matrix(columns=chord.columns[1:13])
    print (chord)

    #Cmajor = chord['CM']
    #print (Cmajor)

    p = 20
    c = 20


    #distance function
    def distance(a, b, c, d):
        dx = abs(a-c)
        dy = abs(b-d)
        if dx > 10:
            dx = p - dx
        if dy > 10:
            dy = p - dy
        d = dx**(2) + dy**(2)
        return d

    #algorithm code
    for s in range(1,2):
        for t in range(24):
            mini_dis = float("inf")
            r = matrix[(randint(0, 23)), :]
            #print(r)
            for i in range(20):
                for j in range(20):
                    #print (w[i][j])
                    dis = ed.euclidean(w[i][j], r)
                    #print(dis)
                    if dis < mini_dis:
                        mini_dis = dis
                        bmi = i
                        bmj = j
            for k in range(1, p+1):
                for l in range(1, p+1):
                    #print(w[k-1][l-1])
                    h = (p -1 - (s/c))/3
                    q = math.e**(-(distance(bmi, bmj, k, l)/(2*h**2)))
                    subr = list(map(sub, r, w[k-1][l-1]))
                    #print(w[k-1][l-1])
                    for e in range(len(subr)):
                        subr[e] = subr[e] * h *q
                    w[k-1][l-1] = list(map(add, w[k-1][l-1], subr))
                    #print(w[k-1][l-1])
                    #print(h*q)


    #find the similarity grid


    #generate the distrabut matirx for fig1
    c = []
    for i in range(20):
        v=[]
        for j in range(20):
            v.append('x')
        c.append(v)
    print(c)

    #display the figur1
    for i in range(20):
        for j in range(20):
            plt.text(i, j, c[i][j], ha='center',va='center')
    plt.xlim(-0.25, 19.5)
    plt.ylim(-0.25, 19.5)

    plt.show()







            #print (r)








if __name__ == '__main__':
    main()
