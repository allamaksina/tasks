# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
from sys import argv
from itertools import cycle


def cycle_test(lst, num_of_iterations):
    num_of_iterations *= len(lst)
    counter = 0
    for i in cycle(lst):
        counter += 1
        print(i, counter)
        if counter == num_of_iterations:
            break


def get_inputs():
    # Здесь можно вводить что угодно
    cycle_list = input('Enter a list of any values: ')
    # а здесь - нет
    while True:
        try:
            stop = int(input('Enter number of iterations: '))
        except ValueError:
            print('Please enter an integer!')
        else:
            break
    # * len(start) чтобы на каждой итерации функция вывела всю последовательность
    return cycle_list, stop


try:
    cycle_test(argv[1], int(argv[2]))
except IndexError:
    print('Not enough input parameters! Try again!')
    cycle_test(*get_inputs())
except ValueError:
    print('Num of iterations must be integer! Try again!')
    cycle_test(*get_inputs())


