class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # Метод экземпляра
    def drive(self, miles):
        self.mileage += miles

blue_car = Car('blue', 20000)
red_car = Car('red', 30000)
print(f'The {blue_car.color} car has {blue_car.mileage:,d} miles.')
print(f'The {red_car.color} car has {red_car.mileage:,d} miles.')

black_car = Car('Black', 0)
print(f'The {black_car.color} car has {black_car.mileage:,d} miles.')
black_car.drive(100)
black_car.drive(200)
print(black_car.mileage)



