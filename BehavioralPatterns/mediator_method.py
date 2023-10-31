from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def send(self, message: str, specific_sender):
        pass


class Handler(ABC):
    def __init__(self, handler_mediator: Mediator):
        self.mediator = handler_mediator

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass


class Manager(Handler):
    def send(self, message: str):
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"Менеджер: {message}")


class Kitchen(Handler):
    def send(self, message: str):
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"Кухня: {message}")


class Waiter(Handler):
    def send(self, message: str):
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"Офіціант: {message}")


class RestaurantMediator(Mediator):
    def __init__(self):
        self.manager = Manager(self)
        self.kitchen = Kitchen(self)
        self.waiter = Waiter(self)

    def send(self, message: str, specific_sender):
        try:
            if specific_sender == self.manager:
                self.manager.receive(message)

            elif specific_sender == self.kitchen:
                self.kitchen.receive(message)

            elif specific_sender == self.waiter:
                self.waiter.receive(message)

        except ValueError:
            print(f"Помилка: Невідомий відправник повідомлення")


if __name__ == '__main__':
    mediator = RestaurantMediator()

    mediator.manager.send("Замовлення для столу №3")
    mediator.kitchen.send("Замовлення для столу №3 - Виконано")
    mediator.waiter.send("Відношу замовлення столику №3")
