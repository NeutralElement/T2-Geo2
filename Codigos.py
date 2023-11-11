import random
import numpy as np

TablaDeInstancias = [((3,6),(11,20))]#, ((7,11),(11,20)), 
                    #((12,15),(11,20)), ((12,15),(20,29)), 
                    #((15,18),(20,29)),((19,23),(20,29)),
                    #((19,23),(26,35)),((24,28),(26,35))]

CostoInstalacionCeleste = random.randint(1000,1500)
CostoInstalacionVerde = random.randint(1500,4000)

EmisionesPorOperacion = random.randint(20,70)

MatricesDeCostos = []

for (t1,t2) in TablaDeInstancias:
    TamañoUbicacionesPosibles = random.randint(t1[0],t1[1])
    TamañoTiendasYaInstaladas = random.randint(t2[0],t2[1])

    #Ahora hay que calcular h_ij, el peso total de x_ij, i.e. de asignar i a j
    Dist = np.zeros[(600,600)]
    i = 1
    j = 1
    for x in range(1,600,1):
        for y in range(1,600,1):
            if (abs(x-300.5)>75) & (abs(y-300.5)>75): #i.e., están fuera de la zona gris
                for (x2) in range (226,375,1):
                    for (y2) in range (226,375,1):
                        Dist[i][j] = ((x-x2)**2+(y-y2)**2)**(1/2)
                    j+=1
                j+=1
        i+=1
    i+=1

    MatricesDeCostos.append(Dist)