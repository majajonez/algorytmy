
operator = ['+', '-', '*', '/']


def wykonaj_dzialanie(a, b, znak_dzialania):
    if znak_dzialania == '+':
        return a + b
    elif znak_dzialania == '-':
        return a - b
    elif znak_dzialania == '*':
        return a * b
    elif znak_dzialania == '/':
        return a / b


def oblicz_onp(wpisane):
    kolejka = [x for x in wpisane]
    stos = []
    while len(kolejka) > 0:
        if kolejka[0] not in operator:
            stos.append(int(kolejka[0]))
            del kolejka[0]
        else:
            a = stos[-2]
            b = stos[-1]
            del stos[-1]
            del stos[-1]
            stos.append(wykonaj_dzialanie(a, b, kolejka[0]))
            del kolejka[0]
    return stos[0]


if __name__ == '__main__':
    print(oblicz_onp(input("wpisz działanie onp oddzielając znaki spacją").split(" ")))






