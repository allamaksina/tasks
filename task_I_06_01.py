# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

from time import sleep
# Так и не поняла толком, что надо сделать.
# var 1


class TrafficLightV1:

    __color = {'red': 'yellow', 'yellow': 'green', 'green': 'red'}
    __intervals = {'red': 7, 'yellow': 2, 'green': 3}

    def __init__(self):
        self.schedule = ''

    def running(self, schedule):
        self.schedule = schedule
        for i in range(len(self.schedule)):
            col = self.schedule[i]
            print(f'the signal is {col}')
            t = TrafficLightV1.__intervals[col]
            for j in range(t):
                print(t - j)
                sleep(1)
            if i < len(self.schedule) - 1 and self.schedule[i + 1] != TrafficLightV1.__color[col]:
                print(f'После {col} должен быть {TrafficLightV1.__color[col]}, '
                      f'а во входных данных {self.schedule[i + 1]}.')
                print('Порядок смены режимов нарушен! Светофор капут!')
                break


tl = TrafficLightV1()
tl.running(['yellow', 'green', 'red', 'yellow', 'green', 'yellow', 'red'])


# var 2 Без проверки на неверный цвет...

class TrafficLightV2:
    __color = 'red'

    # @staticmethod
    def running(self):
        order = {'red': 'yellow', 'yellow': 'green', 'green': 'red'}
        intervals = {'red': 7, 'yellow': 2, 'green': 3}

        for col in order.keys():
            TrafficLightV2.__color = col
            t = intervals[TrafficLightV2.__color]
            print(f'The signal is {TrafficLightV2.__color}.')
            for j in range(t):
                print(t - j)
                sleep(1)


tl = TrafficLightV2()
tl.running()

# var 3


class TrafficLight:

    __color = 'green'
    __order = {'red': 'yellow', 'yellow': 'green', 'green': 'red'}
    __intervals = {'red': 7, 'yellow': 2, 'green': 3}

    def running(self, next_color):
        if TrafficLight.__order[TrafficLight.__color] != next_color:
            print('wrong color')
            exit()
            # вроде бы вот этот exit() - моветон, но я не придумала, как иначе в этом варианте
        else:
            TrafficLight.__color = next_color
            t = TrafficLight.__intervals[TrafficLight.__color]
            print(f'The signal is {TrafficLight.__color}')
            for i in range(t):
                print(t - i)
                sleep(1)


tl_v3 = TrafficLight()
tl_v3.running('red')
tl_v3.running('yellow')
tl_v3.running('green')
tl_v3.running('red')
tl_v3.running('yellow')
tl_v3.running('red')
tl_v3.running('green')




