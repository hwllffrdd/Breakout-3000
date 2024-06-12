from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout 3000")
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball((0, -350))
scoreboard = Scoreboard()

brick_rows = 5
brick_cols = 8
brick_width = 60
brick_height = 20
brick_spacing_x = 10
brick_spacing_y = 10

bricks = []
for y in range(brick_rows):
    for x in range(brick_cols):
        x_offset = (x * (brick_width + brick_spacing_x)) - (300 - (brick_width // 2))
        if y % 2 == 0:
            x_offset += brick_width // 2
        y_offset = (y * (brick_height + brick_spacing_y)) + 50
        bricks.append(Brick((x_offset, y_offset)))

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

    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)  # Move the brick off-screen (effectively "removing" it)
            ball.bounce_y()
            bricks.remove(brick)  # Remove brick from the list

screen.exitonclick()