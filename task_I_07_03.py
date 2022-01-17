# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
# ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.


class MulticellularSmth:

    def __init__(self, n_cells):
        if isinstance(n_cells, int) and n_cells > 0:
            self.cells = n_cells
            # print(f'New organism is created by uniting {self.cells} cells, Master!')
        else:
            print('The number of the cage cells is to be a natural one')

    def __add__(self, other):
        return MulticellularSmth(self.cells + other.cells)

    def __sub__(self, other):
        return MulticellularSmth(self.cells - other.cells)

    def __mul__(self, other):
        return MulticellularSmth(self.cells * other.cells)

    def __truediv__(self, other):
        return MulticellularSmth(self.cells // other.cells)

    def make_order(self, num_stars_in_line):
        a, b = divmod(self.cells, num_stars_in_line)
        return ('*' * num_stars_in_line + '\n') * a + '*' * b

    def __str__(self):
        return f'I am {self.cells}-cells organism'


c = MulticellularSmth(12)
g = MulticellularSmth(-4)
h = MulticellularSmth(5)


print((c + h).make_order(6))
print(c)
print(c + h)



