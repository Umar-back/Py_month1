# Структуры данных: списки - list, срезы, кортежи.
# [start:stop:step]


# objects = 45, 7.8, 'Geeks', True, [4, 5, 6] #это просто переменная, list вводит ее на терминал
# objects = list(objects)
# objects.append(44)
#
# #превращает list в tuple(кортежи)
# objects = tuple(objects)
#
# print(objects)
# print (type(objects))


# word = '1234556436303455345653469'
# half = len(word) // 2
# print(word[:half][::2])


# print(word[0:4])
# print(word[-1])

# word1 = [23, 56, False, [5,6]]
# print(word[0])
# print(word[3])
# print(word1[3][1])

# new = list('python')
# new = list(range(1, 6))
# print(new)

objects = [13, 23, 8.8, 33, 43, True, False]
#
# new = objects.copy()
# # new = objects
# print(id(new))
# print(id(objects))
#
# print(objects is new)
# print(objects == new)
#
# new[0] = 500
# print(objects)
# print(new)

# objects.sort()
# objects.sort(reverse=True)
# objects.reverse()
# objects = objects[::-1]

'''edit'''
# objects[0], objects[-1] = objects[-1], objects[0]        # меняет местами
# objects[-2] = 'piton'         # в конец списка добавляет можно с конца считаем с -
# objects[1:4] = [1, 4, 3]      # меняет местами 1:4 между ними убирает и добавляет 1, 4, 3

'''add'''
# objects.append(2+3)   # -+ и добавляет в конец списка
# objects.insert(2, 'Geeks')   # добавить новый элемент в любое место списка
# objects.extend(new)    # добавляет новые элементы в конец списка


'''delete'''
# new = [i for i in objects if i != 23]
# print(new)

# objects.remove(8.8)  # убирает 8.8 из листа
# objects.pop(-5)      # удаляет по индексу
# deleted = objects.pop(-5)
# objects = objects[2:]


print(objects)
# print(deleted)

# print(type(objects))
# print(objects)
# print(objects.index(23))


# for number in range(1,21):
#    print(number if number % 2 == 0 else None)


'''word вводит каждую букву и рядом число и убирает Т'''
# word = 'Kyrgyzstan'
# counter = 0
# 
# for letter in word:
#     if letter == 't':
#         continue
#     counter += 1
#     print(letter.upper(), counter)

'''задача с температурой'''
# # counter = 5
# while True:
#     temperature = input('enter temp: or "q" to exit ')
#     if temperature == 'q':
#         print('exit...')
#         break
#
#     temperature = int(temperature)
#
#     if temperature >= -20 and temperature <= 0:
#         print('холодно')
#     elif temperature >= 1 and temperature <= 15:
#         print('прохладно')
#     elif temperature >= 16 and temperature <= 25:
#         print('тепло')
#     elif temperature >= 25 and temperature <= 40:
#         print('жарко')
#     else:
#         print('аномальная погода')
#    # counter -= 1

'''while n повторяется до тех пор пока n не станет 0'''
# n = 5
#
# while n > 0:
#     print(n)
#     n -= 1