class Transport:
    def __init__(self, transport_type):
        self.transport_type = transport_type

    def can_cross(self, bridge):
        return f'Can {self.transport_type} cross {bridge.__class__.__name__}?' \
               f' --> {"Yes" if bridge.can_cross(self) else "No"}'


class Car(Transport):
    def __init__(self):
        super().__init__(__class__.__name__)


class Bus(Transport):
    def __init__(self):
        super().__init__(__class__.__name__)


class Truck(Transport):
    def __init__(self):
        super().__init__(__class__.__name__)


class Motorcycle(Transport):
    def __init__(self):
        super().__init__(__class__.__name__)


class Train(Transport):
    def __init__(self):
        super().__init__(__class__.__name__)


class Bridge:
    def __init__(self):
        self.allowed_transport_types = set()

    def can_cross(self, transport):
        return transport.transport_type in self.allowed_transport_types


class RoadBridge(Bridge):
    def __init__(self):
        super().__init__()
        self.allowed_transport_types = ('Car', 'Bus', 'Truck', 'Motorcycle')


class RailwayBridge(Bridge):
    def __init__(self):
        super().__init__()
        self.allowed_transport_types = ('Train', 'Motorcycle')


if __name__ == '__main__':
    # Example usage

    car = Car()
    train = Train()
    motorcycle = Motorcycle()

    road_bridge = RoadBridge()
    railway_bridge = RailwayBridge()

    print(car.can_cross(road_bridge))
    print(car.can_cross(railway_bridge))

    print(train.can_cross(road_bridge))
    print(train.can_cross(railway_bridge))

    print(motorcycle.can_cross(road_bridge))
    print(motorcycle.can_cross(railway_bridge))

