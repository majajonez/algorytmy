def quicksort(list):
    element = list[0]
    list1 = []
    list2 = []
    for l in list:
        if l <= element:
            list1.append(l)
        else:
            list2.append(l)
    del list1[0]
    list1.sort()
    list2.sort()
    sorted = list1
    sorted.append(element)
    sorted += list2
    print(sorted)


numbers = [22, 6, 2, 76, 83, 47, 10, 49, 84, 3, 78, 50, 17]


def mergesort(list):
    central = len(list) // 2
    list1 = list[:central]
    list2 = list[central:]
    list1.sort()
    list2.sort()
    sorted = []
    while len(list1) and len(list2) > 0:
        if list1[0] < list2[0]:
            sorted.append(list1[0])
            del list1[0]
        elif list1[0] > list2[0]:
            sorted.append(list2[0])
            del list2[0]
        else:
            sorted.append(list1[0])
            sorted.append(list2[0])
            del list1[0]
            del list2[0]
    if len(list1) > 0:
        sorted += list1
    elif len(list2) > 0:
        sorted += list2
    print(sorted)



def insert_sort(lista):
    sorted = []
    c_list = lista.copy()
    if len(sorted) == 0:
        sorted.append(c_list[0])
    for x in c_list[1:]:
        been_inserted = False
        for p in range(len(sorted)):
            if x < sorted[p]:
                end = sorted[p:]
                del sorted[p:]
                sorted.append(x)
                sorted += end
                been_inserted = True
                break
        if been_inserted == False:
            sorted.append(x)
    print(sorted)





def bubble_sort(list):
    change = True
    while change == True:
        change = False
        for l in range(len(list) - 1):
            if list[l] > list[l + 1]:
                x = list[l]
                list[l] = list[l + 1]
                list[l + 1] = x
                change = True
    return list


print(bubble_sort(numbers))