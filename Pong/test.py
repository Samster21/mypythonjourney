from turtle import Turtle, Screen
import random

pd = Turtle()
pd.color("white")
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)

pd.forward(100)
pd.seth(-30)
pd.forward(70)
pd.seth(30)
pd.forward((70))
screen.exitonclick()