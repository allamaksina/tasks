# 6. Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

#
def int_func(word):
    return word.capitalize()


# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func_for_string(string):
    # return ' '.join([int_func(word) for word in string.split()])
    # or
    return ' '.join(map(int_func, string.split()))


print(int_func('text'))
print(int_func_for_string('dictionary views can be iterated over to yield their respective data, '
                   'and support membership tests'))

