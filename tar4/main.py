from classes.car import Car
from classes.engine import Engine

car = Car("Mazda", Engine(150))
print(car.start())