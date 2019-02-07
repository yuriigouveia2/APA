#Análise e Projeto de Algoritmos - Gilberto Farias
#Aluno    : Yuri da Costa Gouveia (yuridacostagouveia@gmail.com)
#Matrícula: 11328072

def merge_list(l_lista, r_lista):
    i = 0
    j = 0
    list_ordenada = []
    #iterate through both left and right sublist
    while i<len(l_lista) and j<len(r_lista):
        if l_lista[i] <= r_lista[j]:            #Se a lista da esquerda for menor que a da direita, então a colocamos na lista ordenada com um append e incrementa i
            list_ordenada.append(l_lista[i])
            i += 1
        else:                                   #Se a lista da direita for menor que o da esquerda, então a colocamos na lista ordenada com um append e incrementa j
            list_ordenada.append(r_lista[j])
            j += 1
    #É feito um merge do resto da lista da esquerda com o da direita
    list_ordenada += l_lista[i:]
    list_ordenada += r_lista[j:]
    
    return list_ordenada


def merge_sort(lista):
    final_list = []
    if len(lista) <= 1:                                        #Se houver um único elemento na lista, retorna-o
        final_list = lista
    else:
        meio = int(len(lista)/2)
        r_lista = merge_sort(lista[:meio])
        l_lista = merge_sort(lista[meio:])

        final_list = merge_list(l_lista,r_lista)               #Faz o merge das duas listas
    return final_list
        
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

################################################
################### EXECUÇÃO ###################
################################################
lista = read_file("entrada.txt")
print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
print(lista)
print("--- LISTA ORDENADA DO INSERTION SORT ---")
print(merge_sort(lista))