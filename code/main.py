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

def p_way_merge_driver(mem_size, k_pages, n_runs, keys):
    max_tam_runs = len(keys)//mem_size #n/m
    # if(alg == "B"):
    #     k_pages = k_pages/2
    
    runs = []
    i = 0
    j = 0
    max_list = max_tam_runs
    while j < n_runs:                   ## pega somente a r sequencias iniciais. o restante é descartado
        inner_list = keys[i:max_list]   ##pegando os elementos da runs de tamanho maximo n/m
        runs.append(inner_list)
        i = i + max_tam_runs
        max_list = max_list + max_tam_runs
        j = j + 1

    print(runs)
    for i in range(n_runs):
        heapsort(runs[i])

    for i in range(n_runs):
        #p_way_merge()
    
    print(runs)
    return runs

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

#show_data_debug(params)
#show_data_debug(keys)
#heapsort(keys)
show_data_debug(keys)
runs = p_way_merge_driver(params[0], params[1], params[2], keys)
#show_data_debug(runs)
#p_way_merge(params)
