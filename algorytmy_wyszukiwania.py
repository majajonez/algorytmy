numbers = [1, 3, 4, 5, 7, 8, 9, 10, 19, 20, 39, 40, 49, 50, 51, 60]

def search_by_division(list, number):
    central_index = len(list) // 2
    central_number = list[central_index]
    if central_number == number:
        print(f'{number} was found')
    elif number < central_number:
        if len(list) > 1:
            search_by_division(list[:central_index], number)
        else:
            print("this number is not on the list")
    elif number > central_number:
        if len(list) > 1:
            search_by_division(list[central_index:], number)
        else:
            print("this number is not on the list")


search_by_division(numbers, 2)
