# (Завдання_1)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Node:
    def __init__(self, car):
        self.car = car
        self.left = None
        self.right = None

class CarPark:
    def __init__(self):
        self.root = None

    def add(self, car):
        if self.root is None:
            self.root = Node(car)
        else:
            self._insert(self.root, car)

    def _insert(self, node, car):
        if car.model < node.car.model:
            if node.left is None:
                node.left = Node(car)
            else:
                self._insert(node.left, car)
        elif car.model > node.car.model:
            if node.right is None:
                node.right = Node(car)
            else:
                self._insert(node.right, car)

    def remove(self, model):
        self.root = self._remove(self.root, model)

    def _remove(self, node, model):
        if node is None:
            return node
        if model < node.car.model:
            node.left = self._remove(node.left, model)
        elif model > node.car.model:
            node.right = self._remove(node.right, model)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.car = min_larger_node.car
            node.right = self._remove(node.right, min_larger_node.car.model)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, model):
        return self._search(self.root, model)

    def _search(self, node, model):
        if node is None or node.car.model == model:
            return node.car if node is not None else None
        if model < node.car.model:
            return self._search(node.left, model)
        return self._search(node.right, model)

    def __len__(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    def sell_car(self, client, model):
        car = self.search(model)
        if car is not None:
            self.remove(model)
            return f"Автомобіль {car.brand} {car.model}, {car.year} продано {client}."
        return "Автомобіль не знайдено."