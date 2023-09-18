from turtle import Turtle
import random
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = ["sport.gif", "sport2.gif", "sport3.gif"]

class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []
        for car in range(50):
            new_car = Turtle()

            new_car.shape(random.choice(CARS))
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(random.randint(-300,300), self.car_y_position())
            new_car.color(random.choice(COLORS))
            self.car_list.append(new_car)


    def move_mechanics(self):
        random_cars = random.sample(self.car_list, 20)
        for random_car in random_cars:
            if random_car.xcor() < -300:
                random_car.setx(350)

        for car in self.car_list:
            car.forward(2)

    def check_collisions(self):
        cars_to_remove = []
        for i in range(len(self.car_list)):
            car1 = self.car_list[i]
            for j in range(i + 1, len(self.car_list)):
                car2 = self.car_list[j]
                if car1.distance(car2) < 50:
                    car2.hideturtle()
                    cars_to_remove.append(car2)

        for car in cars_to_remove:
            if car in self.car_list:
                self.car_list.remove(car)

    def car_y_position(self):
        y_up_top = random.randint(175, 200)
        y_up_middle = random.randint(115, 142)
        y_up_bottom = random.randint(60, 85)

        y_down_top = random.randint(-85, -60)
        y_down_middle = random.randint(-145, -120)
        y_down_bottom = random.randint(-200, -175)

        possible_car_y = [y_up_top, y_up_middle, y_up_bottom, y_down_top, y_down_middle, y_down_bottom]
        car_y = random.choice(possible_car_y)
        return car_y


