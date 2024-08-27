from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.goto(randint(-280, 280), randint(-280, 280))

    def respawn(self):
        self.hideturtle()
        self.goto(randint(-280, 280), randint(-280, 280))
        self.showturtle()
