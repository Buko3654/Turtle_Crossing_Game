import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.drive()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.score_up()
        car_manager.speed_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
