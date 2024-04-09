class Dog:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:

    """A simple cat class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


"""The factory method"""


def get_pet(pet="dog"):

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


'''Test Script'''

d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())
