num1 = 0
num2 = 0

while num1 <= 50 and num2 <= 50:
    num = input('Введите число: ')
    if num.isnumeric():
        num = int(num)
        if num == 42:
            break
        if num % 5 == 0:
            print('Кратное 5')
        if num % 2 == 0:
            print('Чётное число')
            num1 += num
        else:
            print('Не чётное')
            num2 += num
    else:
        print('ошибка введите целое число: ')

print('Программа завершена')






