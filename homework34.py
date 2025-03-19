# (Завдання_1)

import json
import random


def start_game():
    number_to_guess = random.randint(1, 100)

    attempts = 0
    won = False

    while attempts < 5:
        guess = int(input("Вгадайте число (від 1 до 100): "))
        attempts += 1
        if guess < number_to_guess:
            print("Моє число більше!")
        elif guess > number_to_guess:
            print("Моє число менше!")
        else:
            print("Вітаю! Ви вгадали число!")
            won = True
            break

    if not won:
        print(f"На жаль, ви програли! Загадане число було: {number_to_guess}")

    return won


def save_data(stats, filename='game_data.json'):
    with open(filename, 'w') as f:
        json.dump(stats, f)


def load_data(filename='game_data.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"wins": 0, "losses": 0}


def main():
    stats = load_data()
    while True:
        if start_game():
            stats["wins"] += 1
        else:
            stats["losses"] += 1

        save_data(stats)

        play_again = input("Бажаєте зіграти ще раз? (так/ні): ").strip().lower()
        if play_again != 'так':
            break

    print(f"Кількість перемог: {stats['wins']}, Кількість поразок: {stats['losses']}")


if __name__ == "__main__":
    main()