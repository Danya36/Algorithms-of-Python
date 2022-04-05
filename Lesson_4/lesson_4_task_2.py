"""# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

# Тестовая функция проверяет до 1229-го простого числа."""

import cProfile


def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

# python -m timeit -n 100 -s "import lesson_4_task_2" "lesson_4_task_2.eratosthenes_sieve(10)"
# "lesson_4_task_2.eratosthenes_sieve(10)"
#100 loops, best of 5: 9.1 usec per loop
# "lesson_4_task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 162 usec per loop
# "lesson_4_task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 13.3 msec per loop
# Предположительно, алгоритм сложности O(n**2). Увеличение количества чисел в 10 раз
# увеличивает время выполнения приблизительно в 100 раз

# cProfile.run('eratosthenes_sieve(10)')
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:31(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:36(<listcomp>)
# cProfile.run('eratosthenes_sieve(100)')
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:31(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:36(<listcomp>)
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:58(<listcomp>)
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:61(<listcomp>)
# cProfile.run('eratosthenes_sieve(1000)')
# 1    0.022    0.022    0.023    0.023 lesson_4_task_2.py:31(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:36(<listcomp>)
# 2    0.000    0.000    0.000    0.000 lesson_4_task_2.py:58(<listcomp>)
# 2    0.000    0.000    0.000    0.000 lesson_4_task_2.py:61(<listcomp>)
# Время выполнения нарастает. Рекурсий нет.


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

# py -m timeit -n 100 -s "import lesson_4_task_2" "lesson_4_task_2.search_prime(10)"
# "lesson_4_task_2.search_prime(10)"
# 100 loops, best of 5: 6.12 usec per loop
# "lesson_4_task_2.search_prime(100)"
# 100 loops, best of 5: 160 usec per loop
# "lesson_4_task_2.search_prime(1000)"
# 100 loops, best of 5: 15.7 msec per loop
# Сложность близка к O(n**2)
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.

# cProfile.run('search_prime(1000)')
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:97(search_prime) 10
# 1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:97(search_prime) 100
# 1    0.019    0.019    0.019    0.019 lesson_4_task_2.py:97(search_prime) 1000
# Время выполнения нарастает. Рекурсий нет.


# ВЫВОД:
# Сложность алгоритмов и время их работы приблизительно одинаковые.