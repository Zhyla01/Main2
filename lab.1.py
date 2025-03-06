# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __str__(self):
#         return f"{self.head}"
#
#     def push_end(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         self.tail.next = new_node
#         self.tail = new_node
#
# data = SinglyLinkedList()
# data.push_end(1)
# data.push_end(2)
# data.push_end(3)
# print(data)

# Завдання 1
# Використовуючи стек створіть клас WebHistory
# Атрибути:
#  history – стек з історією відвідування веб сторінок
#  forward_history – стек з веб сторінками, для повернення
# «вперед»
# Методи:
#  add(page) – перейти на нову сторінку
#  undo() – повернутись на попередню сторінку
#  redo() – перейти вперед
#  get_current_page() – повернути поточну сторінку
# Завдання 2
# Використовуючи стек створіть клас EnterNumber для
# введення числа в рядку
# Атрибути:
#  digits – стек з введеними цифрами
# Методи:
#  add(digit) – додати нову цифру, вивести помилку якщо
# не цифра
#  undo() – видалити останню цифру
#  get_number() – повернути число
#  clear() – очистити стек
# Завдання 3
# Використовуючи стек створіть клас Calculator
# Атрибути:
#  operation – тип операції(за замовчуванням None)
#  answers – стек з результатами(за замовчуванням там
# один 0)
# Методи:
#  read() – читає текст введений користувачем, далі
# виконує наступні дії, в залежності від тексту
# o операція(+-*/) – змінює operation
# o число – дістати останнє число з answers(не
# видаляючи) та виконати дію operation, результат
# вивести на екран та добавити в answers
# o слово “show” – показати останній результат
# o слово «undo» -- повернутись до попереднього
# результату
# Завдання 4
# Є вираз з дужками, за допомогою стеків визначіть чи
# правильно розтавлені дужки, якщо ні то виведіть індекс
# «проблемної» дужки.
# def highlight_character(text, ind):
# for i, char in enumerate(text, start=1):
# if i == ind:
# print(f"\033[91m{char}\033[0m", end="")
# else:
# print(char, end="")
# print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def is_empty(self):
        """
        Чи є порожній
        :return: True якщо порожній
        """
        return self.head is None

    def peek(self):
        """
        Повертає останній елемент, не видаляючи його
        :return: останній елемент
        """
        return self.tail.data

class WebHistory:
    def __init__(self):
        self.history = DoubleLinkedList()
        self.forward_history = DoubleLinkedList()

    def add(self, page):
        self.history.push_end(page)
        self.forward_history = DoubleLinkedList()

    def undo(self):
        page = self.history.pop_end()
        self.forward_history.push_end(page)

    def redo(self):
        page = self.forward_history.pop_end()
        self.history.push_end(page)
    def get_current_page(self):
        return self.history.peek()