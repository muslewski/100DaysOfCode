from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 235)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def get_point(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)

