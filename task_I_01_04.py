# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

d = str(int(input('\n# 4. \nEnter a natural number n: \n')))
d_max = 0
i = 0
while i < len(d):
    if int(d[i]) > d_max:
        d_max = int(d[i])
    i += 1
print(f'max digit: {d_max}')

