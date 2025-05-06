# Частина 1: Основи Python
#  1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.
#  2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.
#  3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.
#  4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.
#  5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.
#  6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

# (Завдання_1)
# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# start, end = min(a, b), max(a, b)
# total = sum(range(start, end + 1))
# print(f"Сума чисел від {start} до {end}: {total}")

# (Завдання_2)
# total = sum(i for i in range(8, 105, 8))
# print(f"Сума парних чисел від 1 до 100: {total}")

# (Завдання_3)
# s = input("Введіть рядок: ")
# for letter in s:
#     print(letter)

# (Завдання_4)
# numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print("Парані числа:", even_numbers)

# (Завдання_5)
# def start_with_capital(strings):
#     return [s for s in strings if s and s[0].isupper()]
#
# user_strings = input("Введіть рядки через кому: ").split(",")
# result = start_with_capital([s.strip() for s in user_strings])
# print("Рядки що починаються з великої літери:", result)

# # (Завдання_6)
# def contain_python(strings):
#     return [s for s in strings if "Python" in s]
#
# user_strings = input("Введіть рядки через кому: ").split(",")
# result = contain_python([s.strip() for s in user_strings])
# print("Рядки що містять 'Python':", result)

# Частина 2: Об'єктно-орієнтоване програмування (ООП)
# Симулятор роботи сайту
#  WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
#  Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
#  WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
#  Реалізація функціональності:
#  Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
#  Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.

# (Завдання_1)
class WebPage:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def display_details(self):
        print(f"\nЗаголовок: {self.title}")
        print(f"Вміст: {self.content}")
        print(f"Дата публікації: {self.date}\n")

class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, title):
        initial_count = len(self.pages)
        self.pages = [p for p in self.pages if p.title != title]
        if len(self.pages) < initial_count:
            print(f"Сторінка '{title}' успішно видалена.")
        else:
            print(f"Сторінка '{title}' не знайдена.")

    def display_info(self):
        print(f"\n--- Інформація про сайт ---")
        print(f"Назва: {self.name}")
        print(f"URL: {self.url}")
        print("Список сторінок:")
        if self.pages:
            for p in self.pages:
                print(f"  - {p.title}")
        else:
            print("  Сторінок ще немає.")
        print("--------------------------\n")

def main():
    website = None

    while True:
        print("Обирайте дія:")
        print("1. Створити сайт")
        print("2. Додати сторінку")
        print("3. Видалити сторінку")
        print("4. Подивитися інформацію про сайт")
        print("5. Вийти")
        choice = input("Зробити вибір: ")

        if choice == '1':
            name = input("Введіть назву сайту: ")
            url = input("Введіть URL сайту: ")
            website = WebSite(name, url)
            print("Сайт створено.\n")

        elif choice == '2':
            if website is None:
                print("Спочатку створіть сайт.\n")
                continue
            title = input("Заголовок сторінки: ")
            content = input("Вміст сторінки: ")
            date = input("Дата публікації (рік-місяць-день): ")
            page = WebPage(title, content, date)
            website.add_page(page)
            print("Сторінка додана.\n")

        elif choice == '3':
            if website is None:
                print("Спочатку створіть сайт.\n")
                continue
            title = input("Введіть назву сторінки для видалення: ")
            website.remove_page(title)
            print()

        elif choice == '4':
            if website is None:
                print("Спочатку створіть сайт.\n")
                continue
            website.display_info()
            for p in website.pages:
                p.display_details()

        elif choice == '5':
            print("Вихід. До побачення!")
            break

        else:
            print("Некоректний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()