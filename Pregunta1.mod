param cardI;
param cardJ;

set I = {1..cardI}; #Ubicaciones posibles
set J = {1..cardJ}; #Tiendas ya instaladas

param CI{i in I};			#costo de instalación de i
param d{i in I, j in J}; 	#distancia de i a j
param O{i in I}; 			#emisiones por operación
param C{i in I};			#Capacidad de lugar i

var X{i in I, j in J} binary;
var Y{i in I} binary;

########################################################################################

minimize FO:
				sum{i in I, j in J}(1.5*d[i,j]*X[i,j]) +
				sum{i in I}(O[i]*Y[i]) 
########################################################################################				


s.t. a		{i in I}: 	sum{j in J}X[i,j] <= C[i]Y[i];
s.t. b					sum{i in I, j in J}(1.25*d[i,j]*X[i,j]) + sum{i in I}(CI[i]*Y[i]) <= 6000*cardJ;
s.t. c		{j in J}:	sum{i in I} X[i,j] = 1;			#Satisfacción de demanda por único elemento