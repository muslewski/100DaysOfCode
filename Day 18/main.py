import random
from turtle import Turtle, Screen
# import colorgram
#
# colors = colorgram.extract('image.jpg', 25)
# colors_list = []
# for color in colors:
#     rgb = color.rgb
#     color_tuple = (rgb.r, rgb.g, rgb.b)
#     colors_list.append(color_tuple)
# print(colors_list)

color_hirst_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83),
                    (109, 67, 85), (39, 35, 34), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48),
                    (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181),
                    (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)

timmy.penup()
timmy.pensize(5)
x = -400
y = -370
timmy.goto(x, y)

for i in range(10):
    for i in range(10):
        timmy.pendown()
        timmy.pencolor(random.choice(color_hirst_list))
        timmy.circle(8)
        timmy.penup()
        timmy.forward(80)
        y+=8
        x+=0
    timmy.goto(x,y)



screen.exitonclick()

