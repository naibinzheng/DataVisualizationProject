__author__ = 'Naibin Zheng'
from random import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance as ed
import math
from operator import sub
from operator import add
from sklearn.metrics.pairwise import cosine_similarity
import sys

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
    label = chord['Label']
    matrix = chord.as_matrix(columns=chord.columns[1:13])
    #print (label)

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
    for s in range(1,361):
        for t in range(24):
            mini_dis = float("inf")
            bmi = float("inf")
            bmj= float("inf")
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

    print(w)


    #generate the distrabut matirx for fig1
    fig =plt.figure()

    for t in range(24):
        max_cs = -1
        r = matrix[t, :]
        print(r)
        chord_letter = label[t]
        for i in range(20):
            for j in range(20):
                #find the similarity grid
                cs = cosine_similarity(w[i][j], r)
                if cs > max_cs:
                    max_cs = cs
                    bmi = i
                    bmj = j
        plt.text(bmi, bmj, chord_letter, ha='center',va='center')

    plt.xlim(-0.6, 19.4)
    plt.ylim(-0.6, 19.4)
    plt.title('Fig1 VAMSOM')

    fig.savefig('music_som.png')

    #generate fig2
    fig =plt.figure()
    CM = matrix[0,:]
    print (CM)
    CMfig = np.zeros((20, 20))

    for i in range(20):
        for j in range(20):
            CMfig[i][j] = np.dot(np.array(CM), np.array(w[i][j]))
    plt.imshow(CMfig, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title('Fig2 heatmap of CM')

    fig.savefig('music_som_CM.png')

    #generate fig3
    fig =plt.figure()
    cm = matrix[12,:]
    CMfig = np.zeros((20, 20))
    for i in range(20):
        for j in range(20):
            CMfig[i][j] = np.dot(np.array(cm), np.array(w[i][j]))
    plt.imshow(CMfig, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title('Fig3 heatmap of Cm')
    fig.savefig('music_som_Cm.png')

    plt.show()






if __name__ == '__main__':
    main()
