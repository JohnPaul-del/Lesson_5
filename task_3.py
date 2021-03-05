from itertools import zip_longest, islice

names = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
grades = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
res_list = ((name, grade) for (name, grade) in zip_longest(names, grades))
print(*islice(res_list, max(len(names), len(grades))))
try:
    print(next(res_list))
except StopIteration:
    print("Nothing else to do")
