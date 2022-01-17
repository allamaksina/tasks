# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_span(self, param):
        pass


class Coat(Clothes):

    def __init__(self):
        self.name = 'coat'
        self.volume = 0

    def fabric_span(self, param):
        self.volume = param
        return self.span

    @property
    def my_name(self):
        return self.name

    @property
    def span(self):
        # if not self.volume:
            # print('not enough data')
            # return 0
        # else:
        #     return self.volume / 6.5 + 0.5

        return 0 if not self.volume else self.volume / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self):
        self.name = 'suit'

    def fabric_span(self, param):
        return 2 * param + 0.3


coat = Coat()

print(coat.span)
print(coat.fabric_span(44))
print(coat.my_name)

suit = Suit()
print(suit.fabric_span(1.8))

