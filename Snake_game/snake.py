from turtle import Turtle, Screen


class Snake:

    def __init__(self, length, speed):
        self.segments = []
        self.length = length
        for _ in range(length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.speed(speed)
            new_turtle.penup()
            new_turtle.goto(x=-20 * _, y=0)
            self.segments.append(new_turtle)
        self.head = self.segments[0]

    def xcor(self):
        return self.head.xcor()

    def ycor(self):
        return self.head.ycor()

    def move_right(self):
        if self.head.heading() == 270:
            self.head.left(90)
        elif self.head.heading() == 90:
            self.head.right(90)

    def move_left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)

    def move_up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def move_down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180.0:
            self.head.left(90)



    def move(self):
        for i in range(self.length - 1, 0, -1):
            new_position = self.segments[i - 1].pos()
            self.segments[i].goto(new_position)
        self.head.forward(20)

    def eat(self, speed):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.speed(speed)
        new_turtle.penup()
        new_turtle.goto(self.segments[self.length - 1].pos())
        self.length += 1
        self.segments.append(new_turtle)

    def retry(self):
        return True
