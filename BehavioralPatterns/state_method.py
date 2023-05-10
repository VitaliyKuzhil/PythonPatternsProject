from abc import ABC, abstractmethod


class PackageState(ABC):
    @abstractmethod
    def process(self):
        pass


class NewPackage(PackageState):
    def process(self):
        print('New Package')
        return self


class WaiteProcessPackage(PackageState):
    def process(self):
        print('Package is waiting for processing')
        return self


class InProcessPackage(PackageState):
    def process(self):
        print('Package in the process of processing')
        return self


class ShippedPackage(PackageState):
    def process(self):
        print('Package has been sent')
        return self


class Package:
    def __init__(self, recipient_address, weight, size, description):
        self.recipient_address = recipient_address
        self.weight = weight
        self.size = size
        self.description = description
        self.__state = NewPackage().process()

    def change_state(self, current_state):
        self.__state = current_state

    def waite_process(self):
        self.change_state(WaiteProcessPackage().process())

    def in_process(self):
        self.change_state(InProcessPackage().process())

    def shipped(self):
        self.change_state(ShippedPackage().process())

    def print_sate(self):
        print(self.__state)

    def print_data(self):
        print(f'Address: {self.recipient_address}\n'
              f'Weight: {self.weight}\n'
              f'Size: {self.size}\n'
              f'Description: {self.description}\n'
              f'State: {self.__state}')


if __name__ == '__main__':
    package = Package('Main street, 1', 2.3, (20, 30, 40), 'books')
    package.print_data()
    print()

    package.waite_process()
    package.print_sate()
    print()

    package.in_process()
    package.print_sate()
    print()

    package.shipped()
    package.print_sate()
    print()
