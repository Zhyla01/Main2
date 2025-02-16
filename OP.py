# (Завдання_1)

class BankAccount:
    exchange_rates = {
        'USD': 41.350,
        'EUR': 43.410,
        'UAH': 1.0
    }

    def __init__(self, client_name, balance, currency):
        self.client_name = client_name
        self.balance = balance
        self.currency = currency
        self.check_currency(currency)

    def display_info(self):
        """Вивід загальної інформації про рахунок"""
        print(f"Клієнт: {self.client_name}, Баланс: {self.balance} {self.currency}")

    def check_currency(self, currency):
        """Перевірка, чи валюта відома"""
        if currency not in self.exchange_rates:
            raise ValueError(f"Невідома валюта: {currency}")

    def convert_currency(self, amount, target_currency):
        """Переведення грошей з однієї валюти в іншу"""
        if self.currency != target_currency:
            amount_in_usd = amount / self.exchange_rates[self.currency]
            target_amount = amount_in_usd * self.exchange_rates[target_currency]
            return target_amount
        return amount

    def change_currency(self, new_currency):
        """Зміна валюти рахунку"""
        self.check_currency(new_currency)
        self.balance = self.convert_currency(self.balance, new_currency)
        self.currency = new_currency

    def deposit(self, amount):
        """Поповнення балансу (валюта та сама)"""
        self.balance += amount

    def withdraw(self, amount):
        """Зняття грошей з балансу (валюта та сама)"""
        if amount > self.balance:
            raise ValueError("Недостатньо коштів для зняття")
        self.balance -= amount


if __name__ == "__main__":
    account = BankAccount("Іван Іванов", 1000, "USD")
    account.display_info()

    account.deposit(500)
    account.display_info()

    account.withdraw(300)
    account.display_info()

    target_amount = account.convert_currency(200, 'EUR')
    print(f"200 {account.currency} в EUR: {target_amount:.2f}")

    account.change_currency('EUR')
    account.display_info()