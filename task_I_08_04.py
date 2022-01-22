# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.


def input_verif(func):
    def ex_fun(*args, **kwargs):
        ver = 1
        if (len(args) > 1 and not isinstance(args[1], OfficeEquipment)) or\
                (kwargs.get('ob') and not isinstance(kwargs['ob'], OfficeEquipment)):
            ver = 0
            txt = 'an object does not exist'
        elif kwargs.get('count') and not isinstance(kwargs['count'], int):
            ver = 0
            txt = 'the count value must be the integer'
        if ver:
            try:
                return func(*args, **kwargs)
            except TypeError:
                print('wrong input')
        else:
            print(f'Error: {txt}')
    return ex_fun


class Warehouse:

    def __init__(self):
        self.subdivs = []
        self.units = []
        self.links = {}

    @input_verif
    def add_to_storage(self, ob=None, ob_type='Printer', count=1):
        if ob:
            self.units.append(ob)
        else:
            if ob_type == 'Printer':
                for _ in range(count):
                    self.units.append(Printer())
            elif ob_type == 'Scaner':
                for _ in range(count):
                    self.units.append(Scaner())
            elif ob_type == 'Xerox':
                for _ in range(count):
                    self.units.append(Xerox())
            else:
                print('unknown equipment type')

    # @input_verif
    def add_link(self, *args):
        if args[1] not in self.units:
            print(f'no equipment with name {args[1].name}')
        else:
            if self.links.get(args[0]):
                self.links[args[0]].append(args[1])
            else:
                self.links.update([(args[0], [args[1]])])
            self.units.remove(args[1])

    def show_office_equipment(self, office_name):
        if office_name not in self.subdivs:
            print(f'no subdivision {office_name}')
        else:
            print('_' * 20)
            print(f'{office_name}:')
            print(*[f'{i + 1}. {v.name}' for i, v in enumerate(self.links.get(office_name))], sep='\n')
            print('_' * 20)

    def show_storage(self):
        print('_' * 20)
        print('Storage:')
        print(*[f'{i + 1}. {v.name}' for i, v in enumerate(self.units)], sep='\n')
        print('_' * 20)


class OfficeEquipment:

    counter = 0

    def __init__(self):
        self.vendor = ''
        OfficeEquipment.counter += 1
        self.id = bin(OfficeEquipment.counter)
        self.color = 'white'
        self.name = ''


class Printer(OfficeEquipment):

    def __init__(self):
        super().__init__()
        self.name = f'Printer_id#{self.id}'

    def add_attrs(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'{self.name}, {self.vendor}, {self.color}'


class Scaner(OfficeEquipment):

    def __init__(self):
        super().__init__()
        self.name = f'Scaner_id#{self.id}'

    def add_attrs(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'{self.name}, {self.vendor}, {self.color}'


class Xerox(OfficeEquipment):

    def __init__(self):
        super().__init__()
        self.name = f'Xerox_id#{self.id}'

    def add_attrs(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'{self.name}, {self.vendor}, {self.color}'

