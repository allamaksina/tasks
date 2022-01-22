# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDiv(Exception):

    def __init__(self):
        self.name = 'zerodiv'


def my_div(a, b):
    try:
        if not b:
            raise ZeroDiv
        print(a / b)
    except ZeroDiv:
        print('div by zero')


my_div(2, 0)
my_div(20, 4)
