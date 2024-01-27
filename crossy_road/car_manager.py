from turtle import Turtle
import random
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.penup()
        self.goto(-300, -300)

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.seth(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=300, y=random.randint(-200, 245))
            self.all_cars.append(new_car)

    def move(self, game_level):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + 10 * game_level)


