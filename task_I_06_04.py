# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} поехала')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if self.speed:
            print(f'Машина {self.name} повернула {direction}')
        else:
            print('Никак')

    def show_speed(self):
        print(f'Current speed = {self.speed}')
        return self.speed


class TownCar(Car):

    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'Exceeding the speed limit by {self.speed - speed_limit} km/h')
        else:
            print(f'Current speed = {self.speed} km/h')
        return speed_limit - self.speed


class WorkCar(Car):

    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'Exceeding the speed limit by {self.speed - speed_limit} km/h')
        else:
            print(f'Current speed = {self.speed} km/h')
        return speed_limit - self.speed


class PoliceCar(Car):

    def self_check(self):
        if not self.is_police:
            print('PoliceCar is to be the police car!')
            print(f'{self.name} is now really police. \n')
            self.is_police = True

    def check_speed(self, mal_intruder):
        print(f'{self.name} checks {mal_intruder.name}:')
        if self.speed:
            print(f'{self.name} says: "No, no, no! I\'m driving!"\n')
        elif mal_intruder.is_police:
            print('iu-iu-iu... i beg your pardon! \n')
        else:
            sp = mal_intruder.show_speed()
            if sp < 0 or sp > 80:
                print('Hehehe! Gotcha!\n')
            else:
                print(f'Drive on!\n')


class SportCar(Car):

    def fix_speed(self):
        if self.speed:
            self.speed = max(350, self.speed)


sporty = SportCar('orange', 'Sporty')
little_worker = WorkCar('grey', 'Work car')
jig = TownCar('unicorn', 'JigJig')

mahoney = PoliceCar('blue', 'Mahoney')
mahoney.self_check()
lassard = PoliceCar('blue', 'Lassard', is_police=True)
mahoney.self_check()

sporty.go(30)
sporty.fix_speed()
sporty.show_speed()

little_worker.go(30)
little_worker.show_speed()

jig.go(80)
mahoney.go(150)
mahoney.show_speed()

lassard.check_speed(mahoney)
lassard.check_speed(little_worker)
mahoney.check_speed(sporty)

mahoney.stop()
mahoney.check_speed(sporty)
mahoney.check_speed(jig)


