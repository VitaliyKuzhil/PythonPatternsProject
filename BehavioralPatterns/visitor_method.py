from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_teeth_cleaning(self, teeth_cleaning):
        pass

    @abstractmethod
    def visit_filling(self, filling):
        pass

    @abstractmethod
    def visit_root_canal(self, root_canal):
        pass


class DentalProcedure(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class TeethCleaning(DentalProcedure):
    def accept(self, visitor):
        visitor.visit_teeth_cleaning(self)

    def get_cost(self):
        return 100


class Filling(DentalProcedure):
    def accept(self, visitor):
        visitor.visit_filling(self)

    def get_cost(self):
        return 200


class RootCanal(DentalProcedure):
    def accept(self, visitor):
        visitor.visit_root_canal(self)

    def get_cost(self):
        return 500


class DentalVisitor(Visitor):
    def __init__(self):
        self.total_cost = 0

    def visit_teeth_cleaning(self, teeth_cleaning):
        self.total_cost += teeth_cleaning.get_cost()

    def visit_filling(self, filling):
        self.total_cost += filling.get_cost()

    def visit_root_canal(self, root_canal):
        self.total_cost += root_canal.get_cost()

    def get_total_cost(self):
        return self.total_cost


if __name__ == "__main__":
    teeth_cleaning = TeethCleaning()
    filling = Filling()
    root_canal = RootCanal()

    visitor = DentalVisitor()

    teeth_cleaning.accept(visitor)
    filling.accept(visitor)
    root_canal.accept(visitor)

    print(f'Total cost: {visitor.get_total_cost()} $')
