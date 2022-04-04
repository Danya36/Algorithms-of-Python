''' В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.'''

import random

num_list = [random.randint(0, 99) for _ in range(10)]
print(*num_list)
min_el = num_list[0]
max_el = num_list[1]

for i, item in enumerate(num_list):
    if item <= min_el:
        min_el = item
        min_idx = i
    if item >= max_el:
        max_el = item
        max_idx = i

print(f'Минимальный элемент = {min_el}(индекс {min_idx})\nМаксимальный элементам = {max_el} (индекс {max_idx})')
if max_idx < min_idx:                             # Меняем индексы местами, если максимальный элемент встречаеся раньше
    max_idx, min_idx = min_idx, max_idx

print(f'Элементы между минимальным и максимальным: {num_list[min_idx + 1:max_idx]}')

summa = 0
for i in range(min_idx + 1, max_idx):
    summa += num_list[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами = {summa}')
