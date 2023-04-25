from abc import ABC, abstractmethod


class CreditRequest:
    def __init__(self, name, credit_score, income, mounth, amount):
        self.name = name
        self.credit_score = credit_score
        self.income = income
        self.mounth = mounth
        self.amount = amount


class Handler(ABC):
    @abstractmethod
    def permit(self, client):
        pass


class IncomeHandler(Handler):
    def permit(self, client):
        if client.income >= (client.amount / client.mounth) / 0.5:
            print(f'{client.name} має достатній рівень доходів')
            return True
        else:
            print(f'{client.name} не має достатнього рівеня доходів')
            return False


class CreditHandler(Handler):
    def permit(self, client):
        if client.credit_score > 500:
            print(f'В {client.name} хороший кредитний рейтинг')
            return True

        else:
            print(f'В {client.name} поганий кредитний рейтинг')
            return False


class CreditManager:
    handlers = [IncomeHandler(), CreditHandler()]  # List HANDLERS

    def permit(self, client):
        for handler in self.handlers:
            if not handler.permit(client):
                print(f"Клієнт {client.name} не може отримати {client.amount}$")
                return
        print(f"Клієнт {client.name} може отримати {client.amount}")


if __name__ == '__main__':
    client1 = CreditRequest('Artur', 700, 15000, 24, 75000)
    client2 = CreditRequest('Vasia', 500, 25000, 12, 100000)
    client3 = CreditRequest('Vova', 600, 10000, 36, 260000)

    credit_manager = CreditManager()

    credit_manager.permit(client1)
    print()
    credit_manager.permit(client2)
    print()
    credit_manager.permit(client3)
