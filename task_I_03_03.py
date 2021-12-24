# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return sum(sorted([a, b, c])[-2:])


# without sorting
def my_func1(a, b, c):
    # сумма наибольших двух будет наибольшей
    return max(a + b, a + c, b + c)


x, y, z = 300.0, 4, 100
print(my_func(x, y, z))
print(my_func1(x, y, z))

