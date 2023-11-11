import random
import numpy as np

TablaDeInstancias = [((3,6),(11,20))]#, ((7,11),(11,20)), 
                    #((12,15),(11,20)), ((12,15),(20,29)), 
                    #((15,18),(20,29)),((19,23),(20,29)),
                    #((19,23),(26,35)),((24,28),(26,35))]

CostoInstalacionCeleste = random.randint(1000,1500)
CostoInstalacionVerde = random.randint(1500,4000)

#EmisionesPorOperacion = random.randint(20,70) Usar si es que fueran globales

MatricesDeCostos = []
MatricesDeEmisiones = []

for (t1,t2) in TablaDeInstancias:
    TamañoUbicacionesPosibles = random.randint(t1[0],t1[1])
    TamañoTiendasYaInstaladas = random.randint(t2[0],t2[1])


    #Genera las |J| tiendas ya instaladas
    TiendasYaInstaladas = []
    for n in range(1, TamañoTiendasYaInstaladas, 1):            
        (x,y) = (random.randint(226,375), random.randint(226,375))
        TiendasYaInstaladas.append((x,y))
        
    #Reordena de izquierda a derecha, de abajo hacia arriba.        
    TiendasYaInstaladas.sort(key = lambda tup: (tup[0], tup[1])) 



    #Ahora hay que calcular h_ij, el peso total de x_ij, i.e. de asignar i a j
    Dist = np.zeros((600,600))
    Emis = np.zeros((600,600))
    C_Inst = np.zeros((600,600))
    Capacidad = np.zeros((600,600))


    i = 1
    for x in range(1,600,1):
        for y in range(1,600,1):
            j=1
            for z in TiendasYaInstaladas:
                if (abs(x-300.5)>=200.5) & (abs(y-300.5)>=200.5): #i.e., están en la zona celeste
                    C_Inst[i-1][j-1] = random.randint(1000,1500)
                if (abs(x-300.5)>=75.5) & (abs(y-300.5)>=75.5): #i.e., están en la zona verde (contiene a la celeste)
                    if C_Inst[i-1][j-1] == 0:
                        C_Inst[i-1][j-1] = random.randint(1500,4000)
                    Dist[i-1][j-1] = ((x-z[0])**2+(y-z[1])**2)**(1/2)
                    Capacidad[i-1][j-1] = random.randint(2,TamañoTiendasYaInstaladas/2)
                    Emis[i][j] = random.randint(20,70) + 1.5*Dist[i-1][j-1]
                j+=1 
            i+=1
        i+=1

    MatricesDeCostos.append(Dist)
    #print(MatricesDeCostos)