class Tree:
    def __init__(self, wartosc, left, right):
        self.wartosc = wartosc
        self.left = left
        self.right = right

    def __str__(self):
         return f"Tree({self.wartosc})"



element1 = Tree(5, None, None)



print(element1.wartosc)

def drukuj(root):
    print(root.wartosc)
    if root.left is not None:
        print(root.left.wartosc)
