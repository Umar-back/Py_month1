# Работа с файлами
# w - write может стереть все
# a - add
# with открывает и закрывает
# x - не создает сущ файл который уже есть
# r - read, readlines



# with open('new_file.txt', 'r') as file:
#     for i in file.read():
#         print(i, end='')

    # print(file.read())
    # print(file.readlines())

# file = open('new_file.txt', 'w')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('new_file.txt', 'w') as file:
    # file.write('\nтретья строка')

# with open('file.txt', 'x') as new_file:
#     new_file.write('new file')