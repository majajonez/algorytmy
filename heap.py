import math

class Heap:
    def __init__(self, value):
        self.table = [value]

    def insert(self, value):
        self.table.append(value)
        i = len(self.table) - 1           # index elementu
        self.heap_up(i)

    def heap_up(self, i):
        i_parent = (i - 1) // 2             # index rodzica
        value_i = self.table[i]         # wartosc elementu
        value_r = self.table[i_parent]  # wartosc rodzica
        if value_i < value_r:
            self.table[i] = value_r
            self.table[i_parent] = value_i
            i = i_parent
            if i != 0:
                self.heap_up(i)

    def print(self):
        y = len(self.table)
        height = int(math.log(y + 1, 2)) - 1
        if y > int(math.pow(2, height + 1) - 1):
            height += 1
        for n in range(0, height +1):
            low = int(math.pow(2, n) - 1)
            high = int(2 * low + 1)
            elements = ""
            for t in range(low, min(high, y)):
                elements = elements + (str(self.table[t])) + " "
            print(elements)

    def print_2(self):
        height = 0
        elements = ""
        for i in range(0, len(self.table)):
            new_height = int(math.log(i + 1, 2))
            if new_height > height:
                print(elements)
                elements = ""
                height = new_height
            elements = elements + str(self.table[i]) + " "
        print(elements)

    def delete_min(self, i):
        min = self.table[i]
        i_left = 2 * i + 1
        i_right = 2 * i + 2
        if i_left < len(self.table) and i_right < len(self.table):
            w_left = self.table[i_left]
            w_right = self.table[i_right]
            if w_left < w_right:
                self.table[i_left] = min
                self.table[i] = w_left
                i = i_left
            if w_right < w_left:
                self.table[i_right] = min
                self.table[i] = w_right
                i = i_right
            self.delete_min(i)
        elif i_left < len(self.table) and i_right >= len(self.table):
            w_left = self.table[i_left]
            self.table[i] = w_left
            del self.table[i_left]
        else:
            del self.table[i]






element = Heap(5)
element.insert(4)
element.insert(3)
element.insert(7)
element.insert(8)
element.insert(9)
element.insert(10)
element.insert(2)


element.print_2()
print("q")
element.delete_min(0)
print("w")
element.print_2()
