# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

# "В пределах" это включительно или нет? я предположила, что да.
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# если мое предположение не верно, то:
print([i for i in range(21, 240) if not i % 20 or not i % 21])


# def find_nums_div_20or21(start=20, stop=240):
#     return [i for i in range(start, stop + 1) if i % 20 == 0 or not i % 21]
#
#
# print(*find_nums_div_20or21())

