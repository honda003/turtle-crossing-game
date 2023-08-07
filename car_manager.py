import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_pace = 5

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_pace)

    def winwin(self):
        self.move_pace += 5







