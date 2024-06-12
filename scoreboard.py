from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        self.draw_divider()

    def draw_divider(self):
        self.goto(-300, 275)
        self.setheading(0)
        self.pendown()
        self.forward(600)
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()