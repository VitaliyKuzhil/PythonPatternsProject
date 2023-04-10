from abc import ABC, abstractmethod


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.toppings = [] or None
        self.sauce = None

    def __str__(self):
        return f'{self.name} pizza \n  * {self.dough} dough \n  * {self.sauce} sauce \n' \
               f'  * {" ".join(self.toppings)} toppings'


class PizzaBuilder(ABC):
    @abstractmethod
    def set_dough(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_toppings(self):
        pass


class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()
        self.pizza = Pizza("Margherita")

    def set_dough(self):
        self.pizza.dough = "thin crust"

    def set_sauce(self):
        self.pizza.sauce = "tomato"

    def set_toppings(self):
        self.pizza.toppings = ["mozzarella cheese", "fresh basil"]

    def get_pizza(self):
        return self.pizza


class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()
        self.pizza = Pizza("Pepperoni")

    def set_dough(self):
        self.pizza.dough = "thick crust"

    def set_sauce(self):
        self.pizza.sauce = "tomato"

    def set_toppings(self):
        self.pizza.toppings = ["mozzarella cheese", "pepperoni"]

    def get_pizza(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_pizza(self):
        self.builder.set_dough()
        self.builder.set_sauce()
        self.builder.set_toppings()
        return self.builder.get_pizza()


if __name__ == "__main__":
    margherita = MargheritaPizzaBuilder()
    pepperoni = PepperoniPizzaBuilder()

    director = PizzaDirector(margherita)
    director.build_pizza()
    print(f'Take --> {margherita.get_pizza()}')

    director = PizzaDirector(pepperoni)
    director.build_pizza()
    print(f'Take --> {pepperoni.get_pizza()}')
