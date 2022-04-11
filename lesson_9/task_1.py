"""1.
Определение количества различных подстрок с использованием хеш - функции.
Пусть на вход функции дана строка.Требуется вернуть количество различных подстрок в этой строке.
Примечания:
*в сумму не включаем пустую строку и строку целиком;
*без использования функций для вычисления хэша(hash(), sha1() или любой другой из модуля hashlib задача cчитается не решённой.
"""

import hashlib

def substr(s: str) -> int:
    assert len(s) > 0, 'Строка не может быть пустой'

    hash_set = set()

    for len_sub in range(len(s)-1, 0, -1):
        for i in range(len(s) - len_sub + 1):
            h_sub = hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest()
            hash_set.add(h_sub)

    return len(hash_set)

s = input('Введите строку:\n')
print(f'Количество уникальных подстрок {substr(s)} ' )