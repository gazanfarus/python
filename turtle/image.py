# import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = [
    (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156)
]

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.teleport(-150, -150)

# colors = colorgram.extract('image.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
# print(rgb_colors)

def change_color():
    random.choice(color_list)
    return random.choice(color_list)


y_axis = -120
for _ in range(10):
    for _ in range(10):
        tim.dot(20, change_color())
        tim.forward(30)
    tim.teleport(-150, y_axis)
    y_axis += 30


screen = Screen()
screen.exitonclick()