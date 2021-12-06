from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.plus()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()

    for i in snake.snake[1:]:
        if snake.head.distance(i) < 10:
            game_on = False
            scoreboard.reset()


screen.exitonclick()


# snake = []

# for i in range(0,3):
#     my_t = Turtle(shape="square")
#     my_t.color("white")
#     my_t.penup()
#     my_t.setx(i * -20)
#     snake.append(my_t)
