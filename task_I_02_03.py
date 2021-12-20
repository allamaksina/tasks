# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# 'зима' декабрь январь февраль весна март апрель май лето июнь июль август осень сентябрь октябрь ноябрь

seasons = ['зима', 'весна', 'лето', 'осень']
month_num = int(input('Введите номер месяца: '))

# list version

print(seasons[month_num % 12 // 3])

# dict version

d = {12: seasons[0], 1: seasons[0], 2: seasons[0],
     3: seasons[1], 4: seasons[1], 5: seasons[1],
     6: seasons[2], 7: seasons[2], 8: seasons[2],
     9: seasons[3], 10: seasons[3], 11: seasons[3]}
print(d[month_num])

# or
d = {0: seasons[0], 1: seasons[1], 2: seasons[2], 3: seasons[3]}
print(d[month_num % 12 // 3])

# or
d = {seasons[0]: (12, 1, 2), seasons[1]: (3, 4, 5), seasons[2]: (6, 7, 8), seasons[3]: (9, 10, 11)}
print(list(d.keys())[[month_num in z for z in d.values()].index(True)])

# or
d = {seasons[0]: (12, 1, 2), seasons[1]: (3, 4, 5), seasons[2]: (6, 7, 8), seasons[3]: (9, 10, 11)}
for item in d.items():
    if month_num in item[1]:
        print(item[0])
