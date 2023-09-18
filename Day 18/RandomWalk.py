from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBLue", "LightSeaGreen", "wheat", "SlateGray"]

path = [90, -90, 180, -180, 0, -0, 360, -360, 270, -270]

timmy.hideturtle()
timmy.speed(0)
timmy.width(10)
#
screen = Screen()
screen.colormode(255)

while 1==1:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    timmy.right(random.choice(path))
    timmy.forward(20)


# i = 0
# while i < 360:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     timmy.pencolor(r, g, b)
#     timmy.circle(200)
#     i += 5
#     timmy.right(5)



screen.exitonclick()
