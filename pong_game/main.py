from turtle import Turtle, Screen

def

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

turtle = Turtle("square")
turtle.color("white")
turtle.penup()
turtle.seth(90)
turtle.shapesize(stretch_wid=None, stretch_len=5)
turtle.goto(x=350, y=0)
turtle.onkey(fun, key="w")


screen.exitonclick()