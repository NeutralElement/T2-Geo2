param m;					#	Cantidad de viajes.

set N = {1..21};			#	Conjunto de nodos, indexados alfabeticamente, i.e:
							#	Berlin = 3.
							#	Dublin = 8.
							#	Hamburgo = 9.
							#	kiev = 11.
							#	Madrid = 13.
							#	Moscu = 15.
							# 	Paris = 17.
							#	SPB = 20.

set K = {1..m};				#	Conjunto de rutas, ya indexadas.

param p := 20-(m-1);		#	Cantidad maxima de nodos visitables por una sola
							#	ruta. Esta cantidad se usa en las condiciones de MT.
param d{i in N, j in N}; 	#	Distancia de i a j.
param t{i in N, j in N};	#	Tiempo de i a j.

var X{i in N, j in N, k in K: i!=j} binary; 	#	Variable si la ruta k pasa desde i a j.
var D >= 0;										#	Variable que almacena la distancia total recorrida.	
var U{i in N, k in K: i!= 17} >= 0;				#	Variable de las restricciones de MT.

########################################################################################

minimize FO:
				sum{i in N, j in N, k in K: i!=j}(t[i,j]*X[i,j,k]);

########################################################################################				


s.t. Divergencia   		  	{i in N, k in K}:	sum{j in N: j != i} X[i,j,k] - sum{j in N: j != i} X[j,i,k] = 0;
s.t. SeRecorreTodo  	 	 {i in N: i!=17}:	sum{j in N, k in K: j != i} X[i,j,k] = 1;
s.t. TodosSalenDeParis		   		{k in K}:	sum{j in N: j != 17} X[17,j,k] = 1;
s.t. EliminarSubTur	 {i in N, j in N, k in K: 
				   i!=17 and j!=17 and j!=i}:	U[i,k] - U[j,k] + p*X[i,j,k] <= p-1;

s.t. MadridDublin				: sum{k in K} (X[13,8,k] + X[8,13,k]) = 0;
s.t. MoscuSPB_Kiev				: sum{k in K} (X[15,11,k] + X[20,11,k]) = 0;
s.t. Kiev_BerlinHamb			: sum{k in K, j in N: j!=3 and j!=9 and j!= 11} X[11,j,k] = 0;


s.t. DistanciaTotalRecorrida	: D = sum{i in N, j in N, k in K: i!=j}(X[i,j,k]*d[i,j]);