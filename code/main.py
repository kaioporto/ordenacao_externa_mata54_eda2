from sys import argv
import heapq

def read_input_data():
    filename = argv[1]  # argumento passado via CLI
    with open(filename) as f:  # abrindo o arquivo e extraindo parâmetros
        data = f.readlines()
    f.close()

    # organizando parâmetros a serem usados
    alg = data[0].strip()  # char que indica o algoritmo (não utilizado diretamente aqui)
    params = list(map(int, data[1].split()))  # parametros da função -> m, k, r, n
    keys = list(map(int, data[2].split()))  # elementos a serem ordenados

    return params, keys

def heapify(elems, n, i):
    maior = i
    filho_esquerdo = 2*i+1
    filho_direito = 2*i+2

    if filho_esquerdo < n and elems[maior] < elems[filho_esquerdo]:
        maior = filho_esquerdo

    if filho_direito < n and elems[maior] < elems[filho_direito]:
        maior = filho_direito

    if maior != i:
        elems[i], elems[maior] = elems[maior], elems[i]  # troca

        # heapifica a raiz
        heapify(elems, n, maior)

def heapsort(elems):
    n = len(elems)

    for i in range(n//2 - 1, -1, -1):  # do final pro início
        heapify(elems, n, i)

    for i in range(n-1, 0, -1):
        elems[i], elems[0] = elems[0], elems[i]

        heapify(elems, i, 0)

def p_way_merge_driver(mem_size, k_pages, n_runs, keys):
    max_tam_runs = len(keys) // mem_size  # n/m
    
    runs = []
    i = 0
    j = 0
    num_writes = 0
    max_list = max_tam_runs
    while j < n_runs:  # pega somente as r sequências iniciais. o restante é descartado
        inner_list = keys[i:max_list]  # pegando os elementos das runs de tamanho máximo n/m
        runs.append(inner_list)
        #calculo da B(m,j)
        num_writes = num_writes + len(inner_list)

        i = i + max_tam_runs
        max_list = max_list + max_tam_runs
        j = j + 1

    beta_de_m_j = (num_writes)/(n_runs * mem_size)
    
    print("fase 0 %.2f" % round(beta_de_m_j, 2), end=" ")
    for i in range(n_runs):
        heapsort(runs[i])  # Ordena cada run individualmente

    for i in range(n_runs):
        print(runs[i])
    print("1:", runs)

    # Intercalar as runs ordenadas
    merged_output = p_way_merge(runs, k_pages)
    #print("Resultado da intercalação:", merged_output)
    return merged_output

def p_way_merge(runs, k_pages):
    heap = []
    result = []
    
    # Inicializa a heap com o primeiro elemento de cada run
    for i in range(len(runs)):
        if runs[i]:  # Verifica se a run não está vazia
            heapq.heappush(heap, (runs[i][0], i, 0))  # (valor, índice da run, índice do elemento dentro da run)
    

    # Executa o processo de intercalação
    while heap:
        val, run_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Adiciona o próximo elemento da mesma run à heap
        if elem_idx + 1 < len(runs[run_idx]):
            heapq.heappush(heap, (runs[run_idx][elem_idx + 1], run_idx, elem_idx + 1))

    return result

########## DEBUG #############
def show_data_debug(elems=None, var=None):
    print("Elementos do array")
    if elems:
        for elem in elems:
            print("%d" % int(elem), end=" ")
    
    if var:
        print("Variável")
        print(var)


params, keys = read_input_data()

# Realiza o processo de ordenação e intercalação
runs = p_way_merge_driver(params[0], params[1], params[2], keys)
