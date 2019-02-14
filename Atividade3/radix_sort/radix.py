#Lê arquivo e saidaorna lista
def read_file(path):
    lista = []
    #print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
    file = open(path, "r")
    for line in file:                                          #Lê o próximo valor do arquivo e adiciona na lista
        intLine = int(line)
        lista.append(intLine)
        #print("Desordenado[" + str(len(lista) - 1) + "]: " + str(lista[len(lista) - 1]))
    
    return lista

#Algoritmo de contagem para contar a ocorrencia de cada valor
def counting_sort(lista, maximo, indice):
    cont = [0] * maximo

    for a in lista:
        cont[indice(a)] += 1
  
    for i, c in enumerate(cont):
        if i == 0:
            continue
        else:
            cont[i] += cont[i-1]

    for i, c in enumerate(cont[:-1]):
        if i == 0:
            cont[i] = 0
        cont[i+1] = c

    saida = [None] * len(lista)
    for a in lista:
        index = cont[indice(a)]
        saida[index] = a
        cont[indice(a)] += 1
  
    return saida

def digito(n, d):
  for i in range(d-1):
    n = n//10
  return n % 10

def numero_digito(numero):
  return len(str(numero))

def radix_sort(lista):
  maximo = max(lista)
  num_dig = numero_digito(maximo)

  for d in range(num_dig):
    lista = counting_sort(lista, maximo, lambda a: digito(a, d+1))
  return lista

################################################
################### EXECUÇÃO ###################
################################################
lista = read_file("entrada.txt")

print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
print(lista)
print("--- LISTA ORDENADA DO INSERTION SORT ---")
print(radix_sort(lista))