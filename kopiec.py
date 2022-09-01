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
            self.tablica[i] = wartosc_r
            self.tablica[i_rodzic] = wartosc_i
            i = i_rodzic
            if i != 0:
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

    def usun_min(self, i):
        min = self.tablica[i]
        i_lewe = 2 * i + 1
        i_prawe = 2 * i + 2
        if i_lewe < len(self.tablica) and i_prawe < len(self.tablica):
            w_lewe = self.tablica[i_lewe]
            w_prawe = self.tablica[i_prawe]
            if w_lewe < w_prawe:
                self.tablica[i_lewe] = min
                self.tablica[i] = w_lewe
                i = i_lewe
            if w_prawe < w_lewe:
                self.tablica[i_prawe] = min
                self.tablica[i] = w_prawe
                i = i_prawe
            self.usun_min(i)
        elif i_lewe < len(self.tablica) and i_prawe >= len(self.tablica):
            w_lewe = self.tablica[i_lewe]
            self.tablica[i] = w_lewe
            del self.tablica[i_lewe]
        else:
            del self.tablica[i]






element = Kopiec(5)
element.insert(4)
element.insert(3)
element.insert(7)
element.insert(8)
element.insert(9)
element.insert(10)
element.insert(2)


element.inne_drukuj()
print("q")
element.usun_min(0)
print("w")
element.inne_drukuj()
