from abc import abstractmethod, ABC

''' Компінії по наданню туристичних послуг потрібно розширити способи доставки туристів на локації.
Коли компанія була меншою, їй потрібен був тільки Потяг. Але тепер компанія готова розширювати свої послуги,
тому надає послуги за кордоном, куди немає сполучення потягом.
Нам потрібно добавити ще один тип доставки пасажирів на локації і це буде Літак '''


''' Загальний Інтерфейс для створення продукту '''


class Product(ABC):
    def __init__(self):
        self.name = 'Product'


''' Реалізація Інтерфейса його підкласами '''


# Перевизначення методу ініціалізації продукту
class Train(Product):
    def __init__(self):
        super().__init__()
        self.name = 'Train'


# Перевизначення методу ініціалізації продукту
class Plane(Product):
    def __init__(self):
        super().__init__()
        self.name = 'Plain'


''' Інтерфейс Creator оголошує фабричний метод trevel,
 який повертає об'єкт класу Product, а метод some_operation повертає фактичне імя Product'''


class Creator(ABC):
    @abstractmethod
    def trevel(self) -> Product:
        pass

    def some_operation(self):
        return self.trevel().name

    def __str__(self):
        return f'Trevel: {self.some_operation()}'


''' Перевизначення фабричного методу підкласами класу Creator'''


class FactoryTrain(Creator):
    def trevel(self) -> Product:
        return Train()


class FactoryPlain(Creator):
    def trevel(self) -> Product:
        return Plane()


def client_code(move: str) -> None:
    tour_company = {'T': FactoryTrain(), 'P': FactoryPlain()}
    return tour_company[move]


if __name__ == '__main__':
    print(client_code(input('T = Train or P = Plain \n').upper()))
