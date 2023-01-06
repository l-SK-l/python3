class Rectangle:
    # вне __init__ указываются атрибуты класса. 
    # будут иметь одно значения для всех экземпляров класса
    # Атрибут класса
    # species = "Canis familiaris"
    
    # метод
    def __init__(self, length, width):  # length и width параметры
        self.length = length  # .length и .width атрибуты экземпляров
        self.width = width  # они уникальны для каждого экземпляра


    def area(self):  # метод экземпляра
        return self.length * self.width


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length


square = Square(4)  #  инстанцирование объекта square класса Square
square.width = 5  # задаём свойству .width экземпляра Square занение 5
print(square.area())
