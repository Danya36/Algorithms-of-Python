"""4. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв."""

print('Введите две прописные буквы латинского алфавита (a-z):')
letter1 = input('Первая буква = ')
letter2 = input('Вторая буква = ')

pos_letter1 = ord (letter1) - 96     #через таблицу символов Unicode
pos_letter2 = ord (letter2) - 96
distance = abs (pos_letter1 - pos_letter2) - 1
print(f'Буква "{letter1}" {pos_letter1}-я в алфавите\n'
      f'Буква "{letter2}" {pos_letter2}-я в алфавите\n'
      f'Между буквами {distance} букв')