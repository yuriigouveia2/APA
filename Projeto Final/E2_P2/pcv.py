import sys
import numpy as np
import math as mt
import time
from random import randint as rnd

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
    tInicial = time.time()

    caminho = [0]
    visitados = [False]*numNos
    noInicial = 0
    visitados[noInicial] = True
    distancia = 0

    visitados, caminho, distancia = vizinho_mais_proximo(noInicial, numNos, matriz, visitados, caminho, distancia)
    distancia += matriz[caminho[len(caminho) - 1]][noInicial]
    caminho.append(noInicial)

    tFinal = time.time()
    print("O tempo de duração de criação foi: " + str(tFinal - tInicial) + " segundos")
    return visitados, caminho, distancia

################################################
######### CUSTO DO CAMINHO PERCORRIDO ##########
################################################

def custo(matriz, caminho):
    matriz = np.array(matriz)
    caminho = np.array(caminho)
    return matriz[np.roll(caminho, 1), caminho].sum()

################################################
################ METAHEURISTICA ################
################################################
############ ESCOLHE MELHOR VIZINHO ############
################################################
def custo_de_mudanca(matriz, n1, n2, n3, n4):               # Cálculo de custo de benefício ao trocar posições
    return matriz[n1][n3] + matriz[n2][n4] - matriz[n1][n2] - matriz[n3][n4]

def busca_local(caminho, matriz):
    melhorCaminho = caminho
    improved = True
    while improved:
        improved = False
        for i in range(1, len(caminho) - 2):
            for j in range(i + 1, len(caminho)):
                if j - i == 1: continue
                if custo_de_mudanca(matriz, melhorCaminho[i - 1], melhorCaminho[i], melhorCaminho[j - 1], melhorCaminho[j]) < 0:
                    melhorCaminho[i:j] = melhorCaminho[j - 1:i - 1:-1]
                    improved = True
        caminho = melhorCaminho
    return melhorCaminho.copy()

############# SOLUÇÃO ALEATORIA ################
def gera_solucao_aleatoria(numNos, matriz):

    adicionado = [False]*numNos
    caminhoAleatorio = [None]*numNos
    posicao = rnd(0, numNos-1)
    primeiro = posicao

    for i in range(0, numNos):
        while adicionado[posicao]:
            posicao = rnd(0, numNos-1)

        caminhoAleatorio[i] = posicao
        adicionado[posicao] = True
    caminhoAleatorio[numNos-1] = primeiro
    distanciaAleatoria = custo(matriz, caminhoAleatorio)

    return caminhoAleatorio.copy(), distanciaAleatoria


############# METAHEURISTICA ###################
def metaheuristica(numNos, matriz):
    visitados, caminho, distancia = construcao_gulosa(n, matriz)
    criterioParada = 0

    print("A distância da construção inicial foi: " + str(distancia))

    while criterioParada < numNos:
        caminhoAleatorio, distanciaAleatoria = gera_solucao_aleatoria(numNos, matriz)
        novoCaminho = busca_local(caminhoAleatorio, matriz)
        novaDist = custo(matriz, novoCaminho)

        if novoCaminho != None and novaDist < distancia: 
            caminho = novoCaminho.copy()
            distancia = novaDist
            return caminho.copy(), distancia
        else: 
            criterioParada += 1   
    return caminho.copy(), distancia
################################################
################### EXECUÇÃO ###################
################################################
n, matriz = tipoArquivo()
sys.setrecursionlimit(n*n)

tInicio = time.time()

novoCaminho, novaDist = metaheuristica(n, matriz)

print("A distância da otimização foi: " + str(novoCaminho))
print("A distância da otimização foi: " + str(novaDist))
tFim = time.time()
print("O tempo de duração de otimização foi: " + str(tFim - tInicio) + " segundos")




