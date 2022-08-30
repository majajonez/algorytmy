import math


class Kopiec:
    def __init__(self, wartosc):
        self.tablica = [wartosc]

    def insert(self, wartosc):
        self.tablica.append(wartosc)
        i = len(self.tablica) - 1           # index elementu
        self.kopcowanie_w_gore(i)

    def kopcowanie_w_gore(self, i):
        i_rodzic = (i - 1) // 2             # index rodzica
        wartosc_i = self.tablica[i]         # wartosc elementu
        wartosc_r = self.tablica[i_rodzic]  # wartosc rodzica
        if wartosc_i < wartosc_r:
            print(f"cos {wartosc_i} {wartosc_r}")
            self.tablica[i] = wartosc_r
            self.tablica[i_rodzic] = wartosc_i
            i = i_rodzic
            self.kopcowanie_w_gore(i)

    def drukuj(self):
        y = len(self.tablica)
        wysokosc = int(math.log(y + 1, 2)) - 1
        if y > int(math.pow(2, wysokosc + 1) - 1):
            wysokosc += 1
        for n in range(0, wysokosc +1):
            low = int(math.pow(2, n) - 1)
            high = int(2 * low + 1)
            zmienna = ""
            for t in range(low, min(high, y)):
                zmienna = zmienna + (str(self.tablica[t])) + " "
            print(zmienna)

    def inne_drukuj(self):
        wysokosc = 0
        zmienna = ""
        for i in range(0, len(self.tablica)):
            nowa_wysokosc = int(math.log(i + 1, 2))
            if nowa_wysokosc > wysokosc:
                print(zmienna)
                zmienna = ""
                wysokosc = nowa_wysokosc
            zmienna = zmienna + str(self.tablica[i]) + " "
        print(zmienna)





element = Kopiec(5)
element.insert(4)
# element.insert(3)
# element.insert(7)
# element.insert(8)
# element.insert(9)
# element.insert(10)
# element.insert(2)


element.inne_drukuj()
