# import redis
#
# server = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
#
# server.set('hello', 'world')
#
# name = server.get('hello')
# print(name)

# sql ін'єкція
# SELECT *
# FROM TABLE
# WHERE PASSWORD = '{user_password}'
#
#
# user_password = 123' OR '2' = '2
#
# SELECT *
# FROM TABLE
# WHERE PASSWORD = '123' OR '2' = '2'


# import redis
#
# server = redis.Redis(host='localhost', port=6379,
#                      db=0, decode_responses=True
#                      )
#
# server.set('user:name', 'Антон')
#
# name = server.get('user:name')
# print(name)

#Завдання 1
# Реалізуйте консольний додаток «Кошик» для
# вебмагазину. Додаток має надавати функціональність
# для роботи з кошиком. Можливості додатку:
# ■ Вхід у кошик за логіном та паролем;
# ■ Додати товар у кошик;
# ■ Видаляти товар з кошика;
# ■ Змінити товар у кошику;
# ■ Повне очищення кошика;
# ■ Пошук даних у кошику;
# ■ Перегляд вмісту кошика.
# Зберігайте дані у базі даних NoSQL.
# Можете використовувати Redis в якості платформи

import redis


class RedisCart:
    def __init__(self):
        self.server = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )

        # користувач з яким зараз працюємо
        self.current_user = None

    def _check_current_user(self):
        if self.current_user is None:
            print('Потрібно залогінитися')
            return False

        return True

    def _get_user_cart_key(self):
        return f"carts:{self.current_user}"

    def register_user(self, username, password):
        # перевірка чи зареєстрований юзер
        if self.server.hexists('users', username):
            print('Користувач уже зареєстрований')
            return

        # реєстрація нового юзера
        self.server.hset(
            'users',  # назва хеша(словника з логінами\паролями)
            username,
            password
        )

    # ■ Вхід у кошик за логіном та паролем;
    def login(self, username, password):
        # неправильний username
        if not self.server.hexists('users', username):
            print("Невірне ім'я користувача")
            return

        real_password = self.server.hget(
            "users", username
        )

        if real_password == password:
            print("Доступ надано")
            self.current_user = username
        else:
            print("Невірний пароль")

    # ■ Додати товар у кошик;
    def add_item(self, item_id, item_count):
        # carts:username = {
        #   "item_id": count
        # }

        # якщо користувач не залогінився
        if not self._check_current_user():
            return

        # словник для конкретного користувача
        key = self._get_user_cart_key()

        if self.server.hexists(key, item_id):
            # old_count = self.server.hget(key, item_id)
            # new_count = old_count + item_count
            # self.server.hset(key, item_id, new_count)
            self.server.hincrby(key, item_id, item_count)
        else:
            self.server.hset(key, item_id, item_count)

    # ■ Видаляти товар з кошика;

    def remove_item(self, item_id):
        if not self._check_current_user():
            return

            # словник для конкретного користувача
        key = self._get_user_cart_key()

        if self.server.hexists(key, item_id):
           self.server.hdel(key, item_id)
        else:
            print("Товару не має")


    # ■ Змінити товар у кошику;


    # ■ Повне очищення кошика;

    def clear_cart(self):
        if not self._check_current_user():
            return

        key = self._get_user_cart_key()
        self.server.delete(key)







    # ■ Пошук даних у кошику;


    # ■ Перегляд вмісту кошика.
    def show_cart(self):
        if not self._check_current_user():
            return

        # словник для конкретного користувача
        key = self._get_user_cart_key()

        # дістаємо увесь словник
        data = self.server.hgetall(key)

        # вивід на екран
        for item_id, item_count in data.items():
            print(f"\t{item_id}\t{item_count}шт")




# створити об'єкт класу
cart = RedisCart()

while True:
    print('0 -- вихід')
    print('1 -- реєстрація нового користувача')
    print('2 -- логін')
    print('3 -- додати товар до кошика')
    print('4 -- показати кошик')
    print('5 -- Видалити товар' )
    print('6 -- Кошик очишено')

    command = input('Введіть номер команди: ')

    if command == '0':
        break

    elif command == '1':
        username = input("Ведіть ім'я користувача: ")
        password = input("Ведіть пароль: ")
        cart.register_user(username, password)

    elif command == '2':
        username = input("Ведіть ім'я користувача: ")
        password = input("Ведіть пароль: ")
        cart.login(username, password)

    elif command == '3':
        item_id = input("Ведіть id товару: ")
        count = int(input("Ведіть кількість(шт): "))
        cart.add_item(item_id, count)

    elif command == '4':
        cart.show_cart()

    elif command == '5':
        item_id = input("Ведіть id товару: ")
        cart.remove_item(item_id)

    elif command == '6':
        cart.clear_cart()
    else:
        print("Невірна команда")



# hset users = {
#   "login": password
# }
#
# users = {
#     'Anton': '123456',
#     "Jhon": "asd123",
#     ....
# }