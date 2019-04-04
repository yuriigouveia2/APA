import numpy

def carregaLista():
    arquivo = None
    while arquivo is None:
        arquivoEntrada = input("Digite o nome do arquivo (com a extensão): ")
        try:
            arquivo = open(arquivoEntrada, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    conteudoEntrada = arquivo.readlines()

    n, M = conteudoEntrada[0].split()
    n = int(n)
    M = int(M)
    p = [-1] * n
    v = [-1] * n

    for i in range(0, n):
        p[i], v[i] = conteudoEntrada[i+1].split()
        p[i] = int(p[i])
        v[i] = int(v[i])

    return n, M, p, v
    
#########################################################

def mochila(p, v, n, M):
    matriz = [[0 for i in range(M+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(M+1):
            if i == 0 or j == 0:
                matriz[i][j] = 0
            elif p[i-1] > j:
                matriz[i][j] = matriz[i - 1][j]
            else:
                matriz[i][j] = max(matriz[i - 1][j], v[i-1] + matriz[i - 1][(j) - p[i-1]])

    return matriz

###############################################

def itens(matriz, n, M, p):
    elementosPresentes = []      # Vetor que conterá os elementos presentes na mochila
    i = n                        # Cópia do número de itens total
    j = M                      # Cópia do peso máximo da mochila
    
    while i > 0 and j > 0:
        if matriz[i][j] != matriz[i-1][j]:
            elementosPresentes.append(i)
            j = j - p[i-1]
            i = i - 1
        else:
            i = i - 1

    elementosPresentes.sort()
    return elementosPresentes

###############################################

def imprimir(matriz, n, M, elementos):
    print("\nO melhor valor é:")
    print(matriz[n][M])
    print("Os elementos na mochila são:")
    print(elementos)

################################################
################### EXECUÇÃO ###################
################################################

[n, M, p, v] = carregaLista()
matriz = mochila(p, v, n, M)
elementos = itens(matriz, n, M, p)
imprimir(matriz, n, M, elementos)
