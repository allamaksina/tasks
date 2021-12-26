# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.


def find_non_repeating_elements(lst):
    return [i for i in lst if lst.count(i) == 1]


s = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(find_non_repeating_elements(s))

input_list = input('Enter a list of integer values separated by a space: ').split()
x = []
for el in input_list:
    try:
        x.append(int(el))
    except ValueError:
        pass

print('Input list if integers:', x)
print('Result:', find_non_repeating_elements(x))

