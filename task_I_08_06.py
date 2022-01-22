# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Сам метод тоже в task_I_08_04. Здесь только тест

import task_I_08_04 as tt

warehouse = tt.Warehouse()


p2 = 10
warehouse.add_to_storage(p2)


warehouse.add_to_storage(ob_type='spoon', count='ten')
warehouse.add_to_storage(ob_type='Scaner', count=10)
warehouse.add_to_storage(ob_type='Xerox', count=5)
warehouse.add_to_storage(ob_type='Printer', count=7)

print(warehouse.units[4])

warehouse.show_storage()
