# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

def count_lines_and_words_in_txt_file(filename):

    f = open(filename, 'r')
    strs_num, words_num = 0, []
    for line in f:
        strs_num += 1
        words_num.append(len(line.split()))
    f.close()
    print(f'Количество строк = {strs_num}')
    print(*[f'Номер строки: {i[0] + 1}, количество слов: {i[1]}' for i in enumerate(words_num)], sep='\n')


count_lines_and_words_in_txt_file('task_I_05_01.txt')

