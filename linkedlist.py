class Node:
    def __init__(self, value, indicator):
        self.value = value
        self.indicator = indicator

    # def __str__(self):
    #     wskaznik = self.wskaznik
    #     if wskaznik is not None:
    #         return f"Node({self.wartosc}, {wskaznik})"
    #     else:
    #         return f"Node({self.wartosc}, None)"


element1 = Node(5, Node(3, None))


def print_node(node):
    print(node.value)
    if node.indicator is not None:
        print_node(node.indicator)

print_node(element1)
