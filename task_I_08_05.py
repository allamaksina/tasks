# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Все в модуле task_I_08_04. Здесь только тест

import task_I_08_04 as tt

warehouse = tt.Warehouse()

warehouse.subdivs = ['office1', 'office2', 'office3']

p1 = tt.Printer()
p1.add_attrs(vendor='HP', mode='laser', pages=30)
print(p1)
warehouse.add_to_storage(p1)


p2 = tt.Printer()
warehouse.add_to_storage(p2)
p3 = tt.Printer()
warehouse.add_to_storage(p3)
p4 = tt.Printer()
warehouse.add_to_storage(p4)

warehouse.add_link('office1', p1)
# try to send p1 to another office
warehouse.add_link('office2', p2)
warehouse.add_link('office3', p3)
warehouse.add_link('office2', p3)

x1 = tt.Xerox()
warehouse.add_to_storage(x1)
warehouse.add_link('office1', x1)
x2 = tt.Xerox()
warehouse.add_to_storage(x2)
x3 = tt.Xerox()
warehouse.add_to_storage(x3)
warehouse.add_link('office3', x3)

s1 = tt.Scaner()
warehouse.add_to_storage(s1)
warehouse.add_link('office1', s1)
s2 = tt.Scaner()
warehouse.add_to_storage(s2)
s3 = tt.Scaner()
warehouse.add_to_storage(s3)
s4 = tt.Scaner()
warehouse.add_to_storage(s4)

print(warehouse.units)
print(*[e.name for e in warehouse.units], sep='\n')
print(*warehouse.links.items(), sep='\n')

warehouse.show_office_equipment('office1')
warehouse.show_office_equipment('office5')
warehouse.show_storage()





