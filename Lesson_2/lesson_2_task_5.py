"""5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке."""

first = 32
last = 127
for i in range(first, last + 1):
    print(f'{i}\t{chr(i)}')