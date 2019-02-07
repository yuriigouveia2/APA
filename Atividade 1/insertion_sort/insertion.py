#Análise e Projeto de Algoritmos - Gilberto Farias
#Aluno    : Yuri da Costa Gouveia (yuridacostagouveia@gmail.com)
#Matrícula: 11328072

#Classe referente ao insertion sort
class insertion:
    def __init__(self, path):
        self.path  = path

    #Lê o arquivo e ordena a medida que lê novos valores (prints mostrados correspondem ao resultado final, e não o decorrer do programa)
    #OBS.: Os prints não foram mostrados no decorrer do programa para evitar desorganização na tela, caso haja alguma dúvida, favor entrar em contato;
    #Apesar disso, os valores são tratados a medida que são lidos do arquivo.
    def insertion(self):
        lista = []
        print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
        file = open(self.path, "r")
        for line in file:                                          #Lê o próximo valor do arquivo e adiciona na lista
            intLine = int(line)
            lista.append(intLine)

            print("Desordenado[" + str(len(lista) - 1) + "]: " + str(lista[len(lista) - 1]))

            for i in range(0, len(lista)):                          #Trata os valores armazenados até a última leitura
                aux = lista[i]                                      #Guarda valor atual numa variável auxiliar
                j   = i                                             #Guarda a posiçao da variável em 'j'
                while(j > 0 and aux < lista[j - 1]):                #Enquanto j>0 e aux for menor que o item anterior
                    lista[j] = lista[j - 1]                         #O de maior valor é alocado no de maior índice
                    j = j - 1                                       #Diminui no tamanho da lista, pois verificou um item
                lista[j] = aux                                      #O de menor valor é alocado no de menor índice

        print("--- LISTA ORDENADA DO INSERTION SORT ---")
        for i in range(0, len(lista)):
            print("Ordenado[" + str(i) + "]: " + str(lista[i]))


        return lista                                                #Retorna lista final

################################################
################### EXECUÇÃO ###################
################################################
insertion_sort = insertion("entrada.txt") 
insertion_sort.insertion()