set N = {1..21};
set K = {1..m};

param d{i in N, j in N}; 	#distancia de i a j
param t{i in N, j in N};	#tiempo de i a j

var X{i in N, j in N, k in K} binary;
var D;

########################################################################################

minimize FO:
				sum{i in N, j in N, k in K: i!=j}(t[i,j]*X[i,j,k])
########################################################################################				


s.t. a	{i in N, k in K}:	sum{j in N: j != i} X[i,j,k] - sum{j in N: i != i} X[j,i,k] = 0;
s.t. b	{i in N, k in K}:	sum{j in N: j != i} X[i,j,k] = 1;

s.t. c			{k in K}:	sum{}X[i,j,k] = 1

s.t. d					: 	D = sum{i in N, j in N, k in K: i!=j}(X[i,j,k]*d[i,j]) #Calcula la distancia total recorrida