from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.current_level = 1

    def level(self):
        self.goto(0, 250)
        self.write(f"Level {self.current_level}", False, "center", ("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, "center", ("Arial", 20, "normal"))

    def next_level(self):
        self.clear()
        self.current_level += 1
        self.goto(0, 250)
        self.write(f"Level {self.current_level}", False, "center", ("Courier", 24, "normal"))

