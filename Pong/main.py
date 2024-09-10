import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game = True

screen_x = 800
screen_y = 600
bounce_boundary = screen_y//2 - 20 #20 accounts for the size of the ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=screen_x, height=screen_y)
screen.tracer(0)
screen.listen()

paddle_r = Paddle(screen_x=screen_x, screen_y=screen_y)
paddle_l = Paddle(screen_x=screen_x, screen_y=screen_y, r="l")

screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")

ball = Ball()

lines = Turtle()
lines.color("white")
lines.hideturtle()
lines.teleport(x=0, y=-270)
lines.seth(90)

for i in range(12):
    lines.forward(25)
    lines.penup()
    lines.forward(25)
    lines.pendown()

r_score = Scoreboard(screen_x=screen_x, screen_y=screen_y)
l_score = Scoreboard(screen_x=screen_x, screen_y=screen_y, r="l")

while game:
    ball.home()
    ball.seth(random.randint(0, 160))

    while True:
        time.sleep(0.1)
        ball.move()
        screen.update()

        if ball.ycor() > bounce_boundary or ball.ycor() < -bounce_boundary:
            ball.bounce_y()

        elif (ball.distance(paddle_r) < 50 and ball.xcor() > 360) or (
                ball.distance(paddle_l) < 50 and ball.xcor() < -360):
            ball.bounce_x()

        elif ball.distance(paddle_r) > 50 and ball.xcor() > 360:
            l_score.score += 1
            l_score.update()
            break

        elif ball.distance(paddle_l) > 50 and ball.xcor() < -360:
            r_score.score += 1
            r_score.update()
            break
