class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self, key):
        t = BinaryTree(key)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def insert_right(self, key):
        t = BinaryTree(key)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def __str__(self):
        return f"[{self.key}; {self.left}; {self.right}]"


element1 = BinaryTree(5)
element1.insert_left(6)
element1.insert_right(3)
child = element1.get_left_child()
child.insert_left(7)
element1.get_left_child().insert_right(8)
element1.get_right_child().insert_right(4)
element1.get_left_child().get_left_child().insert_right(2)


print(element1.__str__())