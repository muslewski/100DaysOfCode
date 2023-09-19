import turtle
import pandas

# Basic customization of application
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(725, 491)
turtle.penup()
turtle.shape("circle")
turtle.hideturtle()
turtle.speed(2)

# Read csv and create list of countries
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    # Get input from user
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?")
    answer = answer_state.title()

    if answer == "Exit":
        break

    # Does answer is correct?
    if answer in list_of_states and answer not in guessed_states:
        guessed_states.append(answer)
        turtle.showturtle()
        correct_row = data[data.state == answer]
        turtle.goto(int(correct_row.x), int(correct_row.y))
        turtle.color("black")
        turtle.write(answer, move=True, font=("Verdana", 8, "bold"))
        turtle.hideturtle()

print("The end!")

# states_to_learn.csv
missing_states = list(set(list_of_states) - set(guessed_states))
df = pandas.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")

screen.exitonclick()
