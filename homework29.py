# (Завдання_1)

class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

# (Завдання_2)

class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        time = distance / self.speed
        print(f"Їдемо до {destination}. Час в дорозі: {time} годин.")

# (Завдання_3)

class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.passengers = []
        self.capacity = capacity

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} сів у автобус.")
        else:
            print("Автобус переповнений. Пасажир не може сісти.")

    def move(self, destination, distance):
        if self.passengers:
            print(f"Висаджуємо {len(self.passengers)} пасажирів:")
            for p in self.passengers:
                print(f"- {p.name} на місце призначення {p.destination}")
            self.passengers.clear()

        super().move(destination, distance)

passenger1 = Passenger("Андрій", "МиколаЇв")
passenger2 = Passenger("Олена", "Одеса")

bus = Bus(speed=60, capacity=2)

bus.board_passenger(passenger1)
bus.board_passenger(passenger2)

passenger3 = Passenger("Петро", "Львів")
bus.board_passenger(passenger3)

bus.move("МиколаЇв", 120)