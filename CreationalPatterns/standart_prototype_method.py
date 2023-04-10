import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Person(Prototype):
    def __init__(self, first_name, last_name, friends):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = friends

    def __str__(self):
        return f'Користувач: {self.first_name} {self.last_name} дружить з {self.friends}'


person1 = Person('Nazar', 'Petrushin', ['Vova', 'Andrii'])
person2 = person1.clone()

print(person1)
print(person2)
