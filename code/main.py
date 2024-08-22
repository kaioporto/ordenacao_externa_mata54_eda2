from sys import argv
from struct import *

def read_input_data():
    filename = argv[1]          #argumento passado via CLI
    with open(filename) as f:   #abrindo o arquivo e extraindo parametros
        data = f.readlines()
    f.close()

    # organizando parâmetros a serem usados
    alg = data[0]                          #char que indica o algoritmo
    params = list(data[1].split(" "))      #parametros da funçao -> m, k, r, n
    keys = list(data[2].split(" "))        #elementos a serem ordenados
    
    #convertendo pra inteiro
    for i in range(len(params)):
        params[i] = int(params[i])

    #convertendo pra inteiro
    for i in range(len(keys)):
        keys[i] = int(keys[i])

    max_tam_runs = int(params[3])/int(params[1])
    if(alg == "B"):
        k_pages = params[1]/2
    

    return params, keys

def heapify(elems, n, i):
    maior = i
    filho_esquerdo = 2*i+1
    filho_direito = 2*i+2

    if(filho_esquerdo < n and elems[maior] < elems[filho_esquerdo]):
        maior = filho_esquerdo

    if(filho_direito < n and elems[maior] < elems[filho_direito]):
        maior = filho_direito

    if(maior != i):
        elems[i], elems[maior] = elems[maior], elems[i] #troca

        #pra raiz
        heapify(elems, n, maior) 

def heapsort(elems):
    n = len(elems)

    for i in range(n//2 - 1, -1, -1): #do final pro início
        heapify(elems, n, i)
    
    for i in range(n-1, 0, -1):
        elems[i], elems[0] = elems[0], elems[i]

        heapify(elems, i, 0)

def p_way_merge(mem_size, k_pages, runs, num_elements):
    i = 1
    j = 1
    k = 0
    while(i <= num_elements and j <= mem_size):
        k = k+1
        if(runs[i] < runs[j]):
            runs[k] = runs[i]
            i=i+1
        else:
            runs[k] = runs[j]
            j=j+1
    while(i < num_elements):
        k=k+1
        runs[k] = runs[i]
        i=i+1
    while(j < mem_size):
        k=k+1
        runs[k] = runs[j]
        j=j+1

def p_way_merge_driver(elems):
    pass

########## DEBUG #############
def show_data_debug(elems = None, var = None):
    print("Elementos do array")
    if(elems):
        for elem in elems:
            print("%d" % int(elem), end=" ")
    
    if(var):
        print("Variavel")
        print(var)


params, keys = read_input_data()

print("Parametros")
show_data_debug(params)
show_data_debug(keys)
heapsort(keys)
show_data_debug(keys)

#p_way_merge(params)
