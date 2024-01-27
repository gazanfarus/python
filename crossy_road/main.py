import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.onkey(fun=player.move, key="Up")
score = Scoreboard()
cars = CarManager()

# y_check = -200
# turtle = Turtle()
# turtle.penup()
# turtle.goto(x=300, y=y_check)
# turtle.pendown()
# turtle.goto(x=-300, y=y_check)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move(score.level)

    if player.distance(cars) < 30:
        game_is_on = False
        score.game_over()

    if player.ycor() > 260:
        score.next_level()
        player.reset_pos()

screen.exitonclick()

