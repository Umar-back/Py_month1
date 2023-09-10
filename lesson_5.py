# Структуры данных: словари - dict, множества - set.
# {key: value}

# # menu
# menu = {
#     'lagman' : {'лапша', 'мясо', 'перец'},
#     'manty' : {'мясо', 'тесто', 'лук'},
#     'okroshka' : {'кефир', 'редиска', 'колбаса'},
#     'salat' : {'томат', 'огурец', 'лук'}}
# while True:
#     name = input('enter menu: ').lower()
#     if name in menu:
#         print(menu[name])
#     else:
#         print(f'такого нет! mb interest for you: {tuple(menu.keys())} ')

# # set
# # дублирующиеся значения удаляются
# numbers = (23, 45, 67, 23, 45, 65)
# numbers = set(numbers)
# print(numbers)

# # новые 4 функции
# lagman = {'лапша', 'мясо', 'перец'}
# manty = {'мясо', 'тесто', 'лук'}

# # тут мы отталкиваемся от лагмана, находит отличия
# print(lagman.difference(manty))
# print(lagman - manty)

# # находим что есть общего между двумя блюдами
# print(lagman.intersection(manty))
# print(lagman & manty)

# # позволяет объединить множество с одной или более последовательностями поддерживающих итерирование
# print(lagman.union(manty))
# print(lagman | manty)

# # позволяет исключить из результата общие элементы
# print(lagman.symmetric_difference(manty))
# print(lagman ^ manty)

# # set  делает все попорядку и удаляет схожие числа
# numbers = [2, 7, 4, 1, 3, 4, 2, 7]
# numbers2 = {2, 7, 4, 1, 3, 4, 2, 7}
#
# print(type(numbers2))
# print(numbers)
# print(numbers2)

# # sum min max
# print(sum([4, 7, 8, 87]))
# print(min([4, 7, 8, 87]))
# print(max([4, 7, 8, 87]))

# # траты за неделю другим способом
# days_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# data = {i: int(input(f'enter exp {i.upper()}: ')) for i in days_list}
# print(
#     sum(data.values()),
#     sum(data.values()) / len(data),
#     sep='\n' # чтобы отделить сумму и среднию
# )

# print(dict(enumerate('python'))) # номерует каждую цифру и букву
#     (0, 3, 5): 5,
#     23: 5,
#     5.6: 67,
#     True: 45,
#     'string' : 5,

new = dict(name='Nazar', surname='Akinov', age=18, country='KGZ')
# print(new)

student = {
    'name' : 'Umar',
    'height' : 1.80,
    'age' : 16,
    'have_a_car' : True,
    'hobby' : ['chess', 'english', 'math', 'fast_typing', 'books'],
    'education' : ('school', 'college'),
}
# print(student.keys())   # вводит только названия ключей
# print(student.values()) # вводит только переменные в ключах
# print(student.items())

# for key, value in student.items():
#     print(f'{key}:{value}')   # в столбик список

# for i in student:
#     print(i, '=>', student[i])  # в столбик список


# print(student.get('educaton', 'нет такого ключа'))
# print(student.get('education'))

'''add'''
# student['surname'] = 'Akinov'
student.update(new)      # объеденение двух словарей сов. меняются

'''edit'''
# student['age'] += 1   # добавляет 1 к возрасту
# student['have_a_car'] = False  # меняет bool на False
# student['hobby'][-2] = 'football'  # меняет в hobby по индексу

'''delete'''
# student.pop('have_a_car')  # удаляет полностью
# del student['hobby']  # удаляет полностью хобби
# del student['hobby'][2]  # по индексу




# print(student['name'])  # получаем только имя
# print(student['age'])   # получаем только возраст
print(student)

print(type(student))

