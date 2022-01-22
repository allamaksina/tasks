# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class FailedCheckNum(Exception):
    pass


stop_word = 'stop'
i = ''
lst = []
while True:
    i = input('enter an integer (or enter stop for quit): ')
    if i == stop_word:
        break
    try:
        if sum([ch.isnumeric() for ch in i]) != len(i):
            raise FailedCheckNum
        lst.append(int(i))
        print(lst)
    except FailedCheckNum:
        print('not a numeric. try again')
