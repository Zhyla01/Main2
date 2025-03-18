# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(fiename) – зберегти дані у файл(за замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за замовчуванням cart.json)

import json

class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total = 0

    def add(self, item, price):
         self.items.append(item)
         self.total += price

    def delete(self, item, price):
        self.items.remove(item)
        self.total -= price

    def info(self):
        print(self.user)
        print("Кошик")
        for item in self.items:
            print("   ", item)

        print(f"Загальна ціна -- {self.total}")

    def save(self, filename="cart.json"):
        data = {"user": self.user, "items": self.items, "total": self.total}
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, filename="cart.json"):
        with open(filename, "r") as file:
            data = json.load(file)
        self.user = data["user"]
        self.items = data["items"]
        self.total = data["total"]


cart = Cart("Jhon")
# cart.add("Молоко", 10)
# cart.add("Хліб", 5)
#
# cart.save()

cart.load()
cart.info()
