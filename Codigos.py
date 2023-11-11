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



    #Genera las |J| tiendas ya instaladas
    TiendasYaInstaladas = []
    for n in range(1, TamañoTiendasYaInstaladas, 1):            
        (x,y) = (random.randint(226,375), random.randint(226,375))
        TiendasYaInstaladas.append((x,y))
    TiendasYaInstaladas.sort


    #Ahora hay que calcular h_ij, el peso total de x_ij, i.e. de asignar i a j
    Dist = np.zeros((600,600))
    i = 1
    for x in range(1,600,1):
        for y in range(1,600,1):
            if (abs(x-300.5)>=75.5) & (abs(y-300.5)>=75.5): #i.e., están fuera de la zona gris
                j=1
                for z in TiendasYaInstaladas:
                    Dist[i-1][j-1] = ((x-z[0])**2+(y-z[1])**2)**(1/2)
                    j+=1
        i+=1
    i+=1

    MatricesDeCostos.append(Dist)
    print(MatricesDeCostos)