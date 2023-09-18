from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.pensize(10)
def move_forwards():
        tim.forward(7)


def move_backwards():
    tim.backward(7)


def move_left():
    tim.left(7)


def move_right():
    tim.right(7)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()

