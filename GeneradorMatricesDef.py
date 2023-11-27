import os
import random
import numpy as np

import time
start_time = time.time()                #Registrará el tiempo total que tarda en generar todas las instancias.


NombresArchivos = []                            #
                                                #
for i in range(1,9,1):                          #
    nombre = "instancia_"+str(i)+".dat"         #   Crea el nombre que tendran las 8 instancias, en orden
    NombresArchivos.append(nombre)              #   creciente de tamaños, y borra las instancias anteriores
                                                #   antes de generar las nuevas
for i in range(1,9,1):                          #
    if os.path.exists(NombresArchivos[i-1]):    #
        os.remove(NombresArchivos[i-1])         #




TablaDeInstancias = [((3,6),(11,20)), ((7,11),(11,20)), 
                    ((12,15),(11,20)), ((12,15),(20,29)), 
                    ((15,18),(20,29)),((19,23),(20,29)),
                    ((19,23),(26,35)),((24,28),(26,35))]

CantidadDeInstancias = len(TablaDeInstancias)

MatricesDeCostosDeInstalacion = []          #
MatricesDeEmisionesOperacionales = []       #   Estas matrices servirán al final del generador,
MatricesDeCapacidades = []                  #   sirviéndonos como almacén de los datos para cada
MatricesDeDistancias = []                   #   instancia.
ListaIJ = []                                #

for (t1,t2) in TablaDeInstancias:
    TamañoUbicacionesPosibles = random.randint(t1[0],t1[1]) # i.e., |I|.
    TamañoTiendasYaInstaladas = random.randint(t2[0],t2[1]) # i.e., |J|.

    TiendasYaInstaladas = []                                        #
    for n in range(1, TamañoTiendasYaInstaladas+1, 1):              #   Generamos las |J| tiendas 
        (x,y) = (random.randint(226,375), random.randint(226,375))  #   instaladas.
        TiendasYaInstaladas.append((x,y))                           #
    
    UbicacionesPosibles = []                                 
    for n in range(1, TamañoUbicacionesPosibles+1, 1):      #     
        x = random.randint(1,600)                           #   Generamos los |I| lugares posibles
        if (abs(x-300.5)>=75.5):                            #   para las warehouses. 
            y = random.randint(1,600)                       #
        else:                                               #
            if random.randint(0,1):                         #
                y = random.randint(1,225)                   #
            else:                                           #
                y = random.randint(376,600)                 #
        UbicacionesPosibles.append((x,y))                   #
        
    #Reordena las listas de izquierda a derecha, de abajo hacia arriba (explicación en PDF).        
    TiendasYaInstaladas.sort(key = lambda tup: (tup[0], tup[1]))
    UbicacionesPosibles.sort(key = lambda tup: (tup[0], tup[1])) 



    Distancia = np.zeros((TamañoUbicacionesPosibles,TamañoTiendasYaInstaladas)) #
    CostoInstalacion = np.zeros(TamañoUbicacionesPosibles)                      #   Se calculan los distintos
    EmisionesOperacion = np.zeros(TamañoUbicacionesPosibles)                    #   parámetros necesarios para
    Capacidad = np.zeros(TamañoUbicacionesPosibles)                             #   AMPL.
    



    i = 1   
    for (x,y) in UbicacionesPosibles:                                   #   Este "for" busca calcular los 
        j=1                                                             #   parámetros por cada ubicación  
        for z in TiendasYaInstaladas:                                   #   posible, digase, calcula los
            Distancia[i-1][j-1] = abs(x-z[0])+abs(y-z[1])               #   costos de instalación, la ca-
            j+=1                                                        #   pacidad y las emisiones por 
                                                                        #   operación asociadas a la posición
        if (abs(x-300.5)>=200.5) or (abs(y-300.5)>=200.5):              #   i-ésima, las cuales se indexan
            #i.e., están en la zona celeste                             #   según un cierto orden que se
            CostoInstalacion[i-1] = random.randint(1000,1500)           #   describe en el informe, además de
        else:                                                           #   calcularse todas las distancias
        #i.e., estamos en la zona verde                                 #   entre el warehouse i-ésimo y
            CostoInstalacion[i-1] = random.randint(1500,4000)           #   las tiendas j.
                                                                        #
        Capacidad[i-1] = random.randint(2,TamañoTiendasYaInstaladas//2) #
        EmisionesOperacion[i-1] = random.randint(20,70)                 #  

        i+=1
    MatricesDeCostosDeInstalacion.append(CostoInstalacion)              #   Todos estos parámetros se almacenan
    MatricesDeEmisionesOperacionales.append(EmisionesOperacion)         #   por instancia, en orden.
    MatricesDeCapacidades.append(Capacidad)                             #
    MatricesDeDistancias.append(Distancia)                              #
    ListaIJ.append((TamañoUbicacionesPosibles,TamañoTiendasYaInstaladas))


def escribir_indexados(conjunto, nombre_conjunto, archivo): #
    archivo.write(nombre_conjunto+':=\n')                   #   Función auxilar que ayuda a escribir compactamente
    for i, valor in enumerate(conjunto, 1):                 #   los parámetros 1 dimensionales en el .dat, con la
        archivo.write(f'{i} {valor}\n')                     #   estructura que necesita AMPL.
    archivo.write(';\n\n')                                  #

def escribir_matriz(conjunto, nombre_conjunto, archivo):    #
    largo = len(conjunto[0])                                #   Este otro código también busca lo mismo que el
                                                            #   anterior, pero para el caso particular de las 
    archivo.write(nombre_conjunto+':\n')                    #   distancias entre la warehouse i y la tienda j,
    for j in range(1,largo+1, 1):                           #   parámetros que son 2-dimensionales (depende de
        if j==1:                                            #   i y j a la vez).
            archivo.write("\t")                             #
        archivo.write(str(j)+"\t")                          #
    archivo.write(":=\n")                                   #
                                                            #
    for i, valor in enumerate(conjunto, 1):                 #
        archivo.write(f"{i}")                               #
        for j in range(1,largo+1,1):                        #  
            archivo.write(f'\t{valor[j-1]}')                #
        archivo.write("\n")                                 #
    archivo.write(';\n\n')                                  #


for i in range (1,CantidadDeInstancias+1,1):                                        #
    archivo_i = open(NombresArchivos[i-1], "w")                                     #   Esta parte final del código, una vez ya
                                                                                    #   terminado la creación de todos los datos
    archivo_i.write("param cardI := "+str(ListaIJ[i-1][0])+";\n")                   #   para todas las instancias, simplemente va
    archivo_i.write("param cardJ := "+str(ListaIJ[i-1][1])+";\n\n")                 #   y crea cada .dat con sus respectivos datos,
                                                                                    #   en el orden y formatos deseados.
    escribir_indexados(MatricesDeCostosDeInstalacion[i-1], "param CI", archivo_i)   #
                                                                                    #       
    escribir_matriz(MatricesDeDistancias[i-1], "param d", archivo_i)                #
                                                                                    #
    escribir_indexados(MatricesDeEmisionesOperacionales[i-1], "param O", archivo_i) #
    escribir_indexados(MatricesDeCapacidades[i-1], "param C", archivo_i)            #
                                                                                    #
    archivo_i.close()                                                               #
print(" %s segundos ---" % (time.time() - start_time))