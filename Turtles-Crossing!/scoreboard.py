from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.goto(x=0,y=260)
        self.level = 0

    def update(self):
        self.clear()
        self.level += 1
        self.write(arg=self.level, align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game Over!", align="center", font=FONT)

