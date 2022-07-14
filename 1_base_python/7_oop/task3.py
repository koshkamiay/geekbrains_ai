class Cage:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __str__(self):
        return str(self.count_cell)

    def __add__(self, other): # сложение
        return Cage(int(self.count_cell + other.count_cell))

    def __sub__(self, other): # вычитание
        if self.count_cell - other.count_cell > 0:
            return Cage(self.count_cell - other.count_cell)
        else:
            return 'Невозможно произвести вычитание'

    def __mul__(self, other): # умножение
        return Cage(self.count_cell * other.count_cell)

    def __truediv__(self, other): # деление
        return Cage(int(self.count_cell / other.count_cell))

    def make_order(self, count_in_row):
        i = self.count_cell
        view_cell = ''
        while i > 0:
            if i > count_in_row:
                view_cell += '*' * count_in_row
            else:
                view_cell += '*' * i
            i -= count_in_row
            if i > 0:
                view_cell += '\n'
        print(view_cell)


cage_1 = Cage(10)
cage_2 = Cage(12)

print(cage_1 + cage_2)
print(cage_1 - cage_2)
print(cage_2 - cage_1)
print(cage_1 * cage_2)
print(cage_1 / cage_2)
cage_1.make_order(5)
