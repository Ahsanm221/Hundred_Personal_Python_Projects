from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x, rand_y)
