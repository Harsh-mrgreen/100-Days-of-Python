import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car()
    car.move_car()
    if player.ycor() >= FINISH_LINE_Y:
        player.levelup()
        car.levelup()
        score.levelup()
        
    for model in car.cars:
        if model.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()