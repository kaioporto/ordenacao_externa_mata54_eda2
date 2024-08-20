from sys import argv
from struct import *

##pega o nome do arquivo de entrada dado na linha de comando
filename = argv[1]

##abrindo arquivo e extraindo parametros
with open(filename) as f:
    data = f.readlines()
f.close()


## Setando parâmetros a serem usados
alg = data[0]               #char que indica o algoritmo
params = list(data[1].split(" "))      #parametros da funçao -> m, k, r, n
keys = list(data[2].split(" "))        #elementos a serem ordenados

#parametros da funçao
mem_size = params[0]
k_files = params[1]
runs = params[2]
num_registros = params[3]



## Criando as runs iniciais



########## DEBUG #############
#print(type(alg))
#print(alg)
#print("elementos")
#for elem in keys:
#    print(elem)
#print("parametros")
#for i in params:
#    print(i)

## 


