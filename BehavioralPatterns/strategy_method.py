from abc import ABC, abstractmethod


class BankStrategy(ABC):  # Strategy
    @abstractmethod
    def calculate_commission(self, amount):
        pass


class PrivatBank(BankStrategy):  # Concrete Strategy
    def calculate_commission(self, amount):
        return amount * 0.03


class OschadBank(BankStrategy):  # Concrete Strategy
    def calculate_commission(self, amount):
        return amount * 0.015


class UkrsibBank(BankStrategy):  # Concrete Strategy
    def calculate_commission(self, amount):
        return amount * 0.025


class PaymentSystem:  # Context
    def __init__(self):
        self._bank_strategy = None

    def set_strategy(self, strategy: BankStrategy):
        self._bank_strategy = strategy

    def make_payment(self, amount):
        if self._bank_strategy is None:
            raise ValueError("No strategy set")
        commission = self._bank_strategy.calculate_commission(amount)
        total_amount = amount + commission
        print(f'Bank: {self._bank_strategy.__class__.__name__}')
        print(f'Making payment of {amount} UAH with commission of {commission} UAH. Total amount: {total_amount} UAH.')
        print()


if __name__ == '__main__':
    client = PaymentSystem()

    # ПриватБанк
    client.set_strategy(PrivatBank())
    client.make_payment(1000)

    # ОщадБанк
    client.set_strategy(OschadBank())
    client.make_payment(1000)

    # Укрсіббанк
    client.set_strategy(UkrsibBank())
    client.make_payment(1000)
