from turtle import Turtle
import random
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.seth(180)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x=300, y=random.randint(-200, 245))

    def move(self, game_level):
        self.forward(STARTING_MOVE_DISTANCE + 10 * game_level)


