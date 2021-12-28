# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.


def choose_greater_element_in_pairs(lst):
    """Функция получает список. Возвращает новый список из тех элементов с индексами i исходного
    списка, которые удовлетворяют условию lst[i] > lst[i - 1]"""
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]


def fix_input_list(input_list):
    """ Function takes input list of string values. Returns the list of correct integer values."""
    x = []
    for x_el in input_list:
        try:
            x.append(int(x_el))
        except ValueError:
            print(f'You entered non-integer value: {x_el}. It is excluded from the input array.')
    return x


# Проверяем, что получилось
#
# val_x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# val_y = [12, 44, 4, 10, 78, 123]
#
# test_y = choose_greater_elements_in_pairs(val_x)
# print(*test_y)
# print(*val_y)


def main():
    x_list_raw = input('Enter numbers separated by a space: ').split()
    x = fix_input_list(x_list_raw)
    print('Input list:', x)
    print('Result:', choose_greater_element_in_pairs(x))


main()
