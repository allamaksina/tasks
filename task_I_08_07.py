# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum:

    def __init__(self, a, b):
        self.real = a
        self.img = b

    def __str__(self):
        if self.img:
            return f"{self.real} {('+', '-')[self.img < 0]} {abs(self.img)}j"
        else:
            return f"{self.real}"

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        a, b = self.real, self.img
        c, d = other.real, other.img
        return ComplexNum(a * c - b * d, a * d + c * b)

    def __truediv__(self, other):
        # z1/z2= (a+bi)/ (c+di)= (ac+bd)/ (c2+d2)+ (bc-ad)/ (c2+d2))i
        a, b = self.real, self.img
        c, d = other.real, other.img
        return ComplexNum((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2))


c1 = ComplexNum(3, 8)
print(c1)
c2 = ComplexNum(-5, 10)
print(c2)

print(c1 + c2, c1 - c2, c1 * c2, c1 / c2, sep='\n')

c3 = ComplexNum(6, -2)

print((c1 + c3) / c2)

c4 = ComplexNum(-2, 0)
print(c4)
print(c4 * c2)


