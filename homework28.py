# (Завдання_1)

from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self.name = name
        self.satiety = max(0, min(satiety, 100))
        self.energy = max(0, min(energy, 100))

    def sleep(self):
        self.energy = 100

    def eat(self, food_amount: int):
        self.satiety = max(0, min(self.satiety + food_amount, 100))

    @abstractmethod
    def play(self, activity_level: int):
        pass

    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level: int):
        if self.satiety > 60:
            self.energy = max(0, self.energy - 2 * activity_level)
            self.satiety = max(0, self.satiety - activity_level)

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"{self.name} ловить мишу.")
            if self.satiety > 40:
                print(f"{self.name} грається з мишею.")
            else:
                print(f"{self.name} їсть мишу.")


class Dog(Pet):
    def play(self, activity_level: int):
        if self.satiety > 15:
            self.energy = max(0, self.energy - activity_level // 2)
            self.satiety = max(0, self.satiety - activity_level // 2)

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.satiety > 10:
            print(f"{self.name} ловить м'яч.")
            self.energy = max(0, self.energy - 5)


if __name__ == "__main__":
    my_cat = Cat("Мурчик")
    my_dog = Dog("Бобік")

    my_cat.eat(30)
    my_cat.play(10)
    my_cat.catch_mouse()
    my_cat.make_sound()

    my_dog.eat(20)
    my_dog.play(5)
    my_dog.fetch_ball()
    my_dog.make_sound()