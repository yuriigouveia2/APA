#Análise e Projeto de Algoritmos - Gilberto Farias
#Aluno    : Yuri da Costa Gouveia (yuridacostagouveia@gmail.com)
#Matrícula: 11328072

#Classe referente ao selection sort
class selection:
    def __init__(self, path):
        self.path  = path

    #Lê o arquivo e após ter conhecimento de todos os valores em uma lista, faz-se a ordenação
    def selection(self):
        lista = []
        print("--- LISTA NAO ORDENADA DO SELECTION SORT ---")
        file       = open(self.path, "r")
        for line in file:                                                   #Vai lendo um valor por vez e armazenando na lista
            intLine = int(line)
            lista.append(intLine)

            print("Desordenado[" + str(len(lista) - 1) + "]: " + str(lista[len(lista) - 1]))

    #A essa altura do código, já temos todos os valores, não ordenados, armazenados na lista 'lista'
        for i in range(0, len(lista)):
            menor = i                                                       #Guarda o valor do índice do menor valor
            for j in range(i + 1, len(lista)):                              #Iteração para a posição seguinte (i+1), em relação ao primeiro for (i)
                if(lista[j] < lista[menor]):                                #Verifica se o valor de i(menor) é maior que j
                    menor = j                                               #Guarda o índice do menor valor
            if(lista[i] != lista[menor]):
                aux          = lista[i]                                     #Armazena o maior valor em uma variável auxiliar (aux)
                lista[i]     = lista[menor]                                 #Menor valor é colocado na menor(anterior) posição  
                lista[menor] = aux                                          #Maior valor é armazenado no de maior posição
            
        print("--- LISTA ORDENADA DO SELECTION SORT ---")
        for i in range(0, len(lista)):
            print("Ordenado[" + str(i) + "]: " + str(lista[i]))


        return lista                                                #Retorna lista final


################################################
################### EXECUÇÃO ###################
################################################
selection_sort = selection("entrada.txt") 
selection_sort.selection()