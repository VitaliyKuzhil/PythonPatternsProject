from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class MenuItem(Component):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_description(self):
        return self._name

    def get_price(self):
        return self._price


class Order(Component):
    def __init__(self, components):
        self._components = components

    def get_description(self):
        description = ""
        for component in self._components:
            description += f" -- {component.get_description()} : {component.get_price()}$\n"
        return description

    def get_price(self):
        price = 0
        for component in self._components:
            price += component.get_price()
        return price


# Composites
class RestaurantOrder(Order):
    def __init__(self, components):
        super().__init__(components)
        self._components = components


class BarOrder(Order):
    def __init__(self, components):
        super().__init__(components)
        self._components = components


if __name__ == '__main__':
    burger = MenuItem("Pizza", 10)
    fries = MenuItem("Fries", 5)
    salad = MenuItem("Salad", 7)
    cola = MenuItem("Cola", 3)
    beer = MenuItem("Beer", 5)
    wine = MenuItem("Wine", 8)

    restaurant_order = RestaurantOrder((burger, fries, salad, cola))
    bar_order = BarOrder((beer, wine))

    print("Restaurant order:")
    print(restaurant_order.get_description())
    print(f"Price of Restaurant: {restaurant_order.get_price()}$\n")

    print("Bar order:")
    print(bar_order.get_description())
    print(f"Price of Bar: {bar_order.get_price()}$")
