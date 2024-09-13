import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(key="Up", fun=player.move)

game_is_on = True

cars = CarManager()

level = Scoreboard()
level.update()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            level.game_over()

    if player.ycor() > 280:
        level.update()
        cars.increment()
        player.revert()



screen.exitonclick()