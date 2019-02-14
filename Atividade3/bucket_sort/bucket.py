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


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

def bucket_sort(lista):
  bucketTam = len(lista)
  if len(lista) == 0:
    return lista

  # Determine minimum and maximum values
  minimo = lista[0]
  maximo = lista[0]
  for i in range(1, len(lista)):
    if lista[i] < minimo:
      minimo = lista[i]
    elif lista[i] > maximo:
      maximo = lista[i]

  # Initialize buckets
  bucketCont = int((maximo - minimo) / bucketTam) + 1
  buckets = []
  for i in range(0, bucketCont):
    buckets.append([])

  # Distribute input lista values into buckets
  for i in range(0, len(lista)):
    buckets[int((lista[i] - minimo) / bucketTam)].append(lista[i])

  # Sort buckets and place back into input lista
  lista = []
  for i in range(0, len(buckets)):
    insertion_sort(buckets[i])
    for j in range(0, len(buckets[i])):
      lista.append(buckets[i][j])

  return lista


################################################
################### EXECUÇÃO ###################
################################################
lista = read_file("entrada.txt")

print("--- LISTA NAO ORDENADA DO INSERTION SORT ---")
print(lista)
print("--- LISTA ORDENADA DO INSERTION SORT ---")
print(bucket_sort(lista))