from turtle import Screen
import time
from food import Food

from snake import Snake

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()  # update screen here to avoid the choppy animation
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
