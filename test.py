import numpy as np

M = [[],[],[],[],[],[],[],[],[],[]]

###

M[0] = [(4, 17), (17, 4)]
M[1] = [(8, 17), (17, 8)]
M[2] = [(12, 17), (17, 12)]
M[3] = [(17, 18), (18, 17)]
M[4] = [(14, 19), (17, 14), (19, 17)]
M[5] = [(1, 17), (13, 1), (17, 13)]
M[6] = [(7, 17), (17, 7)]
M[7] = [(16, 17), (17, 16)]
M[8] = [(15, 20), (17, 15), (20, 17)]
M[9] = [(2, 21), (3, 9), (5, 11), (6, 2), (9, 17)
, (10, 5), (11, 3), (17, 6), (21, 10)]

###

var = 0
for i in range(1,11,1):
    if len(M[i-1]) != 0:
        var+=1

for i in range(1,var+1,1):
    Matriz = {}
    for j in M[i-1]:
        inicio = j[0]
        final = j[1]
        Matriz[inicio] = final


    x = M[i-1][0][0]

    for n in range(len(M[i-1])):
        y = Matriz[x]

        #print("("+str(x)+","+str(y)+")")
        del Matriz[x]
        x = y
    if len(Matriz) > 0:
        print("Oh no!")
    elif len(Matriz) == 0:
        print("wena!")