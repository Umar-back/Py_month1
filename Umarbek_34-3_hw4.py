data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []
for i in data_tuple:
    if isinstance(i, str):
        if i == 'C':
            letters.append(i.lower())
        elif i == 'g':
            letters.append(i.upper())
        else:
            letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
numbers.insert(2, 2)

numbers.pop(0)
letters.insert(8, True)

numbers.sort()
letters.reverse()

numbers = [num ** 2 for num in numbers]

print(tuple(letters))
print(tuple(numbers))