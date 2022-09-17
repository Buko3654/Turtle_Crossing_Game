from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 300


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        traffic = random.randint(1, 5)
        if traffic == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(STARTING_X, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def drive(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
