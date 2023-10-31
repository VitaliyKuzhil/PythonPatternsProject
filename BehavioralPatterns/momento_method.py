import copy
from abc import ABC, abstractmethod


class Person:
    def __init__(self, first_name, last_name, passport, id_code):
        self.first_name = first_name
        self.last_name = last_name
        self.passport = passport
        self.id_code = id_code


class Originator(ABC):
    @abstractmethod
    def create_momento(self):
        pass

    @abstractmethod
    def restore_momento(self, momento):
        pass


class Momento(ABC):
    @abstractmethod
    def get_state(self):
        pass


class AccountOriginator(Originator):
    def __init__(self, person):
        self.name = (person.first_name, person.last_name)
        self.docs = (person.passport, person.id_code)
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount:.2f}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f'Balance: {self.balance:.2f}'

    def get_transactions(self):
        print('Transactions:')
        return "\n".join(reversed(self.transactions))

    def create_momento(self) -> Momento:
        return AccountMomento(self.balance, self.transactions)

    def restore_momento(self, momento) -> None:
        self.balance, self.transactions = momento.get_state()


class AccountMomento(Momento):
    def __init__(self, balance, transactions):
        self.balance = balance
        self.transactions = copy.copy(transactions)

    def get_state(self):
        return self.balance, self.transactions


class AccountCaretaker:
    def __init__(self, originator: AccountOriginator):
        self._originator = originator
        self._momentos = []

    def backup(self) -> None:
        self._momentos.append(self._originator.create_momento())

    def undo(self) -> None:
        if not self._momentos:
            print(f'Not momento')
        else:
            momento = self._momentos.pop()
            self._originator.restore_momento(momento)


if __name__ == '__main__':
    person1 = Person('Ivan', 'Ivanov', 'KT045863', 1324546547)

    account_person1 = AccountOriginator(person1)
    caretaker1 = AccountCaretaker(account_person1)

    account_person1.deposit(700)
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
    print()

    caretaker1.backup()

    account_person1.withdraw(300)
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
    print()

    account_person1.withdraw(500)
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
    print()

    caretaker1.backup()

    account_person1.deposit(100)
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
    print()

    caretaker1.undo()
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
    print()

    caretaker1.undo()
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
    print()

    caretaker1.undo()
    print(account_person1.get_balance())
    print(account_person1.get_transactions())
