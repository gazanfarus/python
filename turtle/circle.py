import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)


tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.pensize(1)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


degree = 0
circles = 10

for _ in range(circles):
    tim.circle(100)
    tim.seth(degree)
    degree += 360/circles
    tim.color(change_color())


screen = Screen()
screen.exitonclick()
