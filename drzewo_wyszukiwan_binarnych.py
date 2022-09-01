class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key <= self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BinarySearchTree(key)
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BinarySearchTree(key)

    def search(self, key):
        if self.key == key:
            return True
        if key < self.key:
            if not self.left:
                return False
            return self.left.search(key)
        if not self.right:
            return False
        return self.right.search(key)

    def __str__(self):
        return f"[{self.key}; {self.left}; {self.right}]"

root = BinarySearchTree(8)
root.insert(5)
root.insert(3)
root.insert(9)
root.insert(10)
print(root.search(3))

print(root.__str__())