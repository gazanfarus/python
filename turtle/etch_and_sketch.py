from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.speed(0)
tim.pensize(5)


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.seth(tim.heading() + 10)

def turn_right():
    tim.seth(tim.heading() - 10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=tim.reset)
screen.onkey(key="r", fun=tim.penup)
screen.onkey(key="R", fun=tim.pendown)

screen.exitonclick()
