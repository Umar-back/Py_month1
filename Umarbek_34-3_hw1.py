Monday = int(input('monday:'))
Tuesday = int(input('tuesday?'))
Wednesday = int(input('wednesday?'))
Thursday = int(input('thursday?'))
Friday = int(input('friday?'))
Saturday = int(input('saturday?'))
Sunday = int(input('sunday?'))

sum_soms = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday
print(f'Общая сумма {sum_soms}')
days_amount = 7
average = round(sum_soms/days_amount, 1)
print(f'Cредний расход в день {average}')
