class Animal:

    sleep = False
    health = 100
    touch_back = None
    position = 0
    stuff_in_belly = 0

    def __init__(self, name, age, num_legs=4):
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.name} is {self.age} years old, he has {self.num_legs} legs"

    def walk(self, walk_increment):
        self.position = self.position + walk_increment
        return self.position

    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"

class Dog(Animal):

    health = 80

    def speak(self, sound='Gaf!'):
        return f"{self.name} barks: {sound}"


class Cat(Animal):
    health = 800

    def touch_back(self):
        return f'Murrrr, Murrr'

class Bird(Animal):
    
    def __init__(self, name, age, num_legs=2):
        super().__init__(name, age, num_legs)
        self.num_legs = num_legs

    def speak(self, sound='Popka durak'):
            return f"{self.name} speak: {sound}!"

bush = Dog('Bush', 3)
parrot = Bird('Kesha', 1)
elfa = Cat('Elfa', 2)
print(bush.health)
print(parrot)
print(parrot.speak())
print(elfa.touch_back())
print(parrot.touch_back)
print(bush.is_hungry())
print(f"{elfa.name} is at position {elfa.walk(2)}.")