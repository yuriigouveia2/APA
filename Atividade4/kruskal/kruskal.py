#Função que lê arquivo de entrada e gera o os vertices com o peso (grafo)
def carregaLista():
    arquivo = None
    while arquivo is None:
        arquivoEntrada = input("Digite o nome do arquivo (com a extensão): ")
        try:
            arquivo = open(arquivoEntrada, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    conteudoEntrada = arquivo.readlines()

    numNos = conteudoEntrada[0]
    listaCarregada = [[0]]*(int(numNos))
    listaAux = [[0]]*(int(numNos))

    # quebra a string de entrada em uma lista de numeros
    for i in range(0, int(numNos)-1):
        listaCarregada[i] = conteudoEntrada[i+1].split()

    aux = []
    for i in range(0, int(numNos) - 1):
        aux.clear()
        n = i
        for j in range(0, len(listaCarregada[i])):
            aux.append([i ,n + 1, int(listaCarregada[i][j])])
            n = n+1
        listaAux[i] = aux.copy()

    listaFinal = []
    for i in range(0, len(listaAux) - 1):
        for j in range(0, len(listaAux[i])):
            listaFinal.append(listaAux[i][j])

    return numNos, listaFinal.copy()

##############################################

#Encontra o elemento na árvore
def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

#Une dois subsets de uma árvore
def union(parent, rank, x, y):
    raixX = find(parent, x)
    raixY = find(parent, y)

    if rank[raixX] < rank[raixY]:
        parent[raixX] = raixY
    elif rank[raixX] > rank[raixY]:
        parent[raixY] = raixX

    else:
        parent[raixY] = raixX
        rank[raixX] += 1


#Algoritmo de Kruskal, que rece como parâmetros a quantidade de nós e o grafo
def kruskal(numNos, grafo):
    numNos = int(numNos)
    mstFinal = []  # Array que guarda a mst final

    listaLigacoes = 0  # Index usado para percorrer todas as ligações do grafo ordenado
    noMst = 0  # Index usado para saber quando a mst foi preenchida completamente (todos os nós)

    # Ordena o grafo em ordem crescente de peso das arestas
    grafo = sorted(grafo, key=lambda item: item[2])

    nos = [];
    altura = []

    # Preenche a variável nos com todos os nós do grafo (cada um representa uma árvore de altura 0)
    for no in range(numNos):
        nos.append(no)
        altura.append(0)

    # Número de arestas que a mst deve possuir (quantidade de nós do grafo - 1)
    while noMst < numNos - 1:

        # Escolhe o primeiro nó e incrementa
        u, v, w = grafo[listaLigacoes]
        listaLigacoes = listaLigacoes + 1

        # retorna o nó pai da sub-árvore correspondente dos nós x e y
        x = find(nos, u)
        y = find(nos, v)

        # verifica se o nó pai das sub-árvores é o mesmo (se for igual, a união das árvores gera um ciclo)
        if x != y:
            noMst = noMst + 1
            mstFinal.append([u, v, w])
            union(nos, altura, x, y)

    resultado = 0
    for u, v, custo in mstFinal:
        resultado = resultado + custo

    print("Resultado: " + str(resultado))
################################################
################### EXECUÇÃO ###################
################################################
[nos, grafo] = carregaLista();

kruskal(nos, grafo);
