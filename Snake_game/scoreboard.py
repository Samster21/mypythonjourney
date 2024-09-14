from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.teleport(x=0, y=270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(arg=f"Score = {self.score}   High Score = {self.high_score}",
                   align="center", font=("Arial", 16, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score}   High Score = {self.high_score}",
                   align="center", font=("Arial", 16, "normal"))

    def score_reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
