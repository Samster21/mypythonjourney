from turtle import Turtle,Screen
import snake
import food
import time




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
scoreboard = Turtle()
scoreboard.teleport(y=270)
scoreboard.hideturtle()
scoreboard.color("white")

while game:
    if cobra.xcor() >270 or cobra.xcor() < -270 or cobra.ycor() < -270 or cobra.ycor() > 270:
        message = Turtle()
        message.penup()
        message.color("white")
        message.hideturtle()
        game = False
    else:
        for i in cobra.segments[1:]:
            if cobra.head.distance(i)<10:
                message = Turtle()
                message.penup()
                message.color("white")
                message.hideturtle()
                message.write(arg="Game Over!!!", align="center", font=("Arial", 16, "normal"))
                game = False
        if khana.distance(cobra.head) < 15:
            khana.respawn()
            cobra.eat(1)
            count += 1
            scoreboard.clear()
            scoreboard.write(arg=f"Score:{count}", align="center", font=("Arial", 16, "normal"))
        cobra.move()
        screen.update()
        time.sleep(0.1)
screen.exitonclick()



