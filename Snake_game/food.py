from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()


    def respawn(self):
        self.teleport(randint(-250, 250), randint(-250, 250))

