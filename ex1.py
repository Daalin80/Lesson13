from random import randint

class City:
    def __init__(self):
        self.streets = []
        self.quantity()

    def quantity(self):
        for i in range(1, randint(1, 10)):
            self.streets.append(Street(i))

    def print_city(self):
        for street in self.streets:
            print('Улица   Дом   Население')
            for house in street.houses:
                print(f'  {street.numbers}\t\t  {house.numbers}      {house.population}')

class Street:
    def __init__(self, numbers):
        self.numbers = numbers
        self.houses = []
        for i in range(1, randint(5, 20)):
            self.houses.append(House(i))

class House:
    def __init__(self, numbers):
        self.population = randint(1, 100)
        self.numbers = numbers

city = City()
city.print_city()