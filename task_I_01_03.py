# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

c = int(input('# 3. \nEnter a number n: \n'))
n, r = 3, [str(c)]
for _ in range(n - 1):
    r.append(str(c) + r[-1])
print('n + nn + nnn = ', sum(list(map(int, r))))

