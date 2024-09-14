from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x=0, y=270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.level = 0

    def update(self):
        self.clear()
        self.write(arg=(self.level + 1), align="center", font=("Arial", 16, "normal"))
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="Game Over!!!", align="center", font=("Arial", 16, "normal"))
