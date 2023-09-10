with open('results.txt', 'r') as file:
    lines = file.readlines()

scores = {}
for line in lines:
    parts = line.split() # без этой функции программа выдаст всех студентов и топ 3 не будет интернет помог
    if len(parts) == 2:
        name = parts[0]
        score_str = parts[1]

        if score_str.isdigit():
            score = int(score_str)
            scores[name] = score
        else:
            print(f'{name}: {score_str}')

sort_students = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

print('топ-3 лучших студента по оценке:')
count = 0
for name, score in sort_students.items():
    if count < 3:
        print(f'{name} {score}')
        count += 1

with open('sorted_results.txt', 'w') as file:
    for name, score in sort_students.items():
        file.write(f'{name} {score}\n')