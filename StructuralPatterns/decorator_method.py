class Item:
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

    def get_items(self):
        return self.items

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items)
        return total_cost


class PromoCode:
    def __init__(self, cart):
        self.cart = cart

    def get_total_cost(self):
        total_cost = self.cart.get_total_cost()  # використовуємо кешоване значення
        return total_cost * 0.8  # знижка 20%


my_cart = Cart()
my_cart.add_item(Item("Футболка", 20))
my_cart.add_item(Item("Штани", 50))
my_cart.add_item(Item("Шорти", 30))

my_promo_code = PromoCode(my_cart)

print(f"Вартість без знижки: {my_cart.get_total_cost()} грн")
print(f"Вартість зі знижкою: {my_promo_code.get_total_cost()} грн")


