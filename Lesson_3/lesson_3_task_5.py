"""В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

import random

num_list = [random.randint(-99, 99) for _ in range(10)]
max_el = -float('inf')

for i, item in enumerate(num_list):
    if max_el < item < 0:
        max_el = item
        max_idx = i

print(f'В массиве: \n{num_list} \nМаксимальный отрицательный элемент = {max_el} \nЕго индекс = {max_idx}')