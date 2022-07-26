from turtle import Screen, Turtle
from snake import Snake
import time










# Control the snake
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create a snake body
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()






screen.exitonclick()