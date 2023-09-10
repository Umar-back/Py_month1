# Функции, аргументы, args = аргумент  kwargs.
# DRY - dont repeat urself


# задача с мин
# def list(i):
#     list_length = len(i)
#     min_value = min(i)
#     print('Длина:', list_length)
#     print('Мин:', min_value)
# my_list = [2, 5, 6, 7]
# list(my_list)


# задача с мин
# def minimum(list):
#     counter = 0
#     min_value = None
#
#     for item in list:
#         counter += 1
#         if min_value is None or item < min_value:
#             min_value = item
#
#     print('Длина :', counter)
#     print('Мин:', min_value)
# my_list = [2, 5, 6, 7]
# minimum(my_list)


# задача с макс
# def maximum(list):
#     counter = 0
#     max_value = None
#
#     for item in list:
#         counter += 1
#         if max_value is None or item > max_value:
#             max_value = item
#
#     print('Длина :', counter)
#     print('Макс:', max_value)
#
# my_list = [2, 5, 6, 7]
# maximum(my_list)



# def menu(**kwargs):
#     return kwargs
#
# monday = menu(drink='tea', eat='pizza')
# print(monday)


# def plus(*args):
#     print(args)
#     return sum(args)
#
# print(plus(2, 5, 6, 8))



# схема функции
# определение наименование (параметры):
#     тело функции
#     возвращение результата
# наименование(аргументы)

# students = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
# def len1(items):
#     counter = 0
#     for _ in items:
#         counter += 1
#     return counter      # последнее действие
#
# print(len(students))
# print(len1(students))

# counter = 0
# for student in students:
#     counter += 1
# print(counter)




# print(len('2343'))   # print(len('2343')+5)
# print(len([1, 4, 4, 9, 7]))
# print(len([2, 4, 5, 6, 3, 7, 9, 10]))



# def greet(name=None, surname= 'Unknown'):  # name - обязательный позиционный параметр
#     print('Hello', name, surname)
#
#
# greet('Umar', 'Akinov')  # аргумент
# greet('Salladin', 'Ryskulov')
# greet(surname='Umarov', name='Madan')   # именованные аргументы


# def get_square(width, length):
#     """
#     Рассчитывает площадь Р
#     """
#     return width * length
# print(get_square.__doc__)
# print(help(get_square))

# square_2 = get_square(width=5, length=8)
# square_hall = get_square(12, 18 )
# print(square_2, square_hall, sep='/n')


# width = 5
# length = 8
# square_2 = width * length
# print(square_2)

# width = 12
# length = 18
# square_2 = width * length
# print(square_2)