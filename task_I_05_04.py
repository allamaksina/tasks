# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# from task_I_05_01 import write_input_to_file
#
file_name = 'task_I_05_04.txt'
# write_input_to_file(file_name)


def read_txt_file(filename, d):
    f = open(filename, 'r')
    lines_lst = []
    for line in f:
        lines_lst.append(line.split())
    f.close()

    f = open('task_I_05_04_2.txt', 'w')
    for line in lines_lst:
        f.write(d[line[0]] + ' ' + ' '.join(line[1:]) + '\n')
    f.close()
    

d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

read_txt_file(file_name, d)
