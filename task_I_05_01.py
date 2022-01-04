# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


def write_input_to_file(filename):
    f = open(filename, 'w')
    while True:
        input_string = input('Введите данные: ')
        if input_string:
            f.write(input_string + '\n')
        else:
            break
    f.close()


if __name__ == '__main__':
    write_input_to_file('task_I_05_01.txt')
