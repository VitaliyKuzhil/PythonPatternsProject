from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, robot_type):
        self.robot_type = robot_type

    def take_on(self):
        print(f"{self.robot_type} is Powering on... ")

    def charge_up(self):
        print(f"{self.robot_type} is Charging...")

    def check_container(self):
        print(f"{self.robot_type} is Checking container...")

    @abstractmethod
    def execute_command(self, command):
        pass

    def take_off(self):
        print(f"{self.robot_type} is Powering off...")


class Cleaner(Robot):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.command_mapping = {
            "take_on": self.take_on,
            "clean_up": self.clean_up,
            "charge_up": self.charge_up,
            "check_container": self.check_container,
            "take_off": self.take_off,
        }

    def execute_command(self, command):
        if command not in self.command_mapping:
            print(f"{self.robot_type} robot does not support {command} command.")
            return
        self.command_mapping[command]()

    def clean_up(self):
        print(f"{self.robot_type} is Cleaning up...")


class Washer(Robot):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.command_mapping = {
            "take_on": self.take_on,
            "wash_up": self.wash_up,
            "charge_up": self.charge_up,
            "set_water": self.set_water,
            "check_container": self.check_container,
            "take_off": self.take_off
        }

    def execute_command(self, command):
        if command not in self.command_mapping:
            print(f"{self.robot_type} robot does not support {command} command.")
            return
        self.command_mapping[command]()

    def wash_up(self):
        print(f"{self.robot_type} is Washing up...")

    def set_water(self):
        print(f"{self.robot_type} is Setting water...")


if __name__ == '__main__':
    # Creating an instance of CleanerRobot and executing its commands
    cleaner = Cleaner()

    cleaner.execute_command("take_on")
    cleaner.execute_command("clean_up")
    cleaner.execute_command("charge_up")
    cleaner.execute_command("check_container")
    cleaner.execute_command("jump")
    cleaner.execute_command("take_off")
    print()

    # Creating an instance of WasherRobot and executing its commands
    washer = Washer()

    washer.execute_command("take_on")
    washer.execute_command("wash_up")
    washer.execute_command("charge_up")
    washer.execute_command("set_water")
    washer.execute_command("check_container")
    washer.execute_command("dance")
    washer.execute_command("take_off")
