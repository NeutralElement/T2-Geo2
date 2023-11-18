import os
import random
import numpy as np

NombresArchivos = []

for i in range(1,9,1):
    nombre = "instancia_"+str(i)+".dat"
    NombresArchivos.append(nombre)

for i in range(1,9,1):
    if os.path.exists(NombresArchivos[i-1]):
        os.remove(NombresArchivos[i-1])




TablaDeInstancias = [((3,6),(11,20)), ((7,11),(11,20)), 
                    ((12,15),(11,20)), ((12,15),(20,29))] 
                    #((15,18),(20,29)),((19,23),(20,29)),
                    #((19,23),(26,35)),((24,28),(26,35))]

CantidadDeInstancias = len(TablaDeInstancias)

#CostoInstalacionCeleste = random.randint(1000,1500)
#CostoInstalacionVerde = random.randint(1500,4000)

#EmisionesPorOperacion = random.randint(20,70) Usar si es que fueran globales

MatricesDeCostosDeInstalacion = []
MatricesDeEmisionesOperacionales = []
MatricesDeCapacidades = []
MatricesDeDistancias = []
ListaIJ = []

for (t1,t2) in TablaDeInstancias:
    TamañoUbicacionesPosibles = random.randint(t1[0],t1[1])
    TamañoTiendasYaInstaladas = random.randint(t2[0],t2[1])


    #Genera las |J| tiendas ya instaladas
    TiendasYaInstaladas = []
    for n in range(1, TamañoTiendasYaInstaladas+1, 1):            
        (x,y) = (random.randint(226,375), random.randint(226,375))
        TiendasYaInstaladas.append((x,y))
        
    #Reordena de izquierda a derecha, de abajo hacia arriba.        
    TiendasYaInstaladas.sort(key = lambda tup: (tup[0], tup[1])) 

    #Ahora hay que calcular h_ij, el peso total de x_ij, i.e. de asignar i a j
    Distancia = np.zeros((337500,TamañoTiendasYaInstaladas))
    CostoInstalacion = np.zeros(337500) 
    EmisionesOperacion = np.zeros((337500,TamañoTiendasYaInstaladas)) 
    Capacidad = np.zeros(337500)
    
    #337500 = 600^2-150^2

    i = 1
    for x in range(1,600+1,1):
        for y in range(1,600+1,1):
            j=1
            if (abs(x-300.5)>=75.5) or (abs(y-300.5)>=75.5): #i.e., están en la zona verde (contiene a la celeste)
                for z in TiendasYaInstaladas:
                    if y > 1:
                        
                        if (abs(x-300.5)>=200.5) or (abs(y-300.5)>=200.5): #i.e., están en la zona celeste
                            CostoInstalacion[i-1] = random.randint(1000,1500)
                        else:                                              #i.e., estamos en la zona verde
                            CostoInstalacion[i-1] = random.randint(1500,4000)
                        
                        Capacidad[i-1] = random.randint(2,TamañoTiendasYaInstaladas//2)
                    
                    Distancia[i-1][j-1] = ((x-z[0])**2+(y-z[1])**2)**(1/2)
                    EmisionesOperacion[i-1][j-1] = random.randint(20,70)

                    j+=1
                i+=1
    MatricesDeCostosDeInstalacion.append(CostoInstalacion)
    MatricesDeEmisionesOperacionales.append(EmisionesOperacion)
    MatricesDeCapacidades.append(Capacidad)
    MatricesDeDistancias.append(Distancia)
    ListaIJ.append((TamañoUbicacionesPosibles,TamañoTiendasYaInstaladas))


def escribir(conjunto, nombre_conjunto):
    archivo_i.write(nombre_conjunto+':=\n')
    for i, valor in enumerate(conjunto, 1):
        archivo_i.write(f'{i} {valor}\n')
    archivo_i.write(';\n\n')   

for i in range (1,CantidadDeInstancias+1,1):
    archivo_i = open(NombresArchivos[i-1], "w")
    
    archivo_i.write("wola tarola"+str(i)+" "+str(random.randint(1,100)))
    
    
    archivo_i.close()