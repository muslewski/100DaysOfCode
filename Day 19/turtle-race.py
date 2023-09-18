from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
colors = ["purple", "red", "yellow", "orange", "green", "blue"]
all_turtles = []

y = 70
i = 0
for animals in colors:
    animal = Turtle(shape = "turtle")
    animal.color(colors[i])
    animal.penup()
    animal.goto(-230, y)
    all_turtles.append(animal)
    y-=30
    i+=1


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

print(colors)

screen.exitonclick()
