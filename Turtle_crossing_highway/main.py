from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car.create_car()
    car.move()

    # Check to see if turtle has reached 300, if yes, reset position, update scoreboard, increase car speed.
    if player.ycor() > 300:
        player.reset_position()
        scoreboard.update_scoreboard()
        car.next_level()

    # Check to see if player hit any car
    for each_car in car.cars:
        if each_car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
