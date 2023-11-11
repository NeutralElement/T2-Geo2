import random

TablaDeInstancias = [((3,6),(11,20)), ((7,11),(11,20)), 
                    ((12,15),(11,20)), ((12,15),(20,29)), 
                    ((15,18),(20,29)),((19,23),(20,29)),
                    ((19,23),(26,35)),((24,28),(26,35))]

for (x,y) in TablaDeInstancias:
    TamañoUbicacionesPosibles = random.randint(x[0],x[1])
    TamañoTiendasYaInstaladas = random.randint(y[0],y[1])
