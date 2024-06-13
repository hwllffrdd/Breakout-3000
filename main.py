import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick
import time
from tkinter import Button, Tk, Frame


def pause_game():
    global game_is_paused
    game_is_paused = not game_is_paused


def restart_game():
    global game_is_on, game_is_paused, scoreboard, bricks

    game_is_paused = True
    game_is_on = True

    scoreboard.score = 0
    scoreboard.life = 5
    scoreboard.update_scoreboard()

    ball.reset_position()

    for brick in bricks:
        brick.goto(1000, 1000)  # Move bricks out of view
    bricks.clear()
    create_bricks()

    game_is_paused = False


def create_bricks():
    global bricks
    for y in range(brick_rows):
        for x in range(brick_cols):
            x_offset = (x * (brick_width + brick_spacing_x)) - (300 - (brick_width // 2))
            if y % 2 == 0:
                x_offset += brick_width // 2
            y_offset = (y * (brick_height + brick_spacing_y)) + 50
            bricks.append(Brick((x_offset, y_offset)))


screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout 3000")
screen.tracer(0)


root = screen._root
root.configure(bg='black')

button_frame = Frame(root, bg='black')
button_frame.pack(pady=10)

pause_btn = Button(button_frame, text="Pause", command=pause_game, bg='grey', fg='white', font=('Lucida Console', 12))
pause_btn.pack(side='left', padx=10)

restart_btn = Button(button_frame, text="Restart", command=restart_game, bg='grey', fg='white', font=('Lucida Console', 12))
restart_btn.pack(side='right', padx=10)


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
create_bricks()

move_speed = 0.1
game_is_on = True
game_is_paused = False


screen.listen()
screen.onkey(paddle.go_left, "Right")
screen.onkey(paddle.go_right, "Left")

while game_is_on:
    if not game_is_paused:
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
            scoreboard.lostlife()
            ball.reset_position()
            if scoreboard.life == 0:
                game_is_on = False
                scoreboard.lose()

        for brick in bricks:
            if ball.distance(brick) < 34:
                brick.goto(1000, 1000)
                ball.bounce_y()
                bricks.remove(brick)
                scoreboard.point()
                move_speed *= 0.95

        if not bricks:
            game_is_on = False
            scoreboard.win()

    screen.update()


screen.exitonclick()