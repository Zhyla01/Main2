# (Завдання_1)

class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата карткою {amount} {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount} {self.currency}")


def create_payment():
    payment_type = input("Введіть тип платежу (CreditCard, PayPal, Crypto): ")
    currency = input("Введіть валюту: ")
    if payment_type.lower() == "creditcard":
        return CreditCardPayment(currency)
    elif payment_type.lower() == "paypal":
        return PayPalPayment(currency)
    elif payment_type.lower() == "crypto":
        return CryptoPayment(currency)
    else:
        print("Невірний тип платежу.")
        return None

def main():
    payments = []

    for _ in range(3):
        payment = create_payment()
        if payment:
            payments.append(payment)

    for payment in payments:
        amount = float(input("Введіть суму платежу: "))
        payment.pay(amount)


if __name__ == "__main__":
    main()