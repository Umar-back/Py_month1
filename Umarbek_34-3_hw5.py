Geeks = {
    'address': 'Toktogula 175',

    'courses': ['Android', 'Backend', 'Frontend'],

    'bag': {'fails', 'errors', 'stack'}
}
del Geeks['bag']
Geeks['address'] = 'Ибраимова 103'
Geeks['phone'] = '0557052018'
Geeks['instagram'] = '@geeks_edu, @geeks_osh'

add_courses = ['UX/UI', 'IOS', 'Менеджер проектов']
Geeks['courses'].extend(add_courses)
Geeks['courses'] = set(Geeks['courses'])

Geeks['founded_data'] = ' 4 мая 2018 года'
courses_num = len(Geeks['courses'])
print('Кол-во курсов', courses_num)

for key, value in Geeks.items():
    print(f'{key}:{value}')

# for i in Geeks:
#     print(i, '=>', Geeks[i])


#  ибраимова 103
# 0557 052 018
# 4 мая 2018 года
