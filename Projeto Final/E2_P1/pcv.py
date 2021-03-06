import sys
import numpy as np
import math as mt
import time

################################################
################## TIPO DE ARQUIVO #############
################################################
def tipoArquivo():
    tipo = input('Tipos de arquivo:\n1 - Competição\t2 - Teste \nQual o tipo de aquivo de leitura? ')

    if tipo == '1':
        n, matriz = criaMatrizComp()
    elif tipo == '2':
        n, matriz = carregaMatrizTeste()
    else:
        tipoArquivo()

    return n, matriz.copy()
    
################################################
############# LEITURA DO ARQUIVO ###############
################################################
def criaMatrizComp():
    arquivo = None
    while arquivo is None:
        arquivoEntrada = input("Digite o nome do arquivo com a extensão: ")
        try:
            arquivo = open(arquivoEntrada, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    entrada = arquivo.readlines()

    numNos = int(entrada[1].split(':')[1])
    vetorCoord = [[0]]*(numNos)
    matrizAux = [[0]*(numNos)]*(numNos)

    # quebra a string de entrada em uma lista de numeros
    for i in range(0, numNos):
        vetorCoord[i] = entrada[i+3].split()[1:]
        vetorCoord[i] = list(map(float, vetorCoord[i]))
 
    for partida in range(0, numNos):
        for chegada in range(0, numNos):
            matrizAux[partida][chegada] = distEuclidiana(vetorCoord[partida], vetorCoord[chegada])
    
    return numNos, matrizAux.copy()

##################################################

def distEuclidiana(inicial, final):
    return round(mt.sqrt((mt.pow((final[0] - inicial[0]), 2) + mt.pow((final[1] - inicial[1]), 2))))

##################################################

def carregaMatrizTeste():
    arquivo = None
    while arquivo is None:
        arquivoEntrada = input("Digite o nome do arquivo com a extensão: ")
        try:
            arquivo = open(arquivoEntrada, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    entrada = arquivo.readlines()

    numNos = int(entrada[1].split(':')[1])
    matrizAux = [[0]]*(numNos)

    # quebra a string de entrada em uma lista de numeros
    for i in range(0, numNos):
        matrizAux[i] = entrada[i+3].replace(',', '').split()
        matrizAux[i] = list(map(int, matrizAux[i]))
    
    return numNos, matrizAux.copy()

################################################
########## HEURISTICA DE CONSTRUÇÃO ############
################################################
############ VIZINHO MAIS PROXIMO ##############
################################################

def vizinho_mais_proximo(pontoPartida, numNos, matriz, visitados, caminho, distancia):
    minimo = sys.maxsize

    for noChegada in range(0, numNos):                    # Loop de escolha do vizinho mais próximo
        if matriz[pontoPartida][noChegada] > 0 and matriz[pontoPartida][noChegada] < minimo and visitados[noChegada]==False:
            minimo = matriz[pontoPartida][noChegada]

    distancia += minimo
    visitados[matriz[pontoPartida].index(minimo)] = True   # Marca ponto como visitado
    caminho.append(matriz[pontoPartida].index(minimo))     # Adiciona ponto aos caminhos

    if len(caminho) < numNos:                              # Recursividade para achar o caminho do vizinho mais próximo
        return vizinho_mais_proximo(matriz[pontoPartida].index(minimo), numNos, matriz, visitados, caminho, distancia)
    else:
        return visitados, caminho, distancia

################################################

def construcao_gulosa(numNos, matriz):
    caminho = [0]
    visitados = [False]*numNos
    noInicial = 0
    visitados[noInicial] = True
    distancia = 0

    visitados, caminho, distancia = vizinho_mais_proximo(noInicial, numNos, matriz, visitados, caminho, distancia)
    distancia += matriz[caminho[len(caminho) - 1]][noInicial]
    caminho.append(noInicial)

    return visitados, caminho, distancia

################################################
######### CUSTO DO CAMINHO PERCORRIDO ##########
################################################

def custo(matriz, caminho):
    return matriz[np.roll(caminho, 1), caminho].sum()

################################################
########### MOVIMENTO DE VIZINHANÇA ############
################################################

def vizinhanca(numNos, matrizAux, caminho, visitados, distancia):

    melhorCaminho = caminho
    melhorado = 0

    for i in range(1, len(caminho)-2):
        for j in range(i+1, len(caminho)):
            if j-i == 1:              # Não muda nada 
                continue
            novoCaminho = caminho[:]
            novoCaminho[i:j] = caminho[j-1:i-1:-1]  # 2-opt swap
            novaDistancia = custo(np.array(matriz), np.array(novoCaminho))
            if novaDistancia < distancia:      # Verifica se o novo caminho é melhor que o antigo
                melhorCaminho = novoCaminho
                melhorado = 0
                return caminho, distancia, melhorCaminho, novaDistancia #Retorna primeira melhora
            else:
                melhorado += 1
            if melhorado > 5000:
                return caminho, distancia, melhorCaminho, novaDistancia #Retorna solução sem melhora

################################################
################### EXECUÇÃO ###################
################################################

tInicio = time.time()
n, matriz = tipoArquivo()
sys.setrecursionlimit(n*n)

visitados, caminho, distancia = construcao_gulosa(n, matriz)
antigo, dist, novo, novaDist = vizinhanca(n, matriz, caminho, visitados, distancia)
print("A distância da construção inicial foi: " + str(dist))
print("A distância da otimização foi: " + str(novaDist))
tFim = time.time()

print("O tempo de duração foi: " + str(tFim - tInicio) + " segundos")




