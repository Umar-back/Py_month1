def get_index(lst):
    while True:
        try:
            enter_index = input('Введите индекс (0-10), or "q" to quit: ')
            if enter_index.lower() == 'q':
                print('Выход')
                break

            index = int(enter_index)


            if 0 <= index <= len(lst) - 1:
                print('Введите индекс', index, ':', lst[index])
            else:
                print('Индекс может быть от 0 до 10 ')
        except ValueError:
            print('Непральный ввод, введите индекс (0-10) ')

def main():
    ten = list(range(1, 11))
    evens = list(filter(lambda x: x % 2 == 0, ten))
    square = list(map(lambda x: x ** 2, evens))

    print('Квадрат четных чисел:', square)



    get_index(ten)
# тут ментор помог
if __name__ == '__main__':
    main()