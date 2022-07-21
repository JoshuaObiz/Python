from turtle import Screen
import time
from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor('Black')
screen.title('Python Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


gaming = True
while gaming:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        gaming = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            gaming = False
            score.game_over()

screen.exitonclick()
