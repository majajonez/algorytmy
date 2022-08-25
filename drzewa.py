class Tree:
    def __init__(self, wartosc, left = None, right = None):
        self.wartosc = wartosc
        self.left = left
        self.right = right

    def __str__(self):
         return f"Tree({self.wartosc})"



element1 = Tree(5, Tree(6, Tree(7, None, Tree(2)), Tree(8)), Tree(3, None, Tree(4)))




# print(element1.wartosc)

def drukuj_pre(node):
    print(node.wartosc)
    if node.left is not None:
        drukuj_pre(node.left)
    if node.right is not None:
        drukuj_pre(node.right)


def drukuj_in(node):
    if node.left is not None:
        drukuj_in(node.left)
    print(node.wartosc)
    if node.right is not None:
        drukuj_in(node.right)


def drukuj_post(node):
    if node.left is not None:
        drukuj_post(node.left)
    if node.right is not None:
        drukuj_post(node.right)
    print(node.wartosc)


kolejka = []
def drukuj_bfs(node):
    if node.left is not None:
        kolejka.append(node.left)
    if node.right is not None:
        kolejka.append(node.right)
    print(node.wartosc)
    if len(kolejka) != 0:
        n1 = kolejka[0]
        del kolejka[0]
        drukuj_bfs(n1)


# drukuj_pre(element1)

# drukuj_in(element1)

# drukuj_post(element1)

# drukuj_bfs(element1)

wysokosc = 0
def wysokosc_drzewa(node, current_depth):
    global wysokosc
    if current_depth > wysokosc:
        wysokosc = current_depth
    if node.left is not None:
        wysokosc_drzewa(node.left, current_depth + 1)
    if node.right is not None:
        wysokosc_drzewa(node.right, current_depth + 1)

# wysokosc_drzewa(element1, 0)
# print(wysokosc)


def wysokosc_post(node, current_depth):
    if node.left is not None:
        wysokosc_post(node.left, current_depth + 1)
    if node.right is not None:
        wysokosc_post(node.right, current_depth + 1)
    global wysokosc
    if current_depth > wysokosc:
        wysokosc = current_depth

# wysokosc_post(element1, 0)
# print(wysokosc)

wysokosc_kolejka = []
def wysokosc_bfs(node, current_depth):
    if node.left is not None:
        wysokosc_kolejka.append((node.left, current_depth +1))
    if node.right is not None:
        wysokosc_kolejka.append((node.right, current_depth +1))
    global wysokosc
    if current_depth > wysokosc:
        wysokosc = current_depth

    if len(wysokosc_kolejka) != 0:
        (n1, c) = wysokosc_kolejka[0]
        del wysokosc_kolejka[0]
        wysokosc_bfs(n1, c)

# wysokosc_bfs(element1, 0)
# print(wysokosc)



def pretrawers(node, f):
    f(node)
    if node.left is not None:
        pretrawers(node.left, f)
    if node.right is not None:
        pretrawers(node.right, f)


def liczba_elementow(root, licznik):
    pretrawers(root, lambda x: licznik.inc(1))



def suma_elementow(root, suma):
    pretrawers(root, lambda x: suma.inc(x.wartosc))

class Licznik:
    def __init__(self):
        self.v=0
    def inc(self, n):
        self.v += n
#
# suma=Licznik()
# suma_elementow(element1, suma)
# print(suma.v)
#
# licznik = Licznik()
# liczba_elementow(element1, licznik)
# print(licznik.v)

liscie = 0
def suma_lisci(node):
    global liscie
    if node.left is not None:
        suma_lisci(node.left)
    if node.right is not None:
        suma_lisci(node.right)
    if node.left is None and node.right is None:
        liscie += 1


suma_lisci(element1)
print(liscie)
