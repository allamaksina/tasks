# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).

# from random import choice, randrange
#
# f = open('task_I_05_07.txt', 'w')
# for i in range(100):
#     n = f'firm{i + 1}'
#     s = choice(['ООО', 'ТОО', 'ИЧП', 'АО'])
#     income = str(randrange(1000, 1000000))
#     costs = str(randrange(1000, 1000000))
#     f.write(' '.join([n, s, income, costs]))
#     f.write('\n')
# f.close()

import json

with open('task_I_05_07.txt', 'r') as f:
    lines = [i.split() for i in f.readlines()]

firms = dict([(line[0], int(line[2]) - int(line[3])) for line in lines])

firms_positive = [i for i in firms.values() if i > 0]
av_profit = sum(firms_positive) / len(firms_positive)

data = [firms, {"avarage_profit": av_profit}]

with open("task_I_05_07.json", "w") as write_f:
    json.dump(data, write_f)

