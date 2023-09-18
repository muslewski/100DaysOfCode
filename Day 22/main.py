from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Kento The Pong")
screen.tracer(0)

paddle1 = Paddle(-350)
paddle2 = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
