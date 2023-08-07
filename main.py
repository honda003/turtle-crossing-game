import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
#  Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Calling cars
x = CarManager()

# Calling player
y = Player()

# Calling score
z = ScoreBoard()

# Screen commands
screen.listen()
screen.onkey(y.up, "Up")

# Game
game_is_on = True
while game_is_on:
    z.level()
    time.sleep(0.1)
    screen.update()
    x.create_car()
    x.move()
    for car in x.cars:
        if car.distance(y) < 25:
            game_is_on = False
            z.game_over()

    if y.ycor() == 280:
        y.win_situation()
        z.next_level()
        x.winwin()

screen.exitonclick()



