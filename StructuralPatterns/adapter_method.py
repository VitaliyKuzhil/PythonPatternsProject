class Bus:
    @staticmethod
    def moving():
        print("Driving a Bus")


class Train:
    @staticmethod
    def moving():
        print("Driving a Train")


class Plain:
    @staticmethod
    def moving():
        print("Driving a Plain")


class TransportAdapter(Bus, Train, Plain):
    def __init__(self, transport_type):
        self.transport_type = transport_type

    def drive(self):
        return self.transport_type.moving()


if __name__ == '__main__':
    # Example usage
    bus = Bus()
    train = Train()
    plain = Plain()

    bus_adapter = TransportAdapter(bus)
    train_adapter = TransportAdapter(train)
    plain_adapter = TransportAdapter(plain)

    bus_adapter.drive()
    train_adapter.drive()
    plain_adapter.drive()
