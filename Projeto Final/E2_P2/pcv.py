import sys
import numpy as np
import math as mt
import time
from random import *

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
    print("O tempo de duração da construção foi: " + str(tFinal - tInicial) + " segundos")

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
################ SELF ANNEALING ################
################################################
def simulated_anealing(temperatura, caminhoAtual, matriz, numNos):
    caminhoMinimo = caminhoAtual
    caminhoAdjacente = []*numNos

    while temperatura > TEMPERATURA_MINIMA:
        #print(str(custo(matriz, caminhoAtual)) + " | " + str(round(temperatura,2)))
        caminhoAdjacente = obter_caminho_adjacente(caminhoAtual, numNos)

        distanciaAtual = custo(matriz, caminhoAtual)            # Calculo dos custos das distancias
        distanciaMinima = custo(matriz, caminhoMinimo)
        distanciaAdjacente = custo(matriz, caminhoAdjacente)

        if distanciaAtual < distanciaMinima:        # Se a distancia do caminho atual for menor que a minima, ...            
            caminhoMinimo = caminhoAtual                                        # ... a minima como sendo a atual
        
        if aceita_rota(distanciaAtual, distanciaAdjacente, temperatura):
            caminhoAtual = caminhoAdjacente

        temperatura *= 1-TAXA_ESFRIAMENTO                                     # Formula de decrescimo da temperatura

    return caminhoMinimo
################################################

def aceita_rota(distanciaAtual, distanciaAdjacente, temperatura):
    rotaAceita = False
    probabilidadeAceitacao = 1

    if distanciaAdjacente >= distanciaAtual:
        probabilidadeAceitacao = np.exp((-1)*(distanciaAdjacente - distanciaAtual) / temperatura)           # Formula probabilistica da aceitaçao

    numAleatorio = random()                                 # Numero aleatorio entre 0 e 1

    if probabilidadeAceitacao >= numAleatorio:              # Caso a probabilidade de aceitaçao for maior que o numero aleatorio, a rota é aceita
        rotaAceita = True

    return rotaAceita

################################################
def obter_caminho_adjacente(caminho, numNos):
    i = j = 0                           # Condição inicial
    while i == j:                       # Gera indices aleatorios
        i = randint(0, numNos)
        j = randint(0, numNos)

    cidadeA = caminho[i]                # Retorna as cidades letativa aos indices
    cidadeB = caminho[j]

    caminho[i] = cidadeB                # Troca elas de posição
    caminho[j] = cidadeA

    return caminho.copy()


############# METAHEURISTICA ###################
def metaheuristica(numNos, matriz):
    visitados, caminho, distancia = construcao_gulosa(n, matriz)
    criterioParada = 0

    print("A distância da construção inicial foi: " + str(distancia))

    caminho = simulated_anealing(TEMPERATURA_INICIAL, caminho, matriz, numNos)
    distancia = custo(matriz, caminho)
 
    return caminho.copy(), distancia
################################################
################### EXECUÇÃO ###################
################################################
TAXA_ESFRIAMENTO = 0.005
TEMPERATURA_INICIAL = 999
TEMPERATURA_MINIMA = 0.99

n, matriz = tipoArquivo()
sys.setrecursionlimit(n*n)

tInicio = time.time()
novoCaminho, novaDist = metaheuristica(n, matriz)

print("A distância da otimização foi: " + str(novaDist))
tFim = time.time()
print("O tempo de duração da otimização foi: " + str(tFim - tInicio) + " segundos")




