from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout 3000")
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball((0, -350))
scoreboard = Scoreboard()

move_speed = 0.1

screen.listen()
screen.onkey(paddle.go_left, "Right")
screen.onkey(paddle.go_right, "Left")

game_is_on = True
while game_is_on:
    time.sleep(move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 275 or ball.xcor() < -285:
        ball.bounce_x()

    if ball.ycor() > 255 or ball.ycor() < -375:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -325 and ball.y_move < 0:
        ball.bounce_y()

    if ball.ycor() < -375:
        game_is_on = False

screen.exitonclick()