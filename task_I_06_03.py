# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.d = {'wage': wage, 'bonus': bonus}
        # Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия
        # Вероятно, тут предполагается что-то такое
        self._income = lambda n_months, is_bonus: n_months * self.d['wage'] + (0, 1)[is_bonus] * self.d['bonus']


class Position(Worker):

    def full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_name(self):
        print('Tne name of the worker is', self.full_name())

    def get_total_income(self):
        n_moths = 12
        is_bonus = True
        print(f'Total income of {self.position} {self.full_name()} is {self._income(n_moths, is_bonus)} coins')


kneze = Position('Tsar', 'Tsarevich', 'The King', 1000, 50000)
kuzya = Position('Kuz\'ma', 'Domovyenok', 'domovoj', 1, 2)


kneze.get_full_name()
kneze.get_total_income()
kuzya.get_full_name()
kuzya.get_total_income()

