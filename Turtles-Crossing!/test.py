from turtle import Turtle, Screen

screen = Screen()

turtle = Turtle()
turtle.shape("square")
turtle.shapesize(stretch_len=1,stretch_wid=5)
print(turtle.heading())
turtle.seth(180)
turtle.forward(100)



screen.exitonclick()