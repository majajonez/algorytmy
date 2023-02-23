class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
         return f"Tree({self.value})"



element1 = Tree(5, Tree(6, Tree(7, None, Tree(2)), Tree(8)), Tree(3, None, Tree(4)))




def print_pre(node):
    print(node.value)
    if node.left is not None:
        print_pre(node.left)
    if node.right is not None:
        print_pre(node.right)


def print_in(node):
    if node.left is not None:
        print_in(node.left)
    print(node.value)
    if node.right is not None:
        print_in(node.right)


def print_post(node):
    if node.left is not None:
        print_post(node.left)
    if node.right is not None:
        print_post(node.right)
    print(node.value)


queue = []
def print_bfs(node):
    if node.left is not None:
        queue.append(node.left)
    if node.right is not None:
        queue.append(node.right)
    print(node.value)
    if len(queue) != 0:
        n1 = queue[0]
        del queue[0]
        print_bfs(n1)



height = 0
def tree_height(node, current_depth):
    global height
    if current_depth > height:
        height = current_depth
    if node.left is not None:
        tree_height(node.left, current_depth + 1)
    if node.right is not None:
        tree_height(node.right, current_depth + 1)



def height_post(node, current_depth):
    if node.left is not None:
        height_post(node.left, current_depth + 1)
    if node.right is not None:
        height_post(node.right, current_depth + 1)
    global height
    if current_depth > height:
        height = current_depth



queue_height = []
def height_bfs(node, current_depth):
    if node.left is not None:
        queue_height.append((node.left, current_depth + 1))
    if node.right is not None:
        queue_height.append((node.right, current_depth + 1))
    global height
    if current_depth > height:
        height = current_depth

    if len(queue_height) != 0:
        (n1, c) = queue_height[0]
        del queue_height[0]
        height_bfs(n1, c)

# wysokosc_bfs(element1, 0)
# print(wysokosc)



def pretrawers(node, f):
    f(node)
    if node.left is not None:
        pretrawers(node.left, f)
    if node.right is not None:
        pretrawers(node.right, f)


def elements_number(root, counter):
    pretrawers(root, lambda x: counter.inc(1))



def elements_sum(root, sum):
    pretrawers(root, lambda x: sum.inc(x.value))

class Counter:
    def __init__(self):
        self.v=0
    def inc(self, n):
        self.v += n
#


leaves = 0
def leaves_sum(node):
    global leaves
    if node.left is not None:
        leaves_sum(node.left)
    if node.right is not None:
        leaves_sum(node.right)
    if node.left is None and node.right is None:
        leaves += 1


leaves_sum(element1)
print(leaves)
