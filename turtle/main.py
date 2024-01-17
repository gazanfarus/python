import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)


tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.pensize(15)
# tim.color("red")


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(200):
    tim.seth(random.choice([0, 90, 180, 270]))
    tim.forward(20)
    tim.color(change_color())
# for _ in range(4):
#    tim.forward(100)
#    tim.right(90)


# def draw_angler(sides):
#    degree = 360 / sides
#    for _ in range(sides):
#        tim.forward(100)
#        tim.right(degree)

# for shape_side in range(3, 11):
#    draw_angler(shape_side)
#    change_color()


screen = Screen()
screen.exitonclick()
