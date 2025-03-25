#Користувач вводить з клавіатури значення у список
# Після чого запускаються два потоки. Перший потік знахо
# дить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading


def find_max(numbers):
    print(max(numbers))


def find_min(numbers):
    print(min(numbers))


def read():
    numbers = []

    while True:
        input_number = int(input(" number "))

        if input_number == 0:
            return numbers


        numbers.append(input_number)


numbers = read()

maximum = threading.Thread(target=find_max, args=(numbers,))
minimum = threading.Thread(target=find_min, args=(numbers,))

maximum.start()
minimum.start()

maximum.join()
minimum.join()
