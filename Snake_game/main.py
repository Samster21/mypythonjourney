from turtle import Turtle, Screen
from snake import Snake
import food
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

cobra = Snake(6, 1)
cobra.create_snake()

khana = food.Food()

screen.listen()
screen.onkey(key="Up", fun=cobra.move_up)
screen.onkey(key="Down", fun=cobra.move_down)
screen.onkey(key="Right", fun=cobra.move_right)
screen.onkey(key="Left", fun=cobra.move_left)
screen.update()


level = Scoreboard()

while True:

    if cobra.xcor() > 270 or cobra.xcor() < -270 or cobra.ycor() < -270 or cobra.ycor() > 270:
        level.score_reset()
        cobra.snake_reset()
        sleep(2)
        # game = screen.textinput(title="Snake",
        #                         prompt="Do you wish to continue? Press Y to continue, and any other key to Quit")
        # if game == "Y" or game == "y":
        #     pass
        # else:
        #     break

    elif khana.distance(cobra.head) < 15:
        khana.respawn()
        cobra.eat(1)
        level.increase_score()

    else:
        for i in cobra.segments[1:]:
            if cobra.head.distance(i) < 10:
                level.score_reset()
                cobra.snake_reset()
                sleep(2)

        cobra.move()
        screen.update()
        sleep(0.09)
