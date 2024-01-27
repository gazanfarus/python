from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Python the Snake")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
