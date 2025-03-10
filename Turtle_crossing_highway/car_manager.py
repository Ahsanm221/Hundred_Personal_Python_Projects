from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            car = Turtle("square")
            car.setheading(180)
            car.penup()
            car.color(random.choice(COLORS))
            car.setposition(x=300, y=random.randint(-250,290))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT

    def next_level(self):
        self.inc_speed()






