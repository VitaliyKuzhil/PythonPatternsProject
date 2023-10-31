from abc import ABC, abstractmethod


class Command(ABC):  # Command
    def __init__(self, tv):
        self.tv = tv

    @abstractmethod
    def execute(self):
        pass


class TurnOn(Command):  # Concrete Command
    def execute(self):
        self.tv.turn_on()


class TurnOff(Command):  # Concrete Command
    def execute(self):
        self.tv.turn_off()


class ChangeChannel(Command):  # Concrete Command
    def __init__(self, tv):
        super().__init__(tv)
        self.tv = tv
        self.channel = None

    def set_channel(self, channel):
        self.channel = channel

    def execute(self):
        if self.channel is not None:
            self.tv.change_channel(self.channel)


class IncreaseVolume(Command):  # Concrete Command
    def execute(self):
        self.tv.increase_volume()


class DecreaseVolume(Command):  # Concrete Command
    def execute(self):
        self.tv.decrease_volume()


class TV:  # Receiver
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.volume = 50

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def change_channel(self, channel):
        if 0 < self.channel < 1000:
            self.channel = channel

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def __str__(self):
        return f'TV is {"On" if self.is_on else "Off"}, chanel: {self.channel}, volume: {self.volume}'


class Remote:  # Invoker
    def __init__(self):
        self.command = None

    def get_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


if __name__ == '__main__':
    tv = TV()

    turn_on = TurnOn(tv)
    turn_off = TurnOff(tv)
    change_channel = ChangeChannel(tv)
    increase_volume = IncreaseVolume(tv)
    decrease_volume = DecreaseVolume(tv)
    print(tv)
    print()

    remote_control = Remote()

    remote_control.get_command(turn_on)
    remote_control.execute_command()
    change_channel.set_channel(5)
    remote_control.get_command(change_channel)
    remote_control.execute_command()
    remote_control.get_command(increase_volume)
    remote_control.execute_command()
    print(tv)
    print()

    change_channel.set_channel(7)
    remote_control.get_command(change_channel)
    remote_control.execute_command()
    remote_control.get_command(decrease_volume)
    remote_control.execute_command()
    remote_control.get_command(decrease_volume)
    remote_control.execute_command()
    print(tv)
    print()

    remote_control.get_command(turn_off)
    remote_control.execute_command()
    print(tv)
