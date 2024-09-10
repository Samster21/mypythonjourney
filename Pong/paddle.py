from turtle import Turtle


# class Paddle():
#     def __init__(self,abcissa):
#         self.segments = []
#         for i in range(3):
#             turtle = Turtle()
#             turtle.hideturtle()
#             turtle.color("white")
#             turtle.shape("square")
#             turtle.penup()
#             turtle.seth(90)
#             self.segments.append(turtle)
#         ordinate = 10
#         for i in range(3):
#             self.segments[i].goto(abcissa, ordinate)
#             ordinate -= 10
#             self.segments[i].showturtle()
#
#         self.top = self.segments[0]
#         self.bottom = self.segments[2]
#
#
#     def move_up(self,distance):
#         if int(self.top.ycor()) < distance-10:
#             for i in range(2, 0, -1):
#                 new_position = self.segments[i - 1].pos()
#                 self.segments[i].goto(new_position)
#             self.top.forward(10)
#
#
#     def move_down(self,distance):
#         if int(self.bottom.ycor()) > distance +10:
#             for i in range(2):
#                 new_position = self.segments[i + 1].pos()
#                 self.segments[i].goto(new_position)
#             self.bottom.backward(10)
class Paddle(Turtle):
    # Gets the screen co-ordinates, and calculates xpos automatically.
    # The r parameter is a default parameter, for right/left positioning of the paddle

    def __init__(self, screen_x, screen_y, r="r"):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        if r == "l":
            self.goto(x=-screen_x//2 + 20, y=0)
        else:
            self.goto(x=screen_x//2 - 20, y=0)
        self.showturtle()
        self.y_lim = screen_y // 2 - screen_y // 12

    def up(self):
        if self.ycor() < self.y_lim:
            self.goto(self.xcor(), self.ycor() + 10)

    def down(self):
        if self.ycor() > -self.y_lim:
            self.goto(self.xcor(), self.ycor() - 10)
