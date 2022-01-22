# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:

    date = ''

    def __init__(self, input_date_string):
        # self.date = input_date_string
        self.date = []
        if isinstance(input_date_string, str):

            for num in input_date_string.split('-'):
                try:
                    self.date.append(int(num))
                except TypeError:
                    print('not valid value')
                    Date.date = ''
                    break
        Date.date = self.date

    @classmethod
    def extract_date(cls):
        if cls.date:
            return '-'.join(map(str, cls.date))
        else:
            return 'no date'

    # cls.day, cls.month, cls.year =

    @staticmethod
    def valid_date():
        if Date.date:
            day_lims = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            if (0 < Date.date[1]) <= 12 and 0 < Date.date[0] <= day_lims[Date.date[1] - 1]:
                return 'valid date'
            else:
                return 'not valid date'
        else:
            return 'no date'


print(Date.extract_date())
print(Date.valid_date())
c = Date('30-2-1940')
print(Date.extract_date())
print(c.valid_date())


