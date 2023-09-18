from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Turtle vs Traffic")
screen.bgpic('triptothebeach.gif')
screen.register_shape('sport.gif')
screen.register_shape('sport2.gif')
screen.register_shape('sport3.gif')
screen.register_shape('police.gif')

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.up, "space")
screen.onkey(player.up, "Return")
screen.onkey(player.up, "w")

SPEED = 0.06
game_is_on = True
while game_is_on:
    sleep(SPEED)
    car_manager.move_mechanics()
    car_manager.check_collisions()
    scoreboard.update_scoreboard()
    screen.update()


    for car in car_manager.car_list:
        if car.distance(player) < 25:
            print("sss")
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 255:
        player.reset_position()
        scoreboard.get_point()
        SPEED *= 0.7



screen.exitonclick()

