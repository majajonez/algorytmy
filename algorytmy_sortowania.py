def quicksort(lista):
    element = lista[0]
    lista1 = []
    lista2 = []
    for l in lista:
        if l <= element:
            lista1.append(l)
        else:
            lista2.append(l)
    del lista1[0]
    lista1.sort()
    lista2.sort()
    posortowane = lista1
    posortowane.append(element)
    posortowane += lista2
    print(posortowane)


numery = [22, 6, 2, 76, 83, 47, 10, 49, 84, 3, 78, 50, 17]
# quicksort(numery)

def mergesort(lista):
    srodek = len(lista) // 2
    lista1 = lista[:srodek]
    lista2 = lista[srodek:]
    lista1.sort()
    lista2.sort()
    posortowane = []
    while len(lista1) and len(lista2) > 0:
        if lista1[0] < lista2[0]:
            posortowane.append(lista1[0])
            del lista1[0]
        elif lista1[0] > lista2[0]:
            posortowane.append(lista2[0])
            del lista2[0]
        else:
            posortowane.append(lista1[0])
            posortowane.append(lista2[0])
            del lista1[0]
            del lista2[0]
    if len(lista1) > 0:
        posortowane += lista1
    elif len(lista2) > 0:
        posortowane += lista2
    print(posortowane)


# mergesort(numery)

def insert_sort(lista):
    posortowane = []
    klista = lista.copy()
    if len(posortowane) == 0:
        posortowane.append(klista[0])
    for x in klista[1:]:
        czy_wstawione = False
        for p in range(len(posortowane)):
            if x < posortowane[p]:
                koniec = posortowane[p:]
                del posortowane[p:]
                posortowane.append(x)
                posortowane += koniec
                czy_wstawione = True
                break
        if czy_wstawione == False:
            posortowane.append(x)
    print(posortowane)



# insert_sort(numery)


def bubble_sort(lista):
    zamiana = True
    while zamiana == True:
        zamiana = False
        for l in range(len(lista) - 1):
            if lista[l] > lista[l + 1]:
                x = lista[l]
                lista[l] = lista[l + 1]
                lista[l + 1] = x
                zamiana = True
    return lista


print(bubble_sort(numery))