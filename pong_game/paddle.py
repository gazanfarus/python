from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.shapesize(stretch_wid=5, stretch_len=1)
        turtle.goto(position)

    def move_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)

