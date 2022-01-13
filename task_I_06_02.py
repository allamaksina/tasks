# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def eval_mass(self):
        unit_mass = input('Enter the mass of the paving unit volume V = 1sq.m. x 1cm (kg): ')
        height = input('Enter the paving height (cm): ')
        mass = self._length * self._width * int(unit_mass) * int(height)
        print(f'The paving mass = {mass // 1000} tons')


r = Road(5000, 20)
r.eval_mass()
