import colorgram
import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)

colors = colorgram.extract('image.jpg', 10)
colors.rgb()
print(colors)