while True:
    word = input('Введите слово (латиница или кариллица) или exit для выхода: ')
    if word.lower() == 'exit':
        print('Программа завершена')
        break
    letters = len(word)
    vowels = 0
    consonants = 0

    for letter in word:
        if letter.lower() in 'aeiouaеёиоуыэюя':
            vowels += 1
        else:
            consonants += 1

    vowels_persentage = (vowels/letters) * 100
    consonants_persentage = (consonants/letters) * 100

    print(f'Количество букв: {letters}')
    print(f'Согласных букв: {consonants}')
    print(f'Гласных букв: {vowels}')
    print(f'Гласные/Согласные:  {vowels_persentage: .2f}% / {consonants_persentage: .2f}%')


