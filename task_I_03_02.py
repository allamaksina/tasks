# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


# если слово "несколько" - ключевое:
def fun(**kwargs):
    return ', '.join([f'{_}: {str(kwargs[_])}' for _ in kwargs])


# если оно не ключевое:
def fun1(name, last_name, year, city, email, phone_number):
    kwa = {'name': name, 'last_name': last_name, 'year': year,
           'city': city, 'email': email, 'phone_number': phone_number}
    return ', '.join([f'{_}: {str(kwa[_])}' for _ in kwa])


print(fun(name='Федя', last_name='Иванов', year=1997, city='СПб', email='fediv@ku.ru', phone_number=89005553533))
print(fun1(name='Федя', last_name='Иванов', year=1997, city='СПб', email='fediv@ku.ru', phone_number=89005553533))
