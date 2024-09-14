from turtle import Turtle, Screen
import snake
import food
import time
from scoreboard import Scoreboard

cobra = snake.Snake(6, 1)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

khana = food.Food()
screen.listen()
screen.onkey(key="Up", fun=cobra.move_up)
screen.onkey(key="Down", fun=cobra.move_down)
screen.onkey(key="Right", fun=cobra.move_right)
screen.onkey(key="Left", fun=cobra.move_left)
screen.update()

game = True

count = 0
level = Scoreboard()
level.update()

while game:
    if cobra.xcor() > 270 or cobra.xcor() < -270 or cobra.ycor() < -270 or cobra.ycor() > 270:
        level.game_over()
        game = False

    elif khana.distance(cobra.head) < 15:
        khana.respawn()
        cobra.eat(1)
        level.update()

    else:
        for i in cobra.segments[1:]:
            if cobra.head.distance(i) < 10:
                level.game_over()
                game = False

        cobra.move()
        screen.update()
        time.sleep(0.09)
screen.exitonclick()
