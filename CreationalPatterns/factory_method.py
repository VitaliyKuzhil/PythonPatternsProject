from abc import abstractmethod, ABC

''' Загальний Інтерфейс для створення продукту '''


class Product:
    def __init__(self, name):
        self.name = name


''' Реалізація Інтерфейса його підкласами '''


# Перевизначення методу ініціалізації продукту
class Train(Product):
    def __init__(self):
        self.name = 'Train'
        super().__init__(self.name)


# Перевизначення методу ініціалізації продукту
class Plane(Product):
    def __init__(self):
        self.name = 'Plain'
        super().__init__(self.name)


''' Інтерфейс Creator оголошує фабричний метод trevel,
 який повертає об'єкт класу Product, а метод some_operation повертає фактичне імя Product'''


class Creator:
    @abstractmethod
    def trevel(self) -> Product:
        pass

    @abstractmethod
    def some_operation(self):
        return self.trevel().name

    def __str__(self):
        return f'Trevel: {self.some_operation()}'


''' Перевизначення фабричного методу підкласами класу Creator'''


class FactoryTrain(Creator, ABC):
    def trevel(self) -> Product:
        return Train()


class FactoryPlain(Creator, ABC):
    def trevel(self) -> Product:
        return Plane()


def client_code(move: str) -> None:
    tour_company = {'T': FactoryTrain, 'P': FactoryPlain}
    return tour_company[move]()


if __name__ == '__main__':
    print(client_code(input('T = Train or P = Plain \n').upper()))


''' Припустимо, компінії по наданню туристичних послуг потрібно розширити способи доставки туристів на локації.
Коли компанія була меншою, їй потрібен був тільки Потяг. Але тепер компанія готова розширювати свої послуги,
тому надає послуги за кордоном, куди немає сполучення потягом. тиким чином ми добавили Літак, як ще один спосіб доставки
пасажирів на локації '''
