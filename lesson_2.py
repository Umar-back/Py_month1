#  логический тип данных, условные конструкции и операторы

'''bool - логический тип данных'''
# print(type(False))
# print(type(True))
#
# print(bool(''))
# print(bool(0))
# print(bool(0.0))


'''операторы назначения'''
# number = 10
# number = number + 5
# number += 7
# print(number)


'''логические операторы'''
# or, and, not
# print(not False)
# print(not True)


'''операторы сравнения'''
# print(2==3)
# print(2!=3)
# print(2>3)
# print(2<3)
# print(2>1)
# print(2==1)
# print(2>=1)
# print(2>1 or 2==1)
# print(5>3 and 5<9)
# print(3<5<9)
# print(7 if 6>9 else 1)


'''if elif else ВРЕМЯ'''
# time = input('введите время: ').lower()
#
# if time == 'утро' or time == 'morning':
#     print('good morning')
# elif time == 'день' or time == 'day':
#     print('good day')
# elif time == 'вечер' or time == 'evening':
#     print('good evening')
# else:
#     print('Здравствуйте, (время дня неизвестно!)')


'''password'''
# word = input('password: ')
# password = 'akinov766'

# if word == password:
#     print('dostup est')
# else:
#     print('dostupa netu')


'''isnumeric  len  ><'''
# if len(word) < 5:
#     print('short')
# elif word.isnumeric():
#     print('add letters')
# else:
#     print('okay')


'''задание со светофором'''
# svetafor = input('enter color: ').lower()
# if svetafor == 'красный' or svetafor == 'red':
#     print('стоп')
# elif svetafor == 'желтый' or svetafor == 'yellow':
#     print('внимание')
# elif svetafor == 'зеленый' or svetafor == 'green':
#     print('можете ехать')
# else:
#     print('не найдено')


'''задача с температурой'''
temperature = int(input('enter temp: '))

if temperature >= -20 and temperature <= 0:
    print('холодно')
elif temperature >= 1 and temperature <= 15:
    print('прохладно')
elif temperature >= 16 and temperature <= 25:
    print('тепло')
elif temperature >= 25 and temperature <= 40:
    print('жарко')
else:
    print('аномальная погода')
