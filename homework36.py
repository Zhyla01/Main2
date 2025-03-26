# (Завдання_1)

import threading

numbers = []


def input_thread():
    while True:
        user_input = input("Введіть число (або натисніть Enter для завершення): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Будь ласка, введіть валідне число.")


def sum_thread():
    total_sum = sum(numbers)
    print(f"Сума введених чисел: {total_sum}")


def average_thread():
    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
        print(f"Середнє арифметичне введених чисел: {average}")
    else:
        print("Список чисел порожній, не можна обчислити середнє.")


def main():
    input_t = threading.Thread(target=input_thread)
    input_t.start()

    input_t.join()

    sum_t = threading.Thread(target=sum_thread)
    average_t = threading.Thread(target=average_thread)

    sum_t.start()
    average_t.start()

    sum_t.join()
    average_t.join()


if __name__ == "__main__":
    main()