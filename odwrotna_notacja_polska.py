operator1 = ['+', '-']
operator2 = ['*', '/']

def onp(wpisane):
    def przeniesienie_do_kolejki():
        kolejka.append(stos[-1])
        del stos[-1]

    kolejka = []
    stos = []
    odczytane = [x for x in wpisane]

    for e in odczytane:
        if e not in operator1 and e not in operator2:
            if e == "(":
                stos.append(e)
            elif e == ")":
                if len(stos) != 0:
                    while stos[-1] != "(":
                        przeniesienie_do_kolejki()
                    if stos[-1] == "(":
                        del stos[-1]
            else:
                kolejka.append(e)
        elif e in operator1:
            if len(stos) != 0:
                if stos[-1] == operator1 or stos[-1] == operator2:
                    przeniesienie_do_kolejki()
                    stos.append(e)
                else:
                    stos.append(e)
            else:
                stos.append(e)
        elif e in operator2:
            if len(stos) != 0:
                if stos[-1] == operator2:
                    przeniesienie_do_kolejki()
                    stos.append(e)
                else:
                    stos.append(e)
            else:
                stos.append(e)
    while len(stos) != 0:
        przeniesienie_do_kolejki()

    return kolejka



if __name__ == '__main__':
    print(onp(input("wpisz działanie oddzielając znaki spacją").split(" ")))

