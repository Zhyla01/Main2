# (Завдання_1)

class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage


class Zone:
    def serve_passenger(self, passenger):
        raise NotImplementedError("Цей метод потрібно перевизначити в дочірніх класах")


class RegistrationZone(Zone):
    def serve_passenger(self, passenger):
        # Перевірка наявності білету в багажі
        has_ticket = "ticket" in passenger.baggage
        return passenger, has_ticket


class SecurityZone(Zone):
    def serve_passenger(self, passenger):
        # Перевірка на наявність небезпечних предметів
        dangerous_items = {"knife", "gun", "explosives"}
        has_dangerous_items = any(item in dangerous_items for item in passenger.baggage)
        return passenger, not has_dangerous_items  # Повертаємо True, якщо немає небезпечних предметів


class BoardingZone(Zone):
    def serve_passenger(self, passenger):
        # Посадка не вимагає перевірки
        return passenger, True


class Airport:
    def __init__(self):
        self.passengers = []
        self.statistics = {
            "registration": 0,
            "security": 0,
            "boarding": 0
        }

    def add(self, passenger):
        self.passengers.append(passenger)

    def serve_registration(self):
        registration_zone = RegistrationZone()
        for passenger in self.passengers:
            passenger, success = registration_zone.serve_passenger(passenger)
            if success:
                self.statistics["registration"] += 1

    def serve_security_control(self):
        security_zone = SecurityZone()
        for passenger in self.passengers:
            passenger, success = security_zone.serve_passenger(passenger)
            if success:
                self.statistics["security"] += 1

    def serve_boarding(self):
        boarding_zone = BoardingZone()
        for passenger in self.passengers:
            passenger, success = boarding_zone.serve_passenger(passenger)
            if success:
                self.statistics["boarding"] += 1

    def show_statistics(self):
        print("Статистика:")
        print(f"Пройшло реєстрацію: {self.statistics['registration']}")
        print(f"Пройшло контроль безпеки: {self.statistics['security']}")
        print(f"Пройшло посадку: {self.statistics['boarding']}")


# Використання
passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)
airport.add(passenger5)
airport.add(passenger6)
airport.add(passenger7)
airport.add(passenger8)
airport.add(passenger9)
airport.add(passenger10)

# Проходимо етапи для кожного пасажира
airport.serve_registration()
airport.serve_security_control()
airport.serve_boarding()

# Показуємо статистику
airport.show_statistics()