import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

game = True

screen_x = 800
screen_y = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=screen_x, height=screen_y)
screen.tracer(0)
screen.listen()

paddle_r = Paddle(screen_x=screen_x,screen_y=screen_y )
paddle_l = Paddle(screen_x=screen_x,screen_y=screen_y , r="l")

screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")

ball = Ball()


while game:
    ball.seth(random.randint(0,160))

    while True:
        time.sleep(0.1)
        ball.move()
        screen.update()

        if (ball.ycor()>290 or ball.ycor() < -290):
            ball.bounce_y()
        if (ball.distance(paddle_r) < 50 and ball.xcor() > 360) :
            ball.bounce_x()










