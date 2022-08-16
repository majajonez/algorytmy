class Node:
    def __init__(self, wartosc, wskaznik):
        self.wartosc = wartosc
        self.wskaznik = wskaznik

    # def __str__(self):
    #     wskaznik = self.wskaznik
    #     if wskaznik is not None:
    #         return f"Node({self.wartosc}, {wskaznik})"
    #     else:
    #         return f"Node({self.wartosc}, None)"


element1 = Node(5, Node(3, None))


def drukuj(node):
    print(node.wartosc)
    if node.wskaznik is not None:
        drukuj(node.wskaznik)

drukuj(element1)
