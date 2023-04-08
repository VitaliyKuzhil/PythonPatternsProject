from abc import ABC, abstractmethod

''' Загальний Інтерфейс для створення продукту '''


class Transport(ABC):
    def __init__(self):
        self.type = 'Transport'

    def __str__(self):
        return f'  *  Create {self.type}'


''' Різновиди Інтерфейсів для створення продукту '''


# Продукт 1
class Car(Transport):
    def __init__(self):
        super().__init__()
        self.type = "Car"


# Перший різновид продукту №1
class StandardCar(Car):
    def __init__(self):
        super().__init__()
        self.type = 'StandardCar'


# Другий різновид продукту №1
class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.type = 'SportCar'


# Продукт 2
class Motorcycle(Transport):
    def __init__(self):
        super().__init__()
        self.type = 'Motorcycle'


# Перший різновид продукту №2
class StandardMotorcycle(Motorcycle):
    def __init__(self):
        super().__init__()
        self.type = 'StandardMotorcycle'


# Другий різновид продукту №2
class SportMotorcycle(Motorcycle):
    def __init__(self):
        super().__init__()
        self.type = 'SportMotorcycle'


''' Загальний Інтерфейс Транспортної Фабрики '''


class TransportFactory(ABC):
    # Фабричний метод 1
    @abstractmethod
    def create_car(self):
        pass

    # Фабричний метод 2
    @abstractmethod
    def create_motorcycle(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} create:'


# Транспортна Фабрика №1
class StandardTransportFactory(TransportFactory):
    def create_car(self):
        return StandardCar()

    def create_motorcycle(self):
        return StandardMotorcycle()


# Транспортна Фабрика №2
class SportTransportFactory(TransportFactory):
    def create_car(self):
        return SportCar()

    def create_motorcycle(self):
        return SportMotorcycle()


if __name__ == '__main__':
    # Створення СТАНДАРТНИХ продуктів
    standart_product = StandardTransportFactory()
    print(standart_product)

    standart_car = standart_product.create_car()
    standart_motorcycle = standart_product.create_motorcycle()
    print(standart_car)
    print(standart_motorcycle)

    # Створення Спортивних продуктів
    sport_product = SportTransportFactory()
    print(sport_product)

    sport_car = sport_product.create_car()
    sport_motorcycle = sport_product.create_motorcycle()
    print(sport_car)
    print(sport_motorcycle)
