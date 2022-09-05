numery = [1, 3, 4, 5, 7, 8, 9, 10, 19, 20, 39, 40, 49, 50, 51, 60]

def wyszukaj_przez_dzielenie(lista, numer):
    srodkowy_index = len(lista) // 2
    srodkowy_numer = lista[srodkowy_index]
    if srodkowy_numer == numer:
        print(f' znalazlem {numer}')
    elif numer < srodkowy_numer:
        if len(lista) > 1:
            wyszukaj_przez_dzielenie(lista[:srodkowy_index], numer)
        else:
            print("numeru nie ma na liscie")
    elif numer > srodkowy_numer:
        if len(lista) > 1:
            wyszukaj_przez_dzielenie(lista[srodkowy_index:], numer)
        else:
            print("numeru nie ma na liscie")


wyszukaj_przez_dzielenie(numery, 2)
