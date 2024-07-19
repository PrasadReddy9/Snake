import time
from turtle import Screen
from food import Food
from scoreboard import Score
from snake import Snake
screen = Screen()
snake = Snake()
food = Food()
scores = Score()

screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(800, 800)
screen.listen()
screen.tracer(0)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

is_go = True
while is_go:
    screen.update()
    time.sleep(0.5)
    snake.move()
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scores.increase()
    if snake.segment[0].xcor() < -380 or snake.segment[0].xcor() > 380 or snake.segment[0].ycor() < -380 or snake.segment[0].ycor() > 380:
        is_go = False
        scores.game()


screen.exitonclick()