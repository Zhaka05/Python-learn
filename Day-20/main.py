from turtle import Screen


from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
import scoreboard













screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create a snake body
snake = Snake()
food = Food()
score = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()


    # Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            game_is_on = False
            score.game_over()





screen.exitonclick()