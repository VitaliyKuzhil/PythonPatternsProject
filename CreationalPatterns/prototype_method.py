import copy


class Person:
    def __init__(self, first_name, last_name, friends):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = friends

    def add_friend(self, friend):
        self.friends.extend(friend)

    def delete_friend(self, friend):
        if friend in self.friends:
            self.friends.pop(self.friends.index(friend))

    def __str__(self):
        return f"Користувач: {self.first_name} {self.last_name} дружить з {self.friends}"


class PersonPrototype:
    def __init__(self):
        self._user = {}

    def add_person(self, name, obj):
        self._user[name] = obj

    def delete_person(self, name):
        del self._user[name]

    def clone(self, old_person, **kwargs):
        person = copy.copy(self._user.get(old_person))
        person.__dict__.update(kwargs)
        return person

    def print_users(self):
        for user in self._user.values():
            print(user)


prototype = PersonPrototype()

person1 = Person("Nazar", "Petrushin", ['Vova', 'Andrii'])
prototype.add_person('person1', person1)
print(person1)

person1.add_friend(['Anatoliy', 'Vasia'])
print(person1)

person2 = prototype.clone('person1', first_name='Michola', last_name='Dolhii', friends=['Petia', 'Dima'])
prototype.add_person('person2', person2)
print(person2)

person2.add_friend(['Maxim', 'Roman'])
print(person2)

person2.delete_friend('Dima')
print(person2)

prototype.delete_person('person2')

print()
prototype.print_users()
