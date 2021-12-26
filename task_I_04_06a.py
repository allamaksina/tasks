# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from sys import argv
from itertools import count

# start = int(argv[1])
# # int(input('Enter start integer value: '))
# stop = int(argv[2])
# # int(input('Enter stop integer value: '))


def count_test(first_val, stop_val):
    if stop_val < first_val:
        print('There is nothing to print!')
    else:
        for i in count(first_val):
            print(i)
            if i == stop_val:
                break


def get_int_val(message='Enter an integer: '):
    while True:
        try:
            res = int(input(message))
        except ValueError:
            print('Please enter an integer!')
        else:
            return res


# я использую функцию get_int_val в другом модуле, и это чтобы он не запускался из другого модуля
if __name__ == '__main__':
    start = 0
    stop = 10
    try:
        start = int(argv[1])
        stop = int(argv[2])
    except IndexError:
        print('Not enough input parameters! Try again!')
        start = get_int_val('Enter a start integer: ')
        stop = get_int_val('Enter a stop integer: ')
    except ValueError:
        print('Values must be integer! Try again!')
        start = get_int_val('Enter a start integer: ')
        stop = get_int_val('Enter a stop integer: ')
    finally:
        count_test(start, stop)
