from turtle import Turtle, Screen


class SnakeBody(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(speed)
        self.penup()


class Snake:
    def __init__(self, length, speed):
        self.head = None
        self.segments = []
        self.initial_length = length
        self.length = length
        self.speed = speed

    def create_snake(self):
        for _ in range(self.initial_length):
            new_turtle = SnakeBody(speed=self.speed)
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
        for i in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[i - 1].pos()
            self.segments[i].goto(new_position[0], new_position[1])
        self.head.forward(20)

    def eat(self, speed):
        new_turtle = SnakeBody(speed=speed)
        position = self.segments[len(self.segments)-1].pos()
        new_turtle.teleport(position[0],position[1])
        self.segments.append(new_turtle)

    def snake_reset(self):
        for _ in self.segments:
            _.teleport(1000,1000)
        self.segments.clear()
        self.length = self.initial_length
        self.create_snake()
