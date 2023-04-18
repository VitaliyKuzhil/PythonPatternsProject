class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        return sum([item.price for item in self.items])


class Delivery:
    def __init__(self):
        self.address = None

    def set_address(self, address):
        self.address = address

    def deliver(self):
        print(f'Delivery to {self.address}')


class Payment:
    def __init__(self):
        self.amount = 0

    def set_amount(self, amount):
        self.amount = amount

    def pay(self):
        print(f'Need to pay --> {self.amount}')


class OrderFacade:
    def __init__(self):
        self.cart = ShoppingCart()
        self.delivery = Delivery()
        self.payment = Payment()

    def add_to_cart(self, product):
        self.cart.add_item(product)

    def remove_from_cart(self, product):
        self.cart.remove_item(product)

    def delivery_address(self, address):
        self.delivery.set_address(address)

    def set_payment_amount(self, amount):
        self.payment.set_amount(amount)

    def order(self):
        total = self.cart.calculate_total()
        self.set_payment_amount(total)
        self.delivery.deliver()
        self.payment.pay()

        print('Order successfully')


if __name__ == '__main__':
    product1 = Product('Laptop', 1000)
    product2 = Product('Mouse', 20)

    client = OrderFacade()

    client.add_to_cart(product1)
    client.add_to_cart(product2)
    client.delivery_address('Main, 123a')
    client.order()

