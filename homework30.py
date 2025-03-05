# (Завдання_1)

class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self):
        if not self.tail:
            return None
        removed_name = self.tail.name
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return removed_name

    def is_empty(self):
        return self.head is None

    def __str__(self):
        current = self.head
        names = []
        while current:
            names.append(current.name)
            current = current.next
        return " -> ".join(names)

class Shop:
    def __init__(self):
        self.queue1 = DoublyLinkedList()
        self.queue2 = DoublyLinkedList()
        self.queue3 = DoublyLinkedList()

    def add_buyer(self, name, idx):
        if idx == 1:
            self.queue1.add(name)
        elif idx == 2:
            self.queue2.add(name)
        elif idx == 3:
            self.queue3.add(name)
        else:
            print("Невірний номер черги!")

    def serve_buyer(self, idx):
        if idx == 1:
            if not self.queue1.is_empty():
                served_name = self.queue1.remove()
                print(f"Обслуговується покупець: {served_name}")
                if self.queue1.is_empty():
                    self._reorder(1)
            else:
                print("Черга 1 порожня!")
        elif idx == 2:
            if not self.queue2.is_empty():
                served_name = self.queue2.remove()
                print(f"Обслуговується покупець: {served_name}")
                if self.queue2.is_empty():
                    self._reorder(2)
            else:
                print("Черга 2 порожня!")
        elif idx == 3:
            if not self.queue3.is_empty():
                served_name = self.queue3.remove()
                print(f"Обслуговується покупець: {served_name}")
                if self.queue3.is_empty():
                    self._reorder(3)
            else:
                print("Черга 3 порожня!")

    def _reorder(self, idx):
        if idx == 1 and not self.queue2.is_empty():
            last_buyer = self.queue2.remove()
            self.queue1.add(last_buyer)
        elif idx == 2 and not self.queue3.is_empty():
            last_buyer = self.queue3.remove()
            self.queue2.add(last_buyer)
        elif idx == 3 and not self.queue1.is_empty():
            last_buyer = self.queue1.remove()
            self.queue3.add(last_buyer)

    def display_info(self):
        print(f"Черга 1: {self.queue1}")
        print(f"Черга 2: {self.queue2}")
        print(f"Черга 3: {self.queue3}")

shop = Shop()
shop.add_buyer("Олег", 1)
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)

print("Черги:")
shop.display_info()

shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)

print("Після обслуговування покупців:")
shop.display_info()

shop.serve_buyer(1)

print("Покупці перейшли до вільної каси:")
shop.display_info()