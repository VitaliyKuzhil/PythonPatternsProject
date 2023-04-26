from abc import ABC


class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_cost(self):
        return self.price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items)
        return total_cost


class PromoCode:
    def __init__(self, cart):
        self.cart = cart

    def get_total_cost(self):
        total_cost = self.cart.get_total_cost()  # використовуємо кешоване значення
        return total_cost * 0.8  # знижка 20%


if __name__ == '__main__':

    t_shirt = Item('Футболка', 20)
    pants = Item('Штани', 50)
    shorts = Item('Шорти', 30)

    my_cart = Cart()

    my_cart.add_item(t_shirt)
    my_cart.add_item(pants)
    my_cart.add_item(shorts)

    my_promo_code = PromoCode(my_cart)

    print(f'Вартість без знижки: {my_cart.get_total_cost()} грн')
    print(f'Вартість зі знижкою: {my_promo_code.get_total_cost()} грн')
