# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.

# тестово-вспомогательный кусок
# import numpy as np
# a = np.matrix([[1, -5, 2], [2, 5000, -1], [3, 2, 0]])
# b = np.matrix([[1, -5, 2], [200, 5, -1], [3, 2, 0]])
# print(a)
# key = 'oruy'
# print(f'{key[:25]:>40}')
# return '\n'.join(['\t'.join([' ' * (max_elem_digits_len - len(str(i))) + str(i) for i in r])
#                   for r in self.elements]) + '\n'


class Matrix:

    def __init__(self, lst):
        if isinstance(lst, list):
            if isinstance(lst[0], list):
                self.elements = lst
            else:
                self.elements = [lst]
        else:
            print('error input')

    @property
    def size(self):
        return len(self.elements), len(self.elements[0])

    def __str__(self):
        max_elem_digits_len = max([max([len(str(el)) for el in row]) for row in self.elements])
        return '\n'.join(['\t'.join([f"{i:>{str(max_elem_digits_len)}}" for i in r])
                          for r in self.elements])

    def __add__(self, other):
        return Matrix([[self.elements[i][j] + other.elements[i][j]
                       for j in range(self.size[1])]
                      for i in range(self.size[0])])

    def transpose(self):
        tmp = [[self.elements[i][j] for i in range(self.size[0])] for j in range(self.size[1])]
        return Matrix(tmp)


c = Matrix([[1, -500, 2], [20, 5, -1], [3, 2, 0]])
c2 = Matrix([[1, -5, 2], [2, 5, -1], [3, 2, 7]])
c3 = Matrix([[1, 2, 3, 4], [1, 1, 1, 1]])

print(c3.size)
print(c3)
print(c3.transpose())
print(c3.transpose().size)
# убедиться, что с3 остался неизменным, хотя по построению с ним и так ничего не произошло
print(c3.size)
print(c3)

print(c)
print(c2)
print(c + c2)

d = Matrix([1, 2, 3])
d2 = Matrix([1, -2, 3])

print(d + d2)

print(d)
print(d.size)
d = d.transpose()
print(d)
print(d.size)


