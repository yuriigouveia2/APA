#Lê arquivo e retorna lista
def read_file(path):
    lista = []
    #print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
    file = open(path, "r")
    for line in file:                                          #Lê o próximo valor do arquivo e adiciona na lista
        intLine = int(line)
        lista.append(intLine)
        #print("Desordenado[" + str(len(lista) - 1) + "]: " + str(lista[len(lista) - 1]))
    
    return lista

def quick_sort(lista):
    lista_final = []
    #Se houver um único elemento na lista, retorna-o
    if len(lista) <= 1:
        lista_final = lista
    else:
        #O elemento pivô é definido como sendo o primeiro elemento da lista
        pivo = lista[0]
        aux = 0
        i = 0
        for j in range(len(lista) - 1):
            if lista[j + 1] < pivo:                       #Se o elemento na posição j + 1 for menor que o pivo, é feito um swap
                aux        = lista[j + 1]
                lista[j+1] = lista[i + 1]
                lista[i+1] = aux
                i          = i + 1
        aux      = lista[0]
        lista[0] = lista[i]
        lista[i] = aux

        primeira_parte = quick_sort(lista[ : i])
        segunda_parte = quick_sort(lista[i + 1: ])
        primeira_parte.append(lista[i])
        lista_final = primeira_parte + segunda_parte
    return lista_final

################################################
################### EXECUÇÃO ###################
################################################
lista = read_file("entrada.txt")

print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
print(lista)
print("--- LISTA ORDENADA DO INSERTION SORT ---")
print(quick_sort(lista))