from operator import itemgetter
import sys

def carregaMatriz():
    arquivo = None
    while arquivo is None:
        arquivoEntrada = input("Digite o nome do arquivo com a extensão: ")
        try:
            arquivo = open(arquivoEntrada, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    entrada = arquivo.readlines()

    numNos = entrada[0]
    listaCarregada = [[0]]*(int(numNos))
    listaAux = [[0]]*(int(numNos))
    matrizAux = [[0]]*(int(numNos))

    # quebra a string de entrada em uma lista de numeros
    for i in range(0, int(numNos)-1):
        listaCarregada[i] = entrada[i+1].split()

    aux = []
    for i in range(0, int(numNos)):
        aux.clear()
        n = i

        for j in range(0, len(listaCarregada[i])):
            if j == 0:
                aux.append([n + 1, 0])
            if listaCarregada[i][j] != 0:
                aux.append([n+2, int(listaCarregada[i][j])])
                n = n+1
        listaAux[i] = aux.copy()


    # completa listas (forma matriz quadrada)
    for i in range(0, int(numNos)):
        for j in range(0, len(listaAux[i])):
            if listaAux[i][j][1] == 0:
                continue
            if (listaAux[i][j][0] - 1) < i:
                continue
            listaAux[(listaAux[i][j][0] - 1)].append([i+1, listaAux[i][j][1]])

    for i in range(0, len(listaAux)):
        listaAux[i] = sorted(listaAux[i], key=itemgetter(0)).copy()

    # cria matriz auxiliar
    for i in range(0, len(listaAux)):
        aux.clear()
        for j in range(0, len(listaAux)):
            aux.append(listaAux[i][j][1])
        matrizAux[i] = aux.copy()

    return numNos, matrizAux.copy()
################################################

def dijkstra(numNos, origem, grafo):
    numNos = int(numNos)

    distancias = [sys.maxsize] * numNos  # array de distâncias do nó x para o nó origem
    distancias[origem] = 0                # da origem para origem a distância é zero
    visitado = [False] * numNos          # cria um array de nós visitados que auxilia na criação dos caminhos

    for i in range(numNos):                        # varre todos os nós do grafo
        u = minDistancia(numNos, distancias, visitado) # retorna a distância mínima dos nós ainda não visitados
        visitado[u] = True                          # e marca o nó com a distância mínima encontrada como visitado

        # atualiza a distância dos nós adjacentes sequenciais se a distância atual for maior que a distância nova
        # e se o nó em questão não tiver sido marcado previamente como visitado
        for v in range(numNos):
            if grafo[u][v] > 0 and visitado[v] == False and distancias[v] > distancias[u] + grafo[u][v]:
                distancias[v] = distancias[u] + grafo[u][v]

    printResultado(distancias[numNos-1])

def printResultado(distancia):
    print("Resultado: " + str(distancia))

def minDistancia(numNos, distancias, visitado):
    min = sys.maxsize   # inicializa variável com o maior valor possível para busca da menor distância

    for v in range(numNos):   # procura os nós com a menor distância que ainda não foram visitados
        if distancias[v] < min and visitado[v] == False:
            min = distancias[v]
            minIndice = v

    return minIndice

################################################
################### EXECUÇÃO ###################
################################################
[nos, grafo] = carregaMatriz();

dijkstra(nos, 0, grafo);