from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.move_up, key="w")
screen.onkey(l_paddle.move_down, key="s")

screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
