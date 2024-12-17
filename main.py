from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, key = 'Up')
screen.onkey(snake.down, key = 'Down')
screen.onkey(snake.right, key = 'Right')
screen.onkey(snake.left, key = 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_increase()

    if snake.segments[0].ycor() > 260 or snake.segments[0].ycor() < -280 or \
            snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290:
        game_is_on = False
        score.game_over()



screen.exitonclick()
print("game over")