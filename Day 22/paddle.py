from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, 0)
        self.shapesize(5, 1)
        self.turtlesize(5, 1)

    def up(self):
        y = self.ycor()
        yg = y + 20
        self.sety(yg)

    def down(self):
        y = self.ycor()
        yg = y - 20
        self.sety(yg)
