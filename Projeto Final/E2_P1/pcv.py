import sys
import numpy as np

################################################
############# LEITURA DO ARQUIVO ###############
################################################
def carregaMatriz():
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
    melhorado = True
    while(melhorado):
        melhorado = False

        for i in range(1, len(caminho)-2):
            for j in range(i+1, len(caminho)):
                if j-i == 1:              # Não muda nada 
                    continue
                novoCaminho = caminho[:]
                novoCaminho[i:j] = caminho[j-1:i-1:-1]  # 2-opt swap
                novaDistancia = custo(np.array(matriz), np.array(novoCaminho))
                if novaDistancia < distancia:      # Verifica se o novo caminho é melhor que o antigo
                    melhorCaminho = novoCaminho
                    melhorado = True
                    return caminho, distancia, melhorCaminho, novaDistancia #Retorna primeira melhora

   # return caminho, distancia, melhorCaminho, novaDistancia



################################################
################### EXECUÇÃO ###################
################################################
n, matriz = carregaMatriz()


visitados, caminho, distancia = construcao_gulosa(n, matriz)
antigo, dist, novo, novaDist = vizinhanca(n, matriz, caminho, visitados, distancia)
print("A distância da construção inicial foi: " + dist)
print("A distância da otimização foi: " + novaDist)