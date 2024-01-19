from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        starting_x_position = 0
        for _ in range(0, 3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=starting_x_position, y=0)
            starting_x_position -= 20
            self.snake.append(turtle)

# Snake movement
    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.seth(90)

    def down(self):
        self.head.seth(270)

    def left(self):
        self.head.seth(180)

    def right(self):
        self.head.seth(0)


