# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def write_nums(filename):
    lst = input('Введите целые числа, разделяя их пробелами: ').split()
    lst_ints = []
    for i in lst:
        try:
            lst_ints.append(int(i))
        except ValueError:
            pass
    f = open(filename, 'w')
    f.write(' '.join(map(str, lst_ints)))
    f.close()

    f = open(filename, 'r')
    # на случай, если чисел будет настолько много, что они не поместятся в одну строку
    file_sum = sum([sum(map(int, line.split())) for line in f.readlines()])
    f.close()

    print(file_sum)


write_nums('task_I_05_05.txt')
