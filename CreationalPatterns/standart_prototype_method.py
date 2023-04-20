import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Person(Prototype):
    def __init__(self, first_name, last_name, friends):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__friends = friends

    def __str__(self):
        return f'Користувач: {self.__first_name} {self.__last_name} дружить з {self.__friends}'


if __name__ == '__main__':

    person1 = Person('Nazar', 'Petrushin', ['Vova', 'Andrii'])
    person2 = person1.clone()

    print(person1)
    print(person2)
