"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов."""

div_dict = dict.fromkeys(range(2, 10), 0)
for num in range(2, 100):
    for i in range(2, 10):
        if num % i == 0:
            div_dict[i] += 1

for key in div_dict:
    print(f'{key} кратны {div_dict[key]} чисел')