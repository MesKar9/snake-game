from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # screen.tracer(0) tracer'ı kapatır


snake = Snake()

food = Food()

score = Score()

on_game = True
while on_game:
    screen.listen()
    screen.onkey(snake.move_up, 'Up')
    screen.onkey(snake.move_down, 'Down')
    screen.onkey(snake.move_left, 'Left')
    screen.onkey(snake.move_right, 'Right')
    screen.update()
    sleep(0.1)
    snake.not_stop_motion()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_inc()
        snake.growing_snake()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        on_game = False
        score.game_over()

    # Detect collision with tail
    for tail in snake.turtles[2:]:
        if snake.head.distance(tail) < 10:
            on_game = False
            score.game_over()

        
    
    
        




















screen.exitonclick()