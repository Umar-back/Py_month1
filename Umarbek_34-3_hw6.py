# def number(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# numbers = (2, 3, 4, 5)
# result = number(*numbers)
# print(result)
#



# def is_mirror_string(input_str, comparison_str='hello'):
#     return input_str.lower().replace(' ', '') == input_str.lower().replace(' ', '')[::-1] and input_str.lower() != comparison_str
#
# test_string = 'deed'
# result = is_mirror_string(test_string)
# print(result)
#
# test_string = 'world'
# result = is_mirror_string(test_string)
# print(result)


while True:
    operator = input("Знак (+, -, *, **, //, /): ")

    if operator == '0':
        break

    if operator in ('+', '-', '*', '**', '//', '/'):
        a = float(input("a = "))
        b = float(input("b = "))

        if operator == '+':
            print("%.2f" % (a + b))
        elif operator == '-':
            print("%.2f" % (a - b))
        elif operator == '**':
            print("%.2f" % (a ** b))
        elif operator == '//':
            print("%.2f" % (a / b))
        elif operator == '*':
            print("%.2f" % (a * b))
        elif operator == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")