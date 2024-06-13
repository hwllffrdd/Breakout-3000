from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Lucida Console", 34, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 5
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
        self.goto(0, 300)
        self.write(f"Score: {self.score}, Lives: {self.life}", align=ALIGNMENT, font=FONT)
        self.draw_divider()

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def lostlife(self):
        self.life -= 1
        self.update_scoreboard()

    def win(self):
        self.goto(0,0)
        self.write(f"We did it Joe!", align=ALIGNMENT, font=FONT)

    def lose(self):
        self.goto(0,0)
        self.write(f"So sad!", align=ALIGNMENT, font=FONT)
