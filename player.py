# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.move_distance = 10
        self.finish_line = 280

    def up(self):
        self.forward(self.move_distance)

    def win_situation(self):
        self.penup()
        self.goto(0, -280)
