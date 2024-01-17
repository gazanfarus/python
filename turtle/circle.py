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


def draw_spirograph(offset):
    for _ in range(int(360 / offset)):
        tim.color(change_color())
        tim.circle(100)
        tim.seth(tim.heading() + offset)
    tim.color("black")

draw_spirograph(10)


screen = Screen()
screen.exitonclick()
