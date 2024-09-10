from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen_x, screen_y, r="r"):
        super().__init__()
        self.color("white")
        self.hideturtle()
        if r == "l":
            self.teleport(-100,200) #-screen_x // 4, screen_y // 2 - 20)
        else:
            self.teleport(100,200) # screen_x // 4, screen_y // 2 - 20)
        self.score = 0

    def update(self):
        self.clear()
        self.write(self.score, align="center", font=("Arial", 80, "normal"))
