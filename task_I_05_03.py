# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from task_I_05_01 import write_input_to_file


def analyze_this(filename):
    f = open(filename, 'r')
    # df = []
    zp_mean = []
    for line in f:
        splitted_line = line.split()
        if int(splitted_line[1]) < 20_000:
            print(splitted_line[0] + ' - оклад < 20 т. руб.')
        zp_mean.append(int(splitted_line[1]))
        # df.append([splitted_line[0], int(splitted_line[1])])
    f.close()
    print()
    print('Средняя величина дохода сотрудников: ', sum(zp_mean) / len(zp_mean))


file_name = 'task_I_05_03.txt'
# write_input_to_file(file_name)
analyze_this(file_name)


