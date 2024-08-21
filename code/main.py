from sys import argv
from struct import *



def read_input_data():
    filename = argv[1] #argumento passado via CLI
    with open(filename) as f: #abrindo o arquivo e extraindo parametros
        data = f.readlines()
    f.close()

    # organizando parâmetros a serem usados
    alg = data[0]                          #char que indica o algoritmo
    params = list(data[1].split(" "))      #parametros da funçao -> m, k, r, n
    keys = list(data[2].split(" "))        #elementos a serem ordenados

    return params

def p_way_merge(mem_size, k_files, runs, num_elements):
    


########## DEBUG #############
def show_data_debug(elems = None, var = None):
    print("Elementos do array")
    if(elems):
        for elem in elems:
            print(elem)

    print("Variavel")
    print(var)


params = read_input_data()

p_way_merge(params)
