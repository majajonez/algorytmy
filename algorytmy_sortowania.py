numbers = [22, 6, 3, 2, 76, 83, 47, 10, 49, 84, 3, 78, 50, 17]

def quicksort(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return list


def mergesort(list):
    if len(list) <= 1:
        return list
    else:
        sorted = []
        central = len(list) // 2
        list1 = list[:central]
        list2 = list[central:]
        sl1 = mergesort(list1)
        sl2 = mergesort(list2)
        while len(sl1) > 0 and len(sl2) > 0:
            if sl1[0] < sl2[0]:
                sorted.append(sl1[0])
                del sl1[0]
            elif sl1[0] == sl2[0]:
                sorted.append(sl1[0])
                del sl1[0]
                sorted.append(sl2[0])
                del sl2[0]
            else:
                sorted.append(sl2[0])
                del sl2[0]
        sorted.extend(sl1)
        sorted.extend(sl2)
        return sorted


def insert_sort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            t = list[j]
            list[j] = list[j - 1]
            list[j - 1] = t
            j -= 1
    print(list)


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