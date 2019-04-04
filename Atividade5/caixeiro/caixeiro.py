import sys
import copy


def carregaMatriz():
    arquivo = None
    while arquivo is None:
        arquivoEntrada = input("Digite o nome do arquivo com a extensão: ")
        try:
            arquivo = open(arquivoEntrada, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    entrada = arquivo.readlines()

    numNos = int(entrada[0])
    matrizAux = [[0]]*(numNos)

    # quebra a string de entrada em uma lista de numeros
    for i in range(0, numNos):
        matrizAux[i] = entrada[i+1].split()
        matrizAux[i] = list(map(int, matrizAux[i]))
    
    return numNos, matrizAux.copy()


def caixeiro():
    for x in range(1, n):
        g[x + 1, ()] = matriz[x][0]
    
    custo = minimo(1,range(2,n+1))
    
    solucao = p.pop()
    caminho = [1]
    caminho.append(solucao[1][0])

    for x in range(n - 2):
        for novaSolucao in p:
            if tuple(solucao[1]) == novaSolucao[0]:
                solucao = novaSolucao
                caminho.append(solucao[1][0])
                break
    caminho.append(1)
   
    
    print("Valor: ", custo)
    print("Caminho: ", caminho)
    
    return

def minimo(k, a):
    if (k, a) in g:
        return g[k, a]

    valores = []
    minimos = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        minimos.append([j, tuple(set_a)])
        result = minimo(j, tuple(set_a))
        valores.append(matriz[k-1][j-1] + result)

    g[k, a] = min(valores)
    p.append(((k, a), minimos[valores.index(g[k, a])]))

    return g[k, a]


################################################
################### EXECUÇÃO ###################
################################################

n, matriz = carregaMatriz()
g = {}
p = []
if __name__ == '__main__':
    caixeiro()
sys.exit(0) 