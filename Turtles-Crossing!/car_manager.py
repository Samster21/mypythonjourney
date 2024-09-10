from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
    def generate(self):
        chance = randint(a=1,b=6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            self.all_cars.append(car)
            car.color(choice(COLORS))
            car.penup()
            car.move_speed = STARTING_MOVE_DISTANCE
            car.teleport(x=270, y=randint(a=-250,b=250))

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increment(self):
        self.move_speed += MOVE_INCREMENT


