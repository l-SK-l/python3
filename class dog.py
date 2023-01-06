class Dog:
    # Атрибут класса
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод экземпляра
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Другой метод экземпляра
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    
    def speak(self, sound='Arf'):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)


# miles = Dog('Miles', 4)
# print(miles)

# print(miles.speak('Woof Woof'))
# philo = Dog("Philo", 5, "brown")
# print(f"{philo.name}'s is {philo.coat_color}.")


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.age)
print(jack)
print(jim.speak('Gaff'))
print(miles.speak())
print(miles.speak('another Gaf'))
print(type(jack))
'''isinstance() получает два
аргумента, объект и класс. В данном случае isinstance()
проверяет, является ли miles экземпляром класса Dog, и
возвращает True.'''
print(isinstance(buddy, Dog))  
print(isinstance(miles, Bulldog))
print(isinstance(jack, Dachshund))
