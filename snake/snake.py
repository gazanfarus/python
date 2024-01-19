from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        self.starting_x_position = 0
        for _ in range(0, 3):
            self.turtle = Turtle("square")
            #    turtle = Turtle("turtle")
            self.turtle.color("white")
            self.turtle.penup()
            self.turtle.goto(x=self.starting_x_position, y=0)
            self.starting_x_position -= 20
            self.snake.append(self.turtle)

# Snake movement
    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)
        self.snake[0].forward(20)